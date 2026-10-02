"""Collect current publication metadata for frozen video IDs; never refresh views."""
import concurrent.futures
import hashlib
import json
import re
from datetime import datetime, timezone, date
from pathlib import Path
from urllib.parse import urlparse, parse_qs
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]


def extract(text, expected_id, observed_date):
    match = re.search(r'(?:var\s+)?ytInitialPlayerResponse\s*=\s*', text)
    if not match:
        return {"status": "player_not_found"}
    player, _ = json.JSONDecoder().raw_decode(text[match.end():])
    details = player.get("videoDetails", {})
    micro = player.get("microformat", {}).get("playerMicroformatRenderer", {})
    facts = {"video_id": details.get("videoId"), "publish_date_raw": micro.get("publishDate"),
             "upload_date_raw": micro.get("uploadDate"), "title": details.get("title")}
    if facts["video_id"] != expected_id:
        return dict(facts, status="identity_mismatch")
    raw = facts["publish_date_raw"]
    if not raw:
        return dict(facts, status="publication_missing")
    published = date.fromisoformat(raw[:10])
    if published > date.fromisoformat(observed_date):
        return dict(facts, status="publication_after_snapshot")
    return dict(facts, status="verified_publication", published_date=published.isoformat(),
                date_rule="First ISO date component of YouTube publishDate; platform calendar date, not converted to UTC")


def collect(case):
    url = case["video_url"]
    result = {"candidate_id": case["candidate_id"], "url": url,
              "retrieved_at_utc": datetime.now(timezone.utc).isoformat()}
    cache = ROOT / "data/raw/workshop-video-pages"
    cache.mkdir(parents=True, exist_ok=True)
    try:
        with urlopen(Request(url, headers={"User-Agent": "Mozilla/5.0"}), timeout=25) as response:
            body = response.read()
            result.update(http_status=response.status, resolved_url=response.url)
        (cache / f"{case['candidate_id']}.html").write_bytes(body)
        result["page_sha256"] = hashlib.sha256(body).hexdigest()
        expected = parse_qs(urlparse(url).query)["v"][0]
        result.update(extract(body.decode("utf-8", errors="replace"), expected, case["views_observed_date"]))
    except (OSError, ValueError, KeyError) as exc:
        result.update(status="request_or_parse_failed", error_type=type(exc).__name__)
    return result


def main():
    lock_path = ROOT / "data/workshop/selection-lock.json"
    lock = json.loads(lock_path.read_text())
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
        records = list(pool.map(collect, lock["candidates"]))
    result = {"scope": "Current exact-video publication metadata; historical audience remains unchanged; no audio or video-format review",
              "selection_lock_sha256": hashlib.sha256(lock_path.read_bytes()).hexdigest(), "records": records}
    output = ROOT / "data/processed/workshop-video-metadata.json"
    output.parent.mkdir(exist_ok=True)
    output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({r["candidate_id"]: r["status"] for r in records}))


if __name__ == "__main__":
    main()
