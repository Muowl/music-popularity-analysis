"""Retrieve public exact-identity pages; retain observations separately from review."""
import concurrent.futures
import argparse
import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.error import HTTPError

ROOT = Path(__file__).resolve().parents[1]


def spotify_jsonld(text):
    facts = []
    blocks = re.findall(r'<script[^>]*type=["\']application/ld\+json["\'][^>]*>(.*?)</script>', text, re.S)
    for block in blocks:
        try:
            data = json.loads(block)
        except json.JSONDecodeError:
            continue
        for item in data if isinstance(data, list) else [data]:
            if isinstance(item, dict) and 'MusicRecording' in item.get('@type', []):
                facts.append({k:v for k,v in item.items() if k in
                    ('@type','name','datePublished','duration','byArtist','inAlbum','genre','url')})
    return facts


def retrieve(case, platform):
    url = case['video_url'] if platform == 'youtube' else 'https://open.spotify.com/track/' + case['track_id']
    observed = datetime.now(timezone.utc).isoformat()
    result = {'pilot_id': case['pilot_id'], 'platform': platform, 'url': url,
              'metadata_retrieved_at_utc': observed}
    cache = ROOT / 'data/raw/metadata-pages'
    cache.mkdir(parents=True, exist_ok=True)
    try:
        request = Request(url, headers={'User-Agent': 'Mozilla/5.0 (compatible; AcademicMetadataPilot/1.0)'})
        with urlopen(request, timeout=25) as response:
            body = response.read()
            result['http_status'] = response.status
            result['resolved_url'] = response.url
        (cache / f"{case['pilot_id']}-{platform}.html").write_bytes(body)
        result['page_sha256'] = hashlib.sha256(body).hexdigest()
        result['bytes'] = len(body)
        text = body.decode('utf-8',errors='replace')
        if platform == 'youtube':
            match = re.search(r'(?:var\s+)?ytInitialPlayerResponse\s*=\s*', text)
            if match:
                data, _ = json.JSONDecoder().raw_decode(text[match.end():])
                video = data.get('videoDetails', {})
                micro = data.get('microformat', {}).get('playerMicroformatRenderer', {})
                result['playability_status'] = data.get('playabilityStatus', {}).get('status')
                result['video_id'] = video.get('videoId')
                result['title'] = video.get('title')
                result['author'] = video.get('author')
                result['length_seconds'] = video.get('lengthSeconds')
                result['publish_date_raw'] = micro.get('publishDate')
                result['upload_date_raw'] = micro.get('uploadDate')
                result['category'] = micro.get('category')
                # Descriptions remain local for contextual review, not bulk redistribution.
                (cache / f"{case['pilot_id']}-description.txt").write_text(video.get('shortDescription',''),encoding='utf-8')
                result['extraction_status'] = 'player_metadata' if video else 'player_without_video_details'
            else:
                result['extraction_status'] = 'player_not_found'
        else:
            result['jsonld'] = spotify_jsonld(text)
            result['extraction_status'] = 'jsonld' if result['jsonld'] else 'jsonld_not_found'
    except (OSError, ValueError) as error:
        result['extraction_status'] = 'request_or_parse_failed'
        result['error_type'] = type(error).__name__
        if isinstance(error, HTTPError):
            result['http_status'] = error.code
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--reparse-cache', action='store_true', help='Reparse Spotify JSON-LD without fresh network reads')
    args = parser.parse_args()
    out = ROOT / 'data/pilot/metadata-observations.json'
    if args.reparse_cache:
        results = json.loads(out.read_text())
        for result in results:
            if result['platform'] == 'spotify' and result.get('http_status') == 200:
                path = ROOT / f"data/raw/metadata-pages/{result['pilot_id']}-spotify.html"
                body = path.read_bytes()
                assert hashlib.sha256(body).hexdigest() == result['page_sha256']
                result['jsonld'] = spotify_jsonld(body.decode('utf-8',errors='replace'))
                result['extraction_status'] = 'jsonld' if result['jsonld'] else 'jsonld_not_found'
        out.write_text(json.dumps(results,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
        return
    cases = json.loads((ROOT / 'data/pilot/metadata-candidates.json').read_text())['candidates']
    tasks = [(c, p) for c in cases for p in ['youtube','spotify']]
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
        results = list(pool.map(lambda args: retrieve(*args), tasks))
    out.write_text(json.dumps(results,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    for r in results:
        print(r['pilot_id'],r['platform'],r['extraction_status'],r.get('publish_date_raw'),r.get('jsonld'))


if __name__ == '__main__':
    main()
