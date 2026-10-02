"""Freeze a metadata-only Hard Rock roster; never inspect audio features."""
import argparse
import csv
import hashlib
import json
import statistics
from collections import Counter
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
SEED = "hard-rock-workshop-v1"
FEATURES = ["Energy", "Danceability", "Acousticness"]


class MetaParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.facts = {}

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        key = attrs.get("property", attrs.get("name", ""))
        if tag == "meta" and key in {
            "og:title", "og:url", "og:description", "music:release_date",
            "music:duration", "music:album", "music:musician_description",
        }:
            self.facts[key] = attrs.get("content")


def load_sources(root=ROOT):
    manifest = json.loads((root / "data/source-manifest.json").read_text())
    paths = {}
    for source in manifest["sources"]:
        path = root / source["local_path"]
        actual = hashlib.sha256(path.read_bytes()).hexdigest()
        if actual != source["sha256"]:
            raise ValueError(f"Source hash mismatch: {path}")
        paths[source["name"]] = path
    with paths["Spotify Tracks Dataset"].open(newline="", encoding="utf-8-sig") as f:
        genre_rows = [r for r in csv.DictReader(f) if r["track_genre"] == "hard-rock"]
    genre_ids = {r["track_id"] for r in genre_rows}
    # Copy only metadata: the selection cannot depend on musical outcomes.
    metadata_fields = ["Artist", "Track", "Uri", "Url_youtube", "Views", "official_video",
                       "Duration_ms", "Album", "Album_type", "Title", "Channel"]
    with paths["Spotify and Youtube"].open(newline="", encoding="utf-8-sig") as f:
        pairs = [{k: r[k] for k in metadata_fields} for r in csv.DictReader(f)]
    return manifest, genre_rows, genre_ids, pairs


def inventory(root=ROOT):
    manifest, genre_rows, genre_ids, pairs = load_sources(root)
    uri_counts = Counter(r["Uri"] for r in pairs)
    video_counts = Counter(r["Url_youtube"] for r in pairs)
    linked = [dict(r, track_id=r["Uri"].removeprefix("spotify:track:"))
              for r in pairs if r["Uri"].removeprefix("spotify:track:") in genre_ids]
    audit = {"genre_label": "hard-rock", "genre_rows": len(genre_rows),
             "genre_unique_ids": len(genre_ids), "intersection_rows": len(linked),
             "intersection_unique_ids": len({r["track_id"] for r in linked}),
             "intersection_artists": len({r["Artist"] for r in linked}),
             "sources": [{k: s[k] for k in ("name", "sha256", "landing_url")} for s in manifest["sources"]]}
    for r in linked:
        reasons = []
        if r["official_video"].lower() != "true":
            reasons.append("publisher_official_video_not_true")
        if uri_counts[r["Uri"]] != 1:
            reasons.append("duplicate_uri_in_pair_source")
        if not r["Url_youtube"] or video_counts[r["Url_youtube"]] != 1:
            reasons.append("missing_or_duplicate_video_in_pair_source")
        try:
            views = float(r["Views"])
            if not views.is_integer() or views <= 0:
                raise ValueError()
            r["views"] = int(views)
        except ValueError:
            reasons.append("missing_or_invalid_positive_views")
        r["metadata_exclusion_reasons"] = reasons
    return audit, linked


def collect_catalogue(root=ROOT):
    _, linked = inventory(root)
    cache = root / "data/raw/hard-rock-pages"
    cache.mkdir(parents=True, exist_ok=True)
    observations = []
    for r in linked:
        track = r["track_id"]
        saved = cache / f"{track}.json"
        if saved.exists():
            result = json.loads(saved.read_text())
            body = (cache / f"{track}.html").read_bytes()
            if hashlib.sha256(body).hexdigest() != result["page_sha256"]:
                raise ValueError(f"Cache hash mismatch: {track}")
        else:
            url = f"https://open.spotify.com/track/{track}"
            result = {"track_id": track, "url": url, "retrieved_at_utc": datetime.now(timezone.utc).isoformat()}
            try:
                with urlopen(Request(url, headers={"User-Agent": "Mozilla/5.0"}), timeout=20) as response:
                    body = response.read()
                    result.update(http_status=response.status, resolved_url=response.url)
                (cache / f"{track}.html").write_bytes(body)
                result["page_sha256"] = hashlib.sha256(body).hexdigest()
            except OSError as exc:
                result["error_type"] = type(exc).__name__
                observations.append(result)
                continue
        parser = MetaParser()
        parser.feed(body.decode("utf-8", errors="replace"))
        result["facts"] = parser.facts
        result["canonical_track_id"] = (parser.facts.get("og:url") or "").rstrip("/").split("/")[-1]
        result["identity_verified"] = result["canonical_track_id"] == track
        date = parser.facts.get("music:release_date", "")
        result["catalogue_date"] = date
        result["catalogue_year"] = int(date[:4]) if date[:4].isdigit() else None
        result["scope"] = "Spotify edition/catalogue date, not validated original recording release"
        saved.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
        observations.append(result)
    output = root / "data/processed/hard-rock-catalogue-observations.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(observations, ensure_ascii=False, indent=2) + "\n")
    print(f"Catalogue observations: {len(observations)}; verified exact IDs: {sum(r.get('identity_verified', False) for r in observations)}")


def freeze(root=ROOT):
    destination = root / "data/workshop/selection-lock.json"
    if destination.exists():
        raise ValueError("Selection already frozen; do not overwrite. Review a versioned protocol amendment.")
    audit, linked = inventory(root)
    observations = json.loads((root / "data/processed/hard-rock-catalogue-observations.json").read_text())
    catalogue = {r["track_id"]: r for r in observations}
    eligible = []
    for r in linked:
        c = catalogue[r["track_id"]]
        r["catalogue_year"] = c.get("catalogue_year")
        if not c.get("identity_verified") or not c.get("catalogue_year"):
            r["metadata_exclusion_reasons"].append("catalogue_identity_or_year_unverified")
        if not r["metadata_exclusion_reasons"]:
            eligible.append(r)
    decade = [r for r in eligible if 1980 <= r["catalogue_year"] <= 1989]
    for r in decade:
        r["selection_hash"] = hashlib.sha256(f"{SEED}|{r['track_id']}".encode()).hexdigest()
    chosen = {}
    for r in sorted(decade, key=lambda r: (r["selection_hash"], r["track_id"])):
        chosen.setdefault(r["Artist"], r)
    selected = sorted(chosen.values(), key=lambda r: (r["views"], r["track_id"]))
    cutoff = statistics.median(r["views"] for r in selected)
    cases = []
    for i, r in enumerate(selected, 1):
        c = catalogue[r["track_id"]]
        cases.append({
            "candidate_id": f"HR{i:02d}", "title": r["Track"], "artist": r["Artist"],
            "track_id": r["track_id"], "spotify_url": c["url"], "video_url": r["Url_youtube"],
            "video_title_snapshot": r["Title"], "channel_snapshot": r["Channel"],
            "album_snapshot": r["Album"], "album_type": r["Album_type"],
            "spotify_duration_ms_snapshot": r["Duration_ms"], "views": r["views"],
            "audience_group": "lower" if r["views"] < cutoff else "higher",
            "views_observed_date": "2023-02-07", "views_date_precision": "day_declared",
            "views_date_source_url": "https://www.kaggle.com/datasets/salvatorerastelli/spotify-and-youtube",
            "catalogue_date": c["catalogue_date"], "catalogue_year": c["catalogue_year"],
            "catalogue_date_scope": c["scope"], "catalogue_metadata_retrieved_at_utc": c["retrieved_at_utc"],
            "catalogue_page_sha256": c["page_sha256"], "selection_hash": r["selection_hash"],
            "video_published_at": "", "video_format": "pending", "recording_review": "pending",
            "reviewer": "", "review_evidence": "", "decision": "pending", "exclusion_reason": "",
        })
    audit.update(eligible_metadata_rows=len(eligible), eligible_metadata_artists=len({r["Artist"] for r in eligible}),
                 decade_rows=len(decade), decade_artists=len(chosen), selected=len(cases))
    lock = {"status": "frozen_candidates_not_approved_recordings", "created_at_utc": datetime.now(timezone.utc).isoformat(),
            "protocol": "docs/workshop-protocolo.md", "seed": SEED, "catalogue_year_window": [1980, 1989],
            "max_tracks_per_artist": 1, "audience_cutoff_views": cutoff,
            "cutoff_population": "one hash-selected track per eligible artist in the 1980–1989 catalogue window",
            "groups": dict(Counter(r["audience_group"] for r in cases)), "reserves": [],
            "features_prespecified": FEATURES, "audit": audit, "candidates": cases}
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(json.dumps(lock, ensure_ascii=False, indent=2) + "\n")
    with (destination.parent / "recording-review.csv").open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(cases[0]), lineterminator="\n")
        writer.writeheader()
        writer.writerows(cases)
    processed = root / "data/processed"
    processed.mkdir(exist_ok=True)
    (processed / "hard-rock-eligibility-audit.json").write_text(json.dumps(linked, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({k: lock[k] for k in ["created_at_utc", "audience_cutoff_views", "groups", "audit"]}, indent=2))


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("action", choices=["collect-catalogue", "freeze"])
    p.add_argument("--root", type=Path, default=ROOT)
    args = p.parse_args()
    (collect_catalogue if args.action == "collect-catalogue" else freeze)(args.root)


if __name__ == "__main__":
    main()
