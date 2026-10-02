"""Post-hoc sensitivity to HR02/HR10 tail-edit exclusions; preserve the main roster."""
import csv
import hashlib
import json
import math
import statistics
from pathlib import Path
from analyze_workshop import read_review
from prepare_workshop import load_sources

ROOT = Path(__file__).resolve().parents[1]
SCENARIOS = {"main": [], "add_HR02": ["HR02"], "add_HR10": ["HR10"], "add_both": ["HR02", "HR10"]}


def scenario_rows(review, additions):
    cases = {r["candidate_id"]: r for r in review}
    for candidate in additions:
        if candidate not in {"HR02", "HR10"}:
            raise ValueError("Only documented tail-edit exclusions belong to this sensitivity")
        row = cases[candidate]
        if row["decision"] != "exclude" or row["exclusion_reason"] != "musical_tail_extension_in_spotify":
            raise ValueError("Tail-edit adjudication changed; review this sensitivity protocol")
    return [r for r in review if r["decision"] == "include" or r["candidate_id"] in additions]


def main():
    lock, review, lock_hash = read_review(ROOT)
    manifest, _, _, _ = load_sources(ROOT)
    source = next(s for s in manifest["sources"] if s["name"] == "Spotify and Youtube")
    ids = {r["track_id"] for r in review}
    with (ROOT / source["local_path"]).open(newline="", encoding="utf-8-sig") as f:
        rows = [r for r in csv.DictReader(f) if r["Uri"].removeprefix("spotify:track:") in ids]
    data = {r["Uri"].removeprefix("spotify:track:"): r for r in rows}
    if len(data) != len(rows) or set(data) != ids:
        raise ValueError("Sensitivity requires one exact source row per frozen track")
    scenarios = {}
    for name, additions in SCENARIOS.items():
        selected = scenario_rows(review, additions)
        groups = {g: [r for r in selected if r["audience_group"] == g] for g in ("lower", "higher")}
        summaries = {}
        for feature in lock["features_prespecified"]:
            medians = {}
            for group, members in groups.items():
                values = [float(data[r["track_id"]][feature]) for r in members]
                if not all(math.isfinite(v) and 0 <= v <= 1 for v in values):
                    raise ValueError("Invalid descriptor in sensitivity scenario")
                medians[group] = statistics.median(values)
            summaries[feature] = dict(medians, difference_higher_minus_lower=medians["higher"]-medians["lower"])
        scenarios[name] = {"added_excluded_candidates": additions,
                           "group_counts": {g: len(v) for g, v in groups.items()}, "medians": summaries}
    result = {"analysis_type": "post_hoc_sensitivity_not_independent_confirmation",
              "scope": "Only HR02/HR10 tail edits; HR03 remains excluded; no change to main decisions, cutoff or groups",
              "selection_lock_sha256": lock_hash,
              "review_csv_sha256": hashlib.sha256((ROOT / "data/workshop/recording-review.csv").read_bytes()).hexdigest(),
              "source_sha256": source["sha256"], "audience_cutoff_views": lock["audience_cutoff_views"],
              "scenarios": scenarios}
    output = ROOT / "data/processed/hard-rock-sensitivity-summary.json"
    output.parent.mkdir(exist_ok=True)
    output.write_text(json.dumps(result, ensure_ascii=False, indent=2)+"\n")
    print(json.dumps(scenarios, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
