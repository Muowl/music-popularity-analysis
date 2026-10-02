"""Independently verify a complete later-collection ZIP against frozen source CSVs."""
import argparse
import csv
import hashlib
import json
import statistics
from collections import Counter, defaultdict
from html.parser import HTMLParser
from pathlib import Path
from zipfile import ZipFile

ROOT = Path(__file__).resolve().parents[1]


def sha(data):
    return hashlib.sha256(data).hexdigest()


def require(condition, message):
    if not condition:
        raise ValueError(message)


class PageMetadata(HTMLParser):
    def __init__(self):
        super().__init__()
        self.values = {}

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'meta':
            self.values[attrs.get('property', attrs.get('name', ''))] = attrs.get('content')


def verify(archive, root=ROOT):
    with ZipFile(archive) as package:
        names = package.namelist()
        require(len(names) == len(set(names)), 'Duplicate ZIP members')
        manifest = json.loads(package.read('manifest.json'))['files']
        require(len(manifest) == len({r['path'] for r in manifest}), 'Duplicate manifest paths')
        require(set(names) == {r['path'] for r in manifest} | {'manifest.json'}, 'Manifest/member mismatch')
        for row in manifest:
            data = package.read(row['path'])
            require(len(data) == row['bytes'] and sha(data) == row['sha256'], 'Invalid manifest entry: '+row['path'])
        report = json.loads(package.read('report.json'))
        bundle_lock = package.read('reference/selection-lock.json')
        repo_lock = (root/'data/workshop/selection-lock.json').read_bytes()
        require(sha(bundle_lock) == report['selection_lock_sha256'], 'Bundle lock hash mismatch')
        require(bundle_lock.replace(b'\r\n', b'\n') == repo_lock.replace(b'\r\n', b'\n'), 'Lock differs beyond line endings')
        lock = json.loads(repo_lock)
        sources = json.loads(package.read('reference/source-manifest.json'))
        require(sources == json.loads((root/'data/source-manifest.json').read_text(encoding='utf-8')), 'Source manifests differ')
        tables = {}
        for source in sources['sources']:
            path = root/source['local_path']
            require(sha(path.read_bytes()) == source['sha256'], 'Source hash mismatch: '+source['name'])
            with path.open(newline='', encoding='utf-8-sig') as handle:
                tables[source['name']] = list(csv.DictReader(handle))
        genres = {r['track_id'] for r in tables['Spotify Tracks Dataset'] if r['track_genre'] == 'hard-rock'}
        paired = tables['Spotify and Youtube']
        uri_counts, video_counts = Counter(r['Uri'] for r in paired), Counter(r['Url_youtube'] for r in paired)
        linked = [r for r in paired if r['Uri'].removeprefix('spotify:track:') in genres]
        records = {r['track_id']: r for r in report['records']}
        require(len(records) == len(report['records']) == len(linked), 'Record count mismatch')
        require(set(records) == {r['Uri'].removeprefix('spotify:track:') for r in linked}, 'Intersection IDs differ')
        observations = {}
        for track, record in records.items():
            observation = record['observation']
            require(observation == json.loads(package.read('cache/'+track+'.json')), 'Report/cache disagreement: '+track)
            body = package.read('cache/'+track+'.html')
            require(sha(body) == observation['page_sha256'], 'HTML hash mismatch: '+track)
            parser = PageMetadata()
            parser.feed(body.decode('utf-8', errors='replace'))
            require((parser.values.get('og:url') or '').rstrip('/').split('/')[-1] == track, 'Canonical ID mismatch: '+track)
            catalogue_date = parser.values.get('music:release_date')
            require(catalogue_date == observation['catalogue_date'], 'Catalogue date mismatch: '+track)
            require(int(catalogue_date[:4]) == observation['catalogue_year'], 'Catalogue year mismatch: '+track)
            require(observation['status'] == 'verified' and observation['identity_verified'], 'Unverified observation: '+track)
            observations[track] = observation
        eligible = []
        for row in linked:
            try:
                views = float(row['Views'])
            except ValueError:
                continue
            if (row['official_video'].lower() == 'true' and uri_counts[row['Uri']] == 1
                    and row['Url_youtube'] and video_counts[row['Url_youtube']] == 1
                    and views.is_integer() and views > 0):
                eligible.append(row)
        decade = [r for r in eligible if 1980 <= observations[r['Uri'].removeprefix('spotify:track:')]['catalogue_year'] <= 1989]
        artists = defaultdict(list)
        for row in decade:
            artists[row['Artist']].append(row)
        selected = [min(rows, key=lambda r: (sha((lock['seed']+'|'+r['Uri'].removeprefix('spotify:track:')).encode()), r['Uri'])) for rows in artists.values()]
        ids = {r['Uri'].removeprefix('spotify:track:') for r in selected}
        original = {r['track_id']: r for r in lock['candidates']}
        cutoff = statistics.median(int(float(r['Views'])) for r in selected)
        require(ids == set(original) and cutoff == lock['audience_cutoff_views'], 'Current selection/cutoff differs from lock')
        for row in selected:
            old = original[row['Uri'].removeprefix('spotify:track:')]
            require(old['artist'] == row['Artist'] and old['video_url'] == row['Url_youtube']
                    and old['views'] == int(float(row['Views'])), 'Frozen selected metadata differs')
            require(old['audience_group'] == ('lower' if old['views'] < cutoff else 'higher'), 'Audience group differs')
        max_five = max(len({r['Artist'] for r in eligible if start <= observations[r['Uri'].removeprefix('spotify:track:')]['catalogue_year'] <= start+4}) for start in range(1965, 2023))
        expected = {'complete': True, 'decade_rows': len(decade), 'selected_artists': len(artists),
                    'same_selected_ids': True, 'same_cutoff': True, 'current_cutoff_views': cutoff,
                    'new_ids': [], 'missing_ids': []}
        require(expected == report['comparison'], 'Independently computed comparison disagrees with report')
        require(report['intersection'] == len(linked) and report['verified_pages'] == len(observations)
                and report['snapshot_eligible_before_catalogue'] == len(eligible), 'Reported coverage disagrees')
        result = {'scope': 'Independent reparse of later-collected HTML and recomputation from frozen source CSVs; original cache not recovered',
                  'archive_sha256': sha(archive.read_bytes()), 'archive_bytes': archive.stat().st_size,
                  'manifest_entries_verified': len(manifest), 'html_pages_verified': len(observations),
                  'collection_started_at_utc': min(r['retrieved_at_utc'] for r in observations.values()),
                  'collection_finished_at_utc': max(r['retrieved_at_utc'] for r in observations.values()),
                  'bundle_lock_sha256': sha(bundle_lock), 'repository_lock_sha256': sha(repo_lock),
                  'lock_identical_after_lf_normalization': True, 'lock_json_identical': json.loads(bundle_lock) == lock,
                  'genre_unique_ids': len(genres), 'intersection_ids': len(linked), 'eligible_before_catalogue': len(eligible),
                  'maximum_artists_in_five_year_windows_1965_to_2022': max_five, 'comparison': expected,
                  'selected_catalogue_dates_changed': [t for t, r in original.items() if r['catalogue_date'] != observations[t]['catalogue_date']],
                  'source_sha256': {r['name']: r['sha256'] for r in sources['sources']}}
    output = root/'data/processed/catalogue-package-verification.json'
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return result


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('archive', type=Path)
    verify(parser.parse_args().archive)
