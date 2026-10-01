"""Search public Apple catalogue metadata; candidates require manual review.

Existing raw search responses are reused. Never infer recording identity
from result rank. Network responses and timestamps are saved locally.
"""
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import urlopen

ROOT = Path(__file__).resolve().parents[1]
FIELDS = ('trackId', 'artistName', 'trackName', 'collectionName', 'releaseDate',
          'primaryGenreName', 'trackTimeMillis', 'trackViewUrl')


def main():
    cases = json.loads((ROOT / 'data/pilot/metadata-candidates.json').read_text())['candidates']
    cache = ROOT / 'data/raw/apple-search'
    cache.mkdir(parents=True, exist_ok=True)
    results = []
    for case in cases:
        path = cache / (case['pilot_id'] + '.json')
        if not path.exists():
            url = 'https://itunes.apple.com/search?' + urlencode({
                'term':case['artist']+' '+case['track'], 'entity':'song', 'limit':10, 'country':'us'})
            observed = datetime.now(timezone.utc).isoformat()
            with urlopen(url, timeout=25) as response:
                data = json.load(response)
            path.write_text(json.dumps({'url':url, 'retrieved_at_utc':observed, 'response':data}),encoding='utf-8')
        stored = json.loads(path.read_text())
        results.append({'pilot_id':case['pilot_id'], 'query_url':stored['url'],
            'retrieved_at_utc':stored.get('retrieved_at_utc'),
            'cache_saved_at_utc':datetime.fromtimestamp(path.stat().st_mtime,timezone.utc).isoformat(),
            'cache_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
            'note':'Search result is a candidate, not a validated cross-platform match. Legacy cache has save time only.',
            'candidates':[{k:r.get(k) for k in FIELDS} for r in stored['response'].get('results',[])]})
    (ROOT / 'data/pilot/catalogue-search.json').write_text(json.dumps(results,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')


if __name__ == '__main__':
    main()
