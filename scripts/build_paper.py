"""Compile the one-page workshop PDF without modifying the supplied style."""
import argparse
import hashlib
import os
import re
import subprocess
import zipfile
from pathlib import Path
from urllib.request import urlopen

ROOT = Path(__file__).resolve().parents[1]
ABNTEX_URL = "https://mirrors.ctan.org/macros/latex/contrib/abntex2.zip"
ABNTEX_SHA256 = "2e4931c7336456083e10748bfb9b5cba855f81899ec84ea92d35a9aa04fc7f85"


def compile_paper(root=ROOT):
    env = os.environ.copy()
    local = root / "data/raw/latex-deps"
    archive = local / "abntex2.zip"
    probe = subprocess.run(["kpsewhich", "abntex2abrev.sty"], capture_output=True)
    if probe.returncode != 0 or archive.exists():
        local.mkdir(parents=True, exist_ok=True)
        if not archive.exists():
            with urlopen(ABNTEX_URL, timeout=30) as response:
                archive.write_bytes(response.read())
        if hashlib.sha256(archive.read_bytes()).hexdigest() != ABNTEX_SHA256:
            raise ValueError("ABNTeX2 archive changed; review the dependency before compiling")
        with zipfile.ZipFile(archive) as package:
            for name in package.namelist():
                if name.endswith((".sty", ".bst", ".bib", ".txt")):
                    target = (local / name).resolve()
                    if not target.is_relative_to(local.resolve()):
                        raise ValueError("Unsafe dependency archive path")
                    target.parent.mkdir(parents=True, exist_ok=True)
                    target.write_bytes(package.read(name))
        for variable in ["TEXINPUTS", "BSTINPUTS", "BIBINPUTS"]:
            env[variable] = str(local.resolve()) + "//:" + env.get(variable, "")
    result = subprocess.run(["latexmk", "-g", "-pdf", "-interaction=nonstopmode", "-halt-on-error", "main.tex"],
                            cwd=root, env=env, capture_output=True, text=True)
    if result.returncode:
        print(result.stdout[-5000:] + result.stderr[-1000:])
        return result.returncode
    log = (root / "main.log").read_text(errors="replace")
    if "undefined references" in log or re.search(r"Citation .*undefined", log):
        raise ValueError("PDF has unresolved references or citations")
    info = subprocess.run(["pdfinfo", "main.pdf"], cwd=root, capture_output=True, text=True, check=True).stdout
    pages = int(re.search(r"Pages:\s+(\d+)", info).group(1))
    if pages != 1:
        raise ValueError(f"Workshop requires one page; generated {pages}. Shorten the text, preserve settings.sty.")
    print("main.pdf: 1 page; bibliography resolved; supplied settings.sty preserved.")
    return 0


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    args = parser.parse_args()
    raise SystemExit(compile_paper(args.root))


if __name__ == "__main__":
    main()
