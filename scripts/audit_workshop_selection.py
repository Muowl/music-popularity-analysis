"""Audit current catalogue concordance without reconstructing missing historical facts."""
import argparse
import concurrent.futures
import hashlib
import json
import statistics
from datetime import datetime, timezone
from pathlib import Path
from urllib.request import Request, urlopen
from prepare_workshop import inventory, MetaParser, SEED

ROOT = Path(__file__).resolve().parents[1]


def collect(row):
    track = row["track_id"]
    url = "https://open.spotify.com/track/" + track
    result = {"url": url, "retrieved_at_utc": datetime.now(timezone.utc).isoformat()}
    cache = ROOT / "data/raw/workshop-catalogue-recheck"
    cache.mkdir(parents=True, exist_ok=True)
    try:
        with urlopen(Request(url, headers={"User-Agent": "Mozilla/5.0"}), timeout=25) as response:
            body = response.read()
            result["http_status"] = response.status
        (cache / f"{track}.html").write_bytes(body)
        parser = MetaParser()
        parser.feed(body.decode("utf-8", errors="replace"))
        canonical = (parser.facts.get("og:url") or "").rstrip("/").split("/")[-1]
        release = parser.facts.get("music:release_date") or ""
        result.update(page_sha256=hashlib.sha256(body).hexdigest(), canonical_track_id=canonical,
                      identity_verified=canonical == track, catalogue_date=release or None,
                      catalogue_year=int(release[:4]) if release[:4].isdigit() else None)
    except (OSError, ValueError) as exc:
        result["error_type"] = type(exc).__name__
    return result


def audit(collect_current=False):
    raw_audit, linked = inventory(ROOT)
    lock_path = ROOT / "data/workshop/selection-lock.json"
    lock = json.loads(lock_path.read_text())
    frozen = {r["track_id"]: r for r in lock["candidates"]}
    cache = ROOT / "data/processed/workshop-catalogue-recheck.json"
    if collect_current:
        with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
            current = dict(zip((r["track_id"] for r in linked), pool.map(collect, linked)))
        cache.parent.mkdir(exist_ok=True)
        cache.write_text(json.dumps(current, ensure_ascii=False, indent=2)+"\n")
    else:
        if cache.exists():
            current = json.loads(cache.read_text())
        else:
            published = json.loads((ROOT / "data/workshop/selection-audit.json").read_text())
            current = {r["track_id"]: r["current_observation"] for r in published["records"]}
    records = []
    for row in linked:
        track = row["track_id"]
        original = frozen.get(track)
        meta = current[track]
        reasons = list(row["metadata_exclusion_reasons"])
        if not meta.get("identity_verified") or not meta.get("catalogue_year"):
            reasons.append("current_catalogue_identity_or_year_unverified")
        elif not 1980 <= meta["catalogue_year"] <= 1989:
            reasons.append("current_catalogue_year_outside_window")
        records.append({"track_id": track, "artist": row["Artist"],
                        "snapshot_filter_exclusions": row["metadata_exclusion_reasons"],
                        "historical_catalogue_date": original["catalogue_date"] if original else None,
                        "historical_page_sha256": original["catalogue_page_sha256"] if original else None,
                        "historical_evidence_status": "selected_case_preserved_in_lock" if original else "original_observation_not_available",
                        "current_observation": meta, "current_exclusions": reasons,
                        "selection_hash": hashlib.sha256(f"{SEED}|{track}".encode()).hexdigest(),
                        "selected_in_frozen_roster": original is not None})
    chosen = {}
    for row in sorted((r for r in records if not r["current_exclusions"]), key=lambda r: (r["selection_hash"], r["track_id"])):
        chosen.setdefault(row["artist"], row["track_id"])
    ids = set(chosen.values())
    views = {r["track_id"]: r.get("views") for r in linked}
    complete = all(r["current_observation"].get("identity_verified") and r["current_observation"].get("catalogue_year") for r in records)
    result = {"scope": "Current catalogue concordance audit; not a reconstruction of the historical selection",
              "selection_lock_sha256": hashlib.sha256(lock_path.read_bytes()).hexdigest(),
              "original_full_catalogue_cache_available": False,
              "historical_metadata_available": len(frozen), "historical_metadata_missing": len(records)-len(frozen),
              "raw_snapshot_audit": raw_audit,
              "current_comparison": {"complete": complete,
                                     "catalogue_verified": sum(bool(r["current_observation"].get("identity_verified")) for r in records),
                                     "request_failures": sum("error_type" in r["current_observation"] for r in records),
                                     "eligible_decade_rows": sum(not r["current_exclusions"] for r in records) if complete else None,
                                     "selected_artists": len(chosen) if complete else None,
                                     "selected_ids_match_lock": ids == set(frozen) if complete else None,
                                     "new_ids": sorted(ids-set(frozen)) if complete else None,
                                     "missing_frozen_ids": sorted(set(frozen)-ids) if complete else None,
                                     "cutoff_views": statistics.median(views[t] for t in ids) if complete and ids else None,
                                     "changed_selected_catalogue_dates": [r["track_id"] for r in records if r["selected_in_frozen_roster"] and r["current_observation"].get("identity_verified") and r["current_observation"].get("catalogue_date") and r["historical_catalogue_date"] != r["current_observation"]["catalogue_date"]]},
              "records": records}
    output = ROOT / "data/processed/workshop-selection-audit.json"
    output.write_text(json.dumps(result, ensure_ascii=False, indent=2)+"\n")
    print(json.dumps(result["current_comparison"], indent=2))


if __name__ == "__main__":
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--collect-current", action="store_true", help="Acquire current pages; never overwrite the historical lock")
    audit(p.parse_args().collect_current)
