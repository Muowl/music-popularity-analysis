"""Download candidate-source snapshots and verify hashes; standard library only."""
import hashlib
import io
import json
from pathlib import Path
from urllib.request import urlopen
from zipfile import ZipFile


def main():
    root = Path(__file__).resolve().parents[1]
    manifest = json.loads((root / 'data/source-manifest.json').read_text(encoding='utf-8'))
    for source in manifest['sources']:
        target = root / source['local_path']
        if target.exists():
            if hashlib.sha256(target.read_bytes()).hexdigest() == source['sha256']:
                print(f'Already verified: {source["local_path"]}')
                continue
            raise ValueError(f'Existing file has unexpected hash: {target}; inspect before replacing')
        with urlopen(source['download_url'], timeout=60) as response:
            data = response.read()
        if source.get('archive_member'):
            with ZipFile(io.BytesIO(data)) as archive:
                data = archive.read(source['archive_member'])
        if hashlib.sha256(data).hexdigest() != source['sha256']:
            raise ValueError(f'Source changed or download invalid: {source["name"]}; no file saved')
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(data)
        print(f'Downloaded and verified: {source["local_path"]}')


if __name__ == '__main__':
    main()
