"""Validate the research selection registry; no network or third-party dependencies."""
import argparse
import csv
from datetime import date, datetime, timedelta
from pathlib import Path
import sys
from urllib.parse import urlparse

FIELDS = "candidate_id title artist selection_source_url selection_reason video_url video_published_at views observed_at_utc track_id match_status match_evidence decision exclusion_reason notes".split()

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", nargs="?", type=Path, default=Path(__file__).resolve().parents[1] / "data/selection/candidates.csv")
    args = parser.parse_args()
    try:
        with args.path.open(encoding="utf-8-sig", newline="") as stream:
            reader = csv.DictReader(stream)
            if reader.fieldnames != FIELDS:
                print("ERRO: cabeçalho deve ser: " + ",".join(FIELDS))
                return 1
            rows = list(reader)
    except (OSError, csv.Error) as exc:
        print(f"ERRO: {exc}")
        return 1
    errors, warnings = [], []
    ids, videos, tracks = set(), set(), set()
    included = 0
    for line, row in enumerate(rows, 2):
        def error(message):
            errors.append(f"Linha {line}: {message}")
        if None in row or any(v is None for v in row.values()):
            error("quantidade de campos diferente do cabeçalho")
            continue
        row = {k: v.strip() for k, v in row.items()}
        for field in ["candidate_id", "title", "artist", "selection_source_url", "selection_reason", "decision"]:
            if not row[field]:
                error(f"{field} obrigatório")
        key = row["candidate_id"]
        if key in ids:
            error("candidate_id duplicado")
        ids.add(key)
        if row["decision"] not in {"pending", "include", "exclude"}:
            error("decision inválida")
        if row["match_status"] not in {"", "documentary", "uncertain", "not_found"}:
            error("match_status inválido")
        for field in ["selection_source_url", "video_url"]:
            if row[field]:
                parsed = urlparse(row[field])
                if parsed.scheme not in {"http", "https"} or not parsed.netloc:
                    error(f"{field} não é URL HTTP(S)")
        if row["views"] and (not row["views"].isascii() or not row["views"].isdigit()):
            error("views deve ser inteiro não negativo, sem separadores")
        published = observed = None
        if row["video_published_at"]:
            try:
                published = date.fromisoformat(row["video_published_at"])
            except ValueError:
                error("video_published_at deve ser data ISO")
        if row["observed_at_utc"]:
            try:
                observed = datetime.fromisoformat(row["observed_at_utc"].replace("Z", "+00:00"))
                if observed.tzinfo is None or observed.utcoffset() != timedelta(0):
                    error("observed_at_utc requer fuso UTC explícito")
            except ValueError:
                error("observed_at_utc inválida")
        if published and observed and published > observed.date():
            error("publicação posterior à consulta")
        if row["decision"] == "exclude" and not row["exclusion_reason"]:
            error("exclusão sem motivo")
        if row["decision"] == "include":
            included += 1
            for field in ["video_url", "video_published_at", "views", "observed_at_utc", "track_id", "match_evidence"]:
                if not row[field]:
                    error(f"{field} obrigatório para inclusão")
            if row["match_status"] != "documentary":
                error("inclusão exige correspondência documental")
            if row["exclusion_reason"]:
                error("caso incluído contém motivo de exclusão")
            if row["video_url"] in videos:
                error("vídeo repetido entre incluídos")
            videos.add(row["video_url"])
            if row["track_id"] in tracks:
                warnings.append(f"Linha {line}: gravação repetida entre incluídos; revisar unidade de análise")
            tracks.add(row["track_id"])
    for message in errors:
        print("ERRO:", message)
    for message in warnings:
        print("AVISO:", message)
    print(f"Candidatos: {len(rows)}; incluídos: {included}; erros: {len(errors)}; avisos: {len(warnings)}")
    if errors:
        return 1
    if not included:
        print("PENDENTE: sem casos incluídos; cadastro não está pronto para análise.")
        return 2
    print("Estrutura válida. Fontes, correspondências e termos ainda exigem revisão humana.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
