"""Resumable current-catalogue check and evidence ZIP; never replace the frozen study."""
import argparse
import hashlib
import json
import statistics
import subprocess
import sys
import time
from datetime import datetime, timezone, date
from pathlib import Path
from urllib.error import HTTPError
from urllib.request import Request, urlopen
from zipfile import ZipFile, ZIP_DEFLATED

from prepare_workshop import inventory, MetaParser, SEED

ROOT = Path(__file__).resolve().parents[1]


def digest(data):
    return hashlib.sha256(data).hexdigest()


def save_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix('.tmp')
    temporary.write_text(json.dumps(value, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    temporary.replace(path)


def cached_observation(cache, track):
    path = cache / (track+'.json')
    if not path.exists():
        return None
    result = json.loads(path.read_text(encoding='utf-8'))
    if result.get('track_id') != track:
        raise ValueError('Cache identity mismatch: '+track)
    if result.get('status') == 'verified' and not (
            result.get('page_sha256') and result.get('identity_verified')
            and result.get('canonical_track_id') == track and result.get('catalogue_year')):
        raise ValueError('Verified cache lacks required evidence: '+track)
    if result.get('page_sha256'):
        html = cache / (track+'.html')
        if not html.exists() or digest(html.read_bytes()) != result['page_sha256']:
            raise ValueError('Cache bytes/hash mismatch: '+track)
    return result


def retrieve(track, cache, attempts, timeout):
    result = {'track_id': track, 'url': 'https://open.spotify.com/track/'+track}
    for attempt in range(attempts):
        result = dict(track_id=track, url=result['url'], retrieved_at_utc=datetime.now(timezone.utc).isoformat())
        try:
            with urlopen(Request(result['url'], headers={'User-Agent': 'Mozilla/5.0'}), timeout=timeout) as response:
                body = response.read()
                result.update(http_status=response.status, resolved_url=response.url)
            (cache / (track+'.html')).write_bytes(body)
            parser = MetaParser()
            parser.feed(body.decode('utf-8', errors='replace'))
            canonical = (parser.facts.get('og:url') or '').rstrip('/').split('/')[-1]
            published = parser.facts.get('music:release_date') or ''
            result.update(page_sha256=digest(body), canonical_track_id=canonical,
                          identity_verified=canonical == track, catalogue_date=published or None,
                          catalogue_year=None, status='unverified_metadata')
            if canonical == track and published:
                parsed = date.fromisoformat(published[:10])
                result.update(catalogue_year=parsed.year, status='verified')
            break
        except (OSError, ValueError) as error:
            result.update(status='request_or_parse_failed', error_type=type(error).__name__)
            if isinstance(error, HTTPError):
                result['http_status'] = error.code
                # Do not retry access-denied responses or try alternate identities.
                if error.code in (401, 403, 404):
                    break
            if attempt+1 < attempts:
                time.sleep(min(2**attempt, 4))
    save_json(cache / (track+'.json'), result)
    return result


def compare(linked, observations, lock):
    complete = all(observations.get(r['track_id'], {}).get('status') == 'verified' for r in linked)
    result = {'complete': complete, 'decade_rows': None, 'selected_artists': None,
              'same_selected_ids': None, 'same_cutoff': None, 'current_cutoff_views': None,
              'new_ids': None, 'missing_ids': None}
    if not complete:
        return result
    eligible = [r for r in linked if not r['metadata_exclusion_reasons']
                and 1980 <= observations[r['track_id']]['catalogue_year'] <= 1989]
    chosen = {}
    for row in sorted(eligible, key=lambda r: (digest((SEED+'|'+r['track_id']).encode()), r['track_id'])):
        chosen.setdefault(row['Artist'], row)
    selected = {r['track_id'] for r in chosen.values()}
    original = {r['track_id'] for r in lock['candidates']}
    cutoff = statistics.median(r['views'] for r in chosen.values()) if chosen else None
    result.update(decade_rows=len(eligible), selected_artists=len(chosen),
                  same_selected_ids=selected == original, same_cutoff=cutoff == lock['audience_cutoff_views'],
                  current_cutoff_views=cutoff, new_ids=sorted(selected-original), missing_ids=sorted(original-selected))
    return result


def package(root, cache, linked, observations, audit, lock, stop_reason):
    stamp = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')
    output = root / 'data/processed/catalogue-automation' / stamp
    output.mkdir(parents=True)
    comparison = compare(linked, observations, lock)
    verified = sum(r.get('status') == 'verified' for r in observations.values())
    report = {'scope': 'Later catalogue verification, not recovery of the original cache or an independent hypothesis test',
              'created_at_utc': datetime.now(timezone.utc).isoformat(), 'stop_reason': stop_reason,
              'intersection': len(linked), 'verified_pages': verified,
              'snapshot_eligible_before_catalogue': sum(not r['metadata_exclusion_reasons'] for r in linked),
              'source_audit': audit, 'selection_lock_sha256': digest((root/'data/workshop/selection-lock.json').read_bytes()),
              'comparison': comparison,
              'records': [{'track_id': r['track_id'], 'artist': r['Artist'],
                           'snapshot_exclusions': r['metadata_exclusion_reasons'],
                           'observation': observations.get(r['track_id'], {'status': 'not_attempted'})} for r in linked]}
    save_json(output/'report.json', report)
    status = 'INCONCLUSIVA: coleta incompleta' if not comparison['complete'] else (
        'SELECAO REPRODUZIDA na coleta posterior' if comparison['same_selected_ids'] and comparison['same_cutoff']
        else 'DIVERGENCIA: revisar antes de qualquer alteracao')
    (output/'RELATORIO.md').write_text(
        '# Verificacao posterior do catalogo\n\n'+status+'\n\n'
        +f'Paginas verificadas: {verified}/{len(linked)}. Encerramento: {stop_reason}.\n\n'
        +'Esta coleta nao recupera o cache original. IDs, decisoes, grupos, descritores e audiencia historica nao foram alterados.\n\n'
        +'Detalhes por ID e comparacao: report.json. O ZIP inclui apenas evidencias desta coleta, protocolo executavel e lock; nao inclui CSVs completos, audios ou credenciais.\n', encoding='utf-8')
    sources = [(output/'report.json', 'report.json'), (output/'RELATORIO.md', 'RELATORIO.md'),
               (root/'data/workshop/selection-lock.json', 'reference/selection-lock.json'),
               (root/'data/source-manifest.json', 'reference/source-manifest.json'),
               (Path(__file__), 'scripts/automate_workshop_audit.py'),
               (root/'scripts/prepare_workshop.py', 'scripts/prepare_workshop.py')]
    for track, observation in observations.items():
        path = cache/(track+'.json')
        if path.exists():
            sources.append((path, 'cache/'+path.name))
        html = cache/(track+'.html')
        if observation.get('page_sha256') and html.exists():
            if digest(html.read_bytes()) != observation['page_sha256']:
                raise ValueError('Cache changed while packaging: '+track)
            sources.append((html, 'cache/'+html.name))
    manifest = [{'path': name, 'bytes': path.stat().st_size, 'sha256': digest(path.read_bytes())} for path, name in sources]
    save_json(output/'manifest.json', {'scope': 'Every ZIP member except this manifest', 'files': manifest})
    archive = output/'catalogue-evidence.zip'
    with ZipFile(archive, 'w', ZIP_DEFLATED) as z:
        for path, name in sources:
            z.write(path, name)
        z.write(output/'manifest.json', 'manifest.json')
    (output/'catalogue-evidence.zip.sha256').write_text(digest(archive.read_bytes())+'  '+archive.name+'\n', encoding='utf-8')
    print(status, flush=True)
    print('ZIP:', archive.resolve(), flush=True)
    print('RELATORIO:', (output/'RELATORIO.md').resolve(), flush=True)
    return 0 if comparison['complete'] and comparison['same_selected_ids'] and comparison['same_cutoff'] else 2


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--offline', action='store_true', help='Package existing cache without network access')
    parser.add_argument('--max-minutes', type=float, default=15, help='Collection budget, excluding initial source download')
    args = parser.parse_args()
    if args.max_minutes <= 0:
        parser.error('--max-minutes must be positive')
    manifest = json.loads((ROOT/'data/source-manifest.json').read_text(encoding='utf-8'))
    if any(not (ROOT/s['local_path']).exists() for s in manifest['sources']):
        if args.offline:
            parser.error('Source CSVs missing; run download_pilot_sources.py first')
        subprocess.run([sys.executable, str(ROOT/'scripts/download_pilot_sources.py')], check=True)
    audit, linked = inventory(ROOT)  # Includes source SHA-256 verification.
    lock_path = ROOT/'data/workshop/selection-lock.json'
    original_lock = lock_path.read_bytes()
    lock = json.loads(original_lock)
    if {s['name']: s['sha256'] for s in audit['sources']} != {s['name']: s['sha256'] for s in lock['audit']['sources']}:
        raise ValueError('Sources differ from the frozen lock')
    cache = ROOT/'data/raw/catalogue-automation'
    cache.mkdir(parents=True, exist_ok=True)
    observations = {}
    for row in linked:
        existing = cached_observation(cache, row['track_id'])
        if existing:
            observations[row['track_id']] = existing
    deadline = time.monotonic()+args.max_minutes*60
    consecutive_failures = 0
    stop_reason = 'offline' if args.offline else 'finished'
    try:
        if not args.offline:
            for index, row in enumerate(linked, 1):
                track = row['track_id']
                if observations.get(track, {}).get('status') == 'verified':
                    print(f'{index}/{len(linked)} {track} cached', flush=True)
                    continue
                if time.monotonic() >= deadline:
                    stop_reason = 'time_budget_reached'
                    break
                result = retrieve(track, cache, attempts=2, timeout=15)
                observations[track] = result
                print(f'{index}/{len(linked)} {track} {result["status"]}', flush=True)
                consecutive_failures = consecutive_failures+1 if result['status'] == 'request_or_parse_failed' else 0
                if consecutive_failures >= 5:
                    stop_reason = 'five_consecutive_access_failures'
                    break
                time.sleep(.4)
    except KeyboardInterrupt:
        stop_reason = 'interrupted_by_user'
    if lock_path.read_bytes() != original_lock:
        raise ValueError('Lock changed during execution; stop and inspect')
    return package(ROOT, cache, linked, observations, audit, lock, stop_reason)


if __name__ == '__main__':
    sys.exit(main())
