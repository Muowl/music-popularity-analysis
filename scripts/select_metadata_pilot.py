"""Freeze a metadata-access pilot without using audio feature values."""
import csv
import hashlib
import json
from collections import Counter, defaultdict
from pathlib import Path

from audit_sources import audience_band, number

ROOT = Path(__file__).resolve().parents[1]
SEED = 'metadata-pilot-v1-2026-10-01'
EXPECTED_SHA = 'a08bda951ec1c62a2fbaeb5547141ba23dd7b16347f0e83bd043b1ba9cf168cd'


def main():
    source = ROOT / 'data/raw/spotify_youtube.csv'
    if hashlib.sha256(source.read_bytes()).hexdigest() != EXPECTED_SHA:
        raise ValueError('Unexpected source snapshot')
    with source.open(newline='', encoding='utf-8') as handle:
        rows = list(csv.DictReader(handle))
    uris = Counter(r['Uri'] for r in rows)
    videos = Counter(r['Url_youtube'] for r in rows if r['Url_youtube'])
    excluded = Counter()
    pool = defaultdict(list)
    for r in rows:
        views = number(r['Views'])
        if not r['Url_youtube'] or views is None or views < 0 or not views.is_integer():
            excluded['missing_or_invalid_video_views'] += 1
        elif r['official_video'] != 'True':
            excluded['not_marked_official'] += 1
        elif uris[r['Uri']] != 1 or videos[r['Url_youtube']] != 1:
            excluded['nonunique_uri_or_video'] += 1
        else:
            key = hashlib.sha256((SEED + '|' + r['Uri'] + '|' + r['Url_youtube']).encode()).hexdigest()
            pool[audience_band(views)].append((key, r))
    selected = []
    for band, candidates in sorted(pool.items()):
        if len(candidates) < 3:
            raise ValueError(f'Insufficient rows in {band}')
        for key, r in sorted(candidates, key=lambda x: x[0])[:3]:
            selected.append({'pilot_id': f'P{len(selected)+1:02d}', 'audience_band': band,
                'source_row_index': r[''], 'track_id': r['Uri'].removeprefix('spotify:track:'),
                'artist': r['Artist'], 'track': r['Track'], 'album': r['Album'],
                'video_url': r['Url_youtube'], 'source_video_title': r['Title'],
                'source_channel': r['Channel'], 'views_historical': int(float(r['Views'])),
                'views_date_declared': '2023-02-07', 'selection_hash': key})
    out = ROOT / 'data/pilot/metadata-candidates.json'
    out.parent.mkdir(parents=True, exist_ok=True)
    payload = {'seed': SEED, 'source_sha256': EXPECTED_SHA,
        'purpose': 'metadata feasibility only; not the study sample',
        'flow': {'input_rows': len(rows), 'exclusions_sequential': dict(excluded),
                 'eligible_rows_by_band': {k:len(v) for k,v in sorted(pool.items())}},
        'candidates': selected}
    assert sum(excluded.values()) + sum(map(len, pool.values())) == len(rows)
    out.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(out.relative_to(ROOT))


if __name__ == '__main__':
    main()
