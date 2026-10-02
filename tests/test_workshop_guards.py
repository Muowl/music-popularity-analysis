"""Test safeguards against unreviewed inclusions and changes to a frozen roster."""
import csv
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from analyze_workshop import read_review
from validate_selection import FIELDS_V2


class WorkshopGuards(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        target = self.root / "data/workshop"
        target.mkdir(parents=True)
        for name in ["selection-lock.json", "recording-review.csv"]:
            shutil.copyfile(ROOT / "data/workshop" / name, target / name)
        self.path = target / "recording-review.csv"
        # Fixtures start from the frozen pending state, independently of real reviews.
        lock = json.loads((target / "selection-lock.json").read_text())
        self.rows = [{k: str(v) for k, v in r.items()} for r in lock["candidates"]]
        self.write()

    def tearDown(self):
        self.temp.cleanup()

    def write(self):
        with self.path.open("w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=list(self.rows[0]))
            w.writeheader()
            w.writerows(self.rows)

    def test_pending_roster_is_structurally_valid(self):
        lock, rows, digest = read_review(self.root)
        self.assertEqual(len(rows), 20)
        self.assertEqual(lock["groups"], {"lower": 10, "higher": 10})
        self.assertEqual(len(digest), 64)

    def test_frozen_id_and_group_cannot_change(self):
        for field, value in [("track_id", "another-recording"), ("audience_group", "higher")]:
            with self.subTest(field=field):
                saved = self.rows[0][field]
                self.rows[0][field] = value
                self.write()
                with self.assertRaisesRegex(ValueError, "Frozen fields"):
                    read_review(self.root)
                self.rows[0][field] = saved

    def test_inclusion_requires_attributed_listening_evidence(self):
        self.rows[0].update(decision="include", recording_review="same_base_recording", video_format="unknown")
        self.write()
        with self.assertRaisesRegex(ValueError, "attributed evidence"):
            read_review(self.root)

    def test_overlay_cannot_be_included(self):
        self.rows[0].update(decision="include", recording_review="audio_overlay", reviewer="test fixture",
                            review_evidence="Synthetic overlay for guard test", video_format="music_video")
        self.write()
        with self.assertRaisesRegex(ValueError, "Ineligible inclusion"):
            read_review(self.root)

    def test_publication_cannot_postdate_historical_snapshot(self):
        self.rows[0]["video_published_at"] = "2026-10-02"
        self.write()
        with self.assertRaisesRegex(ValueError, "after snapshot"):
            read_review(self.root)

    def test_exclusion_requires_reason_and_review(self):
        self.rows[0].update(decision="exclude", recording_review="different_version", reviewer="test fixture",
                            review_evidence="Synthetic different performance for guard test")
        self.write()
        with self.assertRaisesRegex(ValueError, "without reason"):
            read_review(self.root)

    def registry_fixture(self, instant=""):
        row = {key: "" for key in FIELDS_V2}
        row.update(candidate_id="TEST", title="Synthetic guard fixture", artist="Test artist",
                   selection_source_url="https://example.org/source", selection_reason="Synthetic validation fixture",
                   video_url="https://example.org/video", views="100", observed_at_utc=instant,
                   track_id="synthetic-track", match_status="user_reviewed", match_evidence="Synthetic listening evidence",
                   decision="include", notes="Video publication missing; age unavailable in synthetic fixture.",
                   views_observed_date="2023-02-07", views_date_precision="day_declared",
                   views_date_source_url="https://example.org/source", recording_review="same_base_recording",
                   reviewer="test fixture", audience_group="lower")
        path = self.root / "registry.csv"
        with path.open("w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=FIELDS_V2, lineterminator="\n")
            writer.writeheader()
            writer.writerow(row)
        return subprocess.run([sys.executable, str(ROOT / "scripts/validate_selection.py"), str(path)],
                              capture_output=True, text=True)

    def test_historical_day_can_be_included_without_fabricated_utc(self):
        result = self.registry_fixture()
        self.assertEqual(result.returncode, 0, result.stdout)
        self.assertIn("idade/exposição indisponível", result.stdout)

    def test_declared_day_rejects_an_added_midnight_timestamp(self):
        result = self.registry_fixture("2023-02-07T00:00:00+00:00")
        self.assertEqual(result.returncode, 1, result.stdout)
        self.assertIn("não combinar instante fabricado", result.stdout)


if __name__ == "__main__":
    unittest.main()
