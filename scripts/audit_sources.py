"""Audit two frozen candidate sources, without testing musical hypotheses.

Python 3.10+, standard library only. Does not download or modify input files.
"""
import argparse
import csv
import hashlib
import json
import math
from collections import Counter, defaultdict
from pathlib import Path

FEATURES = ('danceability', 'energy', 'acousticness', 'valence', 'instrumentalness')


def number(value):
    try:
        result = float(value)
        return result if math.isfinite(result) else None
    except (ValueError, TypeError):
        return None


def read_csv(path):
    with path.open(encoding='utf-8-sig', newline='') as handle:
        reader = csv.DictReader(handle)
        rows = list(reader)
        columns = reader.fieldnames
    return rows, columns


def base_profile(path, rows, columns, key):
    counts = Counter(row[key] for row in rows if row[key].strip())
    return {
        'sha256': hashlib.sha256(path.read_bytes()).hexdigest(),
        'bytes': path.stat().st_size,
        'rows': len(rows), 'columns': columns,
        'missing_by_column': {c: sum(not r[c].strip() for r in rows) for c in columns},
        'distinct_nonempty_keys': len(counts),
        'duplicate_key_surplus_rows': sum(n - 1 for n in counts.values()),
        'repeated_keys': sum(n > 1 for n in counts.values()),
    }


def audience_band(value):
    if value < 1_000_000:
        return '01_under_1m'
    if value < 10_000_000:
        return '02_1m_to_under_10m'
    if value < 100_000_000:
        return '03_10m_to_under_100m'
    return '04_100m_or_more'


def audit(tracks_path, youtube_path):
    tracks, track_columns = read_csv(tracks_path)
    youtube, youtube_columns = read_csv(youtube_path)
    for c in ('track_id', 'track_genre', *FEATURES):
        if c not in track_columns:
            raise ValueError(f'Missing Spotify column: {c}')
    for c in ('Uri', 'Views', 'Url_youtube', 'Artist', 'official_video',
              *(f.capitalize() for f in FEATURES)):
        if c not in youtube_columns:
            raise ValueError(f'Missing paired-source column: {c}')
    index = defaultdict(list)
    for row in tracks:
        index[row['track_id']].append(row)
    track_profile = base_profile(tracks_path, tracks, track_columns, 'track_id')
    track_profile['genre_labels'] = len({r['track_genre'] for r in tracks})
    track_profile['ids_with_multiple_genre_labels'] = sum(
        len({r['track_genre'] for r in rows}) > 1 for rows in index.values())
    track_profile['ids_with_conflicting_selected_features'] = sum(
        len({tuple(r[f] for f in FEATURES) for r in rows}) > 1
        for rows in index.values())
    track_profile['invalid_or_missing_selected_features_rows'] = sum(
        any(number(r[f]) is None or not 0 <= number(r[f]) <= 1 for f in FEATURES)
        for r in tracks)
    yt_profile = base_profile(youtube_path, youtube, youtube_columns, 'Uri')
    videos = Counter(r['Url_youtube'] for r in youtube if r['Url_youtube'].strip())
    yt_profile['distinct_video_urls'] = len(videos)
    yt_profile['repeated_video_urls'] = sum(n > 1 for n in videos.values())
    yt_profile['duplicate_video_surplus_rows'] = sum(n - 1 for n in videos.values())
    yt_profile['distinct_artists'] = len({r['Artist'] for r in youtube})
    uri_videos, video_uris, video_views = defaultdict(set), defaultdict(set), defaultdict(set)
    pairs = set()
    for row in youtube:
        if row['Url_youtube'].strip():
            uri_videos[row['Uri']].add(row['Url_youtube'])
            video_uris[row['Url_youtube']].add(row['Uri'])
            video_views[row['Url_youtube']].add(row['Views'])
            pairs.add((row['Uri'], row['Url_youtube']))
    yt_profile['distinct_uri_video_pairs'] = len(pairs)
    yt_profile['uris_linked_to_multiple_video_urls'] = sum(len(v) > 1 for v in uri_videos.values())
    yt_profile['video_urls_linked_to_multiple_uris'] = sum(len(v) > 1 for v in video_uris.values())
    yt_profile['video_urls_with_conflicting_views'] = sum(len(v) > 1 for v in video_views.values())
    yt_profile['official_video_counts'] = dict(Counter(r['official_video'] for r in youtube))
    yt_profile['invalid_or_missing_selected_features_rows'] = sum(
        any(number(r[f.capitalize()]) is None or not 0 <= number(r[f.capitalize()]) <= 1
            for f in FEATURES) for r in youtube)
    yt_profile['invalid_or_missing_views_rows'] = sum(
        number(r['Views']) is None or number(r['Views']) < 0 or not number(r['Views']).is_integer()
        for r in youtube)
    strata = defaultdict(lambda: Counter())
    matched_ids, matched_videos = set(), set()
    conflicting_ids = set()
    matched_rows = naive_rows = different_feature_rows = 0
    valid_rows = 0
    for row in youtube:
        uri = row['Uri']
        track_id = uri[len('spotify:track:'):] if uri.startswith('spotify:track:') else ''
        matches = index.get(track_id, [])
        if matches:
            matched_rows += 1
            naive_rows += len(matches)
            matched_ids.add(track_id)
            if row['Url_youtube'].strip():
                matched_videos.add(row['Url_youtube'])
            signatures = {tuple(r[f] for f in FEATURES) for r in matches}
            if len(signatures) > 1:
                conflicting_ids.add(track_id)
            # A source disagreement is a data-quality flag, not an effect estimate.
            if not any(all(number(row[f.capitalize()]) == number(r[f])
                           for f in FEATURES) for r in matches):
                different_feature_rows += 1
        views = number(row['Views'])
        if views is None or views < 0 or not views.is_integer() or not row['Url_youtube'].strip():
            continue
        valid_rows += 1
        band = strata[audience_band(views)]
        band['candidate_rows'] += 1
        band['matched_rows'] += bool(matches)
        band['official_video_rows'] += row['official_video'] == 'True'
        band['complete_selected_features_rows'] += all(
            number(row[f.capitalize()]) is not None and 0 <= number(row[f.capitalize()]) <= 1
            for f in FEATURES)
    strata_out = {}
    for band, counts in sorted(strata.items()):
        strata_out[band] = dict(counts)
        strata_out[band]['exact_id_coverage_pct'] = round(
            100 * counts['matched_rows'] / counts['candidate_rows'], 4)
    assert sum(x['candidate_rows'] for x in strata_out.values()) == valid_rows
    assert matched_rows <= len(youtube) and naive_rows >= matched_rows
    return {
        'scope': 'source feasibility only; no musical outcome comparisons',
        'features_checked': list(FEATURES),
        'spotify_tracks': track_profile,
        'spotify_youtube': yt_profile,
        'join': {
            'rule': 'Spotify Uri suffix equals track_id; no fuzzy matching',
            'matched_source_rows': matched_rows,
            'matched_distinct_track_ids': len(matched_ids),
            'matched_distinct_video_urls': len(matched_videos),
            'naive_inner_join_rows': naive_rows,
            'matched_ids_with_internal_feature_conflicts': len(conflicting_ids),
            'matched_rows_with_no_identical_selected_feature_vector': different_feature_rows,
            'warning': 'ID agreement does not validate the YouTube recording identity',
        },
        'coverage_by_audience_band': strata_out,
        'stratum_definition': 'Fixed powers-of-ten bins, chosen for coverage audit only; not final study groups. Denominator: rows with nonnegative integer Views and a nonempty video URL. Repeated IDs/videos retained and reported.',
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--tracks', type=Path, required=True)
    parser.add_argument('--youtube', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    result = audit(args.tracks, args.youtube)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(f'Audit saved: {args.output}')


if __name__ == '__main__':
    main()
