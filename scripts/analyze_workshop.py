"""Audit the frozen workshop roster and plot validated recordings or a labeled preview."""
import argparse
import csv
import hashlib
import json
import math
import statistics
import sys
from collections import Counter
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(Path(__file__).resolve().parent))
from prepare_workshop import load_sources

MUTABLE = {"video_published_at", "video_format", "recording_review", "reviewer",
           "review_evidence", "decision", "exclusion_reason"}
REVIEW_STATES = {"pending", "same_base_recording", "different_version", "audio_overlay", "uncertain"}
FORMATS = {"pending", "music_video", "official_audio", "other", "unknown"}
LABELS = {"Energy": "Energia", "Danceability": "Dançabilidade", "Acousticness": "Acusticidade"}


def read_review(root=ROOT):
    lock_path = root / "data/workshop/selection-lock.json"
    lock = json.loads(lock_path.read_text())
    with (root / "data/workshop/recording-review.csv").open(newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        expected = list(lock["candidates"][0])
        if reader.fieldnames != expected:
            raise ValueError("Review CSV schema differs from the frozen roster")
        rows = list(reader)
    if len(rows) != len(lock["candidates"]):
        raise ValueError("Review rows were added or removed")
    frozen = {r["candidate_id"]: r for r in lock["candidates"]}
    if len({r["candidate_id"] for r in rows}) != len(rows):
        raise ValueError("Duplicate candidate ID")
    for r in rows:
        original = frozen.get(r["candidate_id"])
        if original is None or any(str(original[k]) != r[k] for k in original if k not in MUTABLE):
            raise ValueError(f"Frozen fields changed: {r['candidate_id']}")
        if r["decision"] not in {"pending", "include", "exclude"}:
            raise ValueError(f"Invalid decision: {r['candidate_id']}")
        if r["recording_review"] not in REVIEW_STATES or r["video_format"] not in FORMATS:
            raise ValueError(f"Invalid review state or video format: {r['candidate_id']}")
        if r["video_published_at"]:
            published = date.fromisoformat(r["video_published_at"])
            if published > date.fromisoformat(r["views_observed_date"]):
                raise ValueError(f"Publication after snapshot: {r['candidate_id']}")
        if r["decision"] != "pending" and not all(r[k].strip() for k in ["reviewer", "review_evidence"]):
            raise ValueError(f"Decision without attributed evidence: {r['candidate_id']}")
        if r["decision"] != "pending" and r["recording_review"] == "pending":
            raise ValueError(f"Final decision with pending review: {r['candidate_id']}")
        if r["decision"] == "include":
            if r["recording_review"] != "same_base_recording" or r["exclusion_reason"]:
                raise ValueError(f"Ineligible inclusion: {r['candidate_id']}")
            if r["video_format"] == "pending":
                raise ValueError(f"Included format must be recorded or explicitly unknown: {r['candidate_id']}")
        if r["decision"] == "exclude" and not r["exclusion_reason"].strip():
            raise ValueError(f"Exclusion without reason: {r['candidate_id']}")
    return lock, rows, hashlib.sha256(lock_path.read_bytes()).hexdigest()


def export_registry(root=ROOT):
    from validate_selection import FIELDS_V2
    lock, rows, _ = read_review(root)
    records = []
    for r in rows:
        notes = "Catalogue date is not validated first release; publisher official flag; historical day declared."
        if not r["video_published_at"]:
            notes += " Video publication missing: exposure age unavailable."
        records.append(dict(
            candidate_id=r["candidate_id"], title=r["title"], artist=r["artist"],
            selection_source_url=r["views_date_source_url"],
            selection_reason=f"hard-rock exact-ID intersection; catalogue 1980–1989; one hash-selected track per artist; {r['audience_group']}",
            video_url=r["video_url"], video_published_at=r["video_published_at"], views=r["views"],
            observed_at_utc="", track_id=r["track_id"],
            match_status="user_reviewed" if r["recording_review"] == "same_base_recording" else "uncertain",
            match_evidence=r["review_evidence"], decision=r["decision"], exclusion_reason=r["exclusion_reason"], notes=notes,
            views_observed_date=r["views_observed_date"], views_date_precision=r["views_date_precision"],
            views_date_source_url=r["views_date_source_url"], recording_review=r["recording_review"],
            reviewer=r["reviewer"], audience_group=r["audience_group"],
        ))
    with (root / "data/selection/candidates.csv").open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS_V2, lineterminator="\n")
        writer.writeheader()
        writer.writerows(records)
    print(f"Exported {len(records)} candidates; included {sum(r['decision'] == 'include' for r in rows)}")


def analyze(root=ROOT, preview=False):
    lock, review, lock_hash = read_review(root)
    manifest, _, _, _ = load_sources(root)
    rows = review if preview else [r for r in review if r["decision"] == "include"]
    if not preview and any(r["decision"] == "pending" for r in review):
        print("PENDENTE: complete a revisão dos 20 candidatos antes da análise principal.")
        return 2
    source = next(s for s in manifest["sources"] if s["name"] == "Spotify and Youtube")
    ids = {r["track_id"] for r in rows}
    with (root / source["local_path"]).open(newline="", encoding="utf-8-sig") as f:
        data = {r["Uri"].removeprefix("spotify:track:"): r for r in csv.DictReader(f)
                if r["Uri"].removeprefix("spotify:track:") in ids}
    included, losses = [], []
    for r in rows:
        values = {}
        try:
            for feature in lock["features_prespecified"]:
                values[feature] = float(data[r["track_id"]][feature])
                if not math.isfinite(values[feature]) or not 0 <= values[feature] <= 1:
                    raise ValueError()
        except (ValueError, KeyError):
            losses.append({"candidate_id": r["candidate_id"], "audience_group": r["audience_group"],
                           "reason": "missing_or_invalid_prespecified_feature"})
            continue
        included.append(dict(r, **values))
    counts = Counter(r["audience_group"] for r in included)
    if not preview and any(counts[g] < 5 for g in ["lower", "higher"]):
        print("INVIÁVEL: menos de cinco gravações incluídas em pelo menos um grupo.")
        return 2
    import numpy as np
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    features = lock["features_prespecified"]
    summaries = {}
    for feature in features:
        summaries[feature] = {}
        for g in ["lower", "higher"]:
            values = [r[feature] for r in included if r["audience_group"] == g]
            if not values:
                raise ValueError(f"Empty group: {g}")
            q1, median, q3 = np.quantile(values, [.25, .5, .75], method="linear")
            summaries[feature][g] = {"n": len(values), "q1": float(q1), "median": float(median), "q3": float(q3),
                                      "min": min(values), "max": max(values)}
    stage = "candidates-preview" if preview else "validated"
    plot_dir = root / "figures"
    plot_dir.mkdir(exist_ok=True)
    figure, axes = plt.subplots(1, 3, figsize=(7.2, 2.95), sharey=True)
    colors = ["#0072B2", "#D55E00"]
    for ax, feature in zip(axes, features):
        for x, (g, color, marker) in enumerate(zip(["lower", "higher"], colors, ["o", "^"]), 1):
            subset = sorted((r for r in included if r["audience_group"] == g), key=lambda r: r["track_id"])
            jitter = [((int(hashlib.sha256(r["track_id"].encode()).hexdigest()[:8], 16) / (2**32 - 1)) - .5) * .32 for r in subset]
            ax.scatter([x + j for j in jitter], [r[feature] for r in subset], color=color, marker=marker, s=22, alpha=.8, zorder=3)
            summary = summaries[feature][g]
            ax.vlines(x, summary["q1"], summary["q3"], color="black", linewidth=2.2, zorder=4)
            ax.hlines(summary["median"], x-.16, x+.16, color="black", linewidth=2.2, zorder=4)
        ax.set_title(LABELS[feature], fontsize=10)
        ax.set_xticks([1, 2], [f"Menor\nn={counts['lower']}", f"Maior\nn={counts['higher']}"])
        ax.tick_params(labelsize=8)
        ax.set_ylim(-.03, 1.03)
        ax.set_xlim(.6, 2.4)
        ax.grid(axis="y", alpha=.2)
        ax.spines[["top", "right"]].set_visible(False)
    axes[0].set_ylabel("Descritor Spotify (0–1)", fontsize=9)
    figure.suptitle("CANDIDATOS NÃO VALIDADOS — PRÉVIA TÉCNICA" if preview else "Gravações revisadas por nível de audiência", fontsize=10, weight="bold")
    figure.text(.5, .01, "Traço horizontal: mediana; traço vertical: intervalo interquartil. Audiência histórica do vídeo.", ha="center", fontsize=8)
    figure.tight_layout(rect=(0, .06, 1, 1))
    for suffix in ["pdf", "png"]:
        figure.savefig(plot_dir / f"hard-rock-{stage}.{suffix}", dpi=180, bbox_inches="tight")
    plt.close(figure)
    context = {}
    for g in ["lower", "higher"]:
        subset = [r for r in included if r["audience_group"] == g]
        years = [int(r["catalogue_year"]) for r in subset]
        ages = [(date.fromisoformat(r["views_observed_date"]) - date.fromisoformat(r["video_published_at"])).days / 365.25
                for r in subset if r["video_published_at"]]
        context[g] = {"n": len(subset), "distinct_artists": len({r["artist"] for r in subset}),
                      "catalogue_year_min": min(years), "catalogue_year_median": statistics.median(years),
                      "catalogue_year_max": max(years), "video_publication_available": len(ages),
                      "video_age_years_median": statistics.median(ages) if ages else None,
                      "formats": dict(Counter(r["video_format"] for r in subset))}
    result = {"stage": stage, "not_a_main_result": preview, "selection_lock_sha256": lock_hash,
              "review_csv_sha256": hashlib.sha256((root / "data/workshop/recording-review.csv").read_bytes()).hexdigest(),
              "source_sha256": source["sha256"], "features": features, "quantile_method": "numpy linear",
              "software": {"python": sys.version.split()[0], "numpy": np.__version__, "matplotlib": matplotlib.__version__},
              "flow": {"candidates": len(review), "decisions": dict(Counter(r["decision"] for r in review)),
                       "review_exclusions": [{"candidate_id": r["candidate_id"], "reason": r["exclusion_reason"]} for r in review if r["decision"] == "exclude"],
                       "feature_exclusions": losses, "plotted": len(included), "group_counts": dict(counts)},
              "context": context, "summaries": summaries}
    output = root / f"data/processed/hard-rock-{stage}-summary.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"stage": stage, "flow": result["flow"], "summaries": summaries}, ensure_ascii=False, indent=2))
    return 0


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--root", type=Path, default=ROOT)
    p.add_argument("--preview", action="store_true", help="Plot all candidates; explicitly unvalidated and excluded from the article")
    p.add_argument("--export-registry", action="store_true", help="Update the selection registry from attributed review decisions")
    args = p.parse_args()
    if args.export_registry:
        export_registry(args.root)
        return 0
    return analyze(args.root, preview=args.preview)


if __name__ == "__main__":
    sys.exit(main())
