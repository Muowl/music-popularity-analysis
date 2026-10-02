"""Validate the research selection registry; no network or third-party dependencies."""
import argparse
import csv
from datetime import date, datetime, timedelta
from pathlib import Path
import sys
from urllib.parse import urlparse

FIELDS = "candidate_id title artist selection_source_url selection_reason video_url video_published_at views observed_at_utc track_id match_status match_evidence decision exclusion_reason notes".split()
FIELDS_V2 = FIELDS + "views_observed_date views_date_precision views_date_source_url recording_review reviewer audience_group".split()

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", nargs="?", type=Path, default=Path(__file__).resolve().parents[1] / "data/selection/candidates.csv")
    args = parser.parse_args()
    try:
        with args.path.open(encoding="utf-8-sig", newline="") as stream:
            reader = csv.DictReader(stream)
            extended = reader.fieldnames == FIELDS_V2
            if reader.fieldnames not in (FIELDS, FIELDS_V2):
                print("ERRO: cabeçalho deve corresponder ao esquema legado ou v2 de data histórica")
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
        allowed_match = {"", "documentary", "uncertain", "not_found"}
        if extended:
            allowed_match.add("user_reviewed")
        if row["match_status"] not in allowed_match:
            error("match_status inválido")
        for field in ["selection_source_url", "video_url"] + (["views_date_source_url"] if extended else []):
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
        declared = None
        if extended:
            if row["audience_group"] not in {"lower", "higher"}:
                error("audience_group inválido")
            if row["recording_review"] not in {"pending", "same_base_recording", "different_version", "audio_overlay", "uncertain"}:
                error("recording_review inválido")
            if row["views_observed_date"]:
                try:
                    declared = date.fromisoformat(row["views_observed_date"])
                except ValueError:
                    error("views_observed_date deve ser data ISO")
            if declared:
                if row["views_date_precision"] != "day_declared" or not row["views_date_source_url"]:
                    error("data declarada requer precisão day_declared e fonte")
                if row["observed_at_utc"]:
                    error("não combinar instante fabricado com dia declarado")
                if published and published > declared:
                    error("publicação posterior ao snapshot declarado")
            elif row["views_date_precision"] or row["views_date_source_url"]:
                error("precisão/fonte de dia declarado sem data")
        if row["decision"] == "exclude" and not row["exclusion_reason"]:
            error("exclusão sem motivo")
        if row["decision"] == "include":
            included += 1
            required = ["video_url", "views", "track_id", "match_evidence"]
            if not extended:
                required += ["video_published_at", "observed_at_utc"]
            for field in required:
                if not row[field]:
                    error(f"{field} obrigatório para inclusão")
            if extended:
                if not observed and not declared:
                    error("inclusão requer instante UTC ou dia declarado documentado")
                if row["recording_review"] != "same_base_recording" or not row["reviewer"]:
                    error("inclusão v2 exige mesma gravação-base e revisor")
                if row["match_status"] not in {"documentary", "user_reviewed"}:
                    error("inclusão v2 exige evidência documental ou revisão atribuída")
                if not published:
                    warnings.append(f"Linha {line}: publicação do vídeo ausente; idade/exposição indisponível")
                    if not row["notes"]:
                        error("publicação ausente exige limitação em notes")
            elif row["match_status"] != "documentary":
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
