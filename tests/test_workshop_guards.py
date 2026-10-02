"""Test safeguards against unreviewed inclusions and changes to a frozen roster."""
import csv
import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from analyze_workshop import read_review


class WorkshopGuards(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        target = self.root / "data/workshop"
        target.mkdir(parents=True)
        for name in ["selection-lock.json", "recording-review.csv"]:
            shutil.copyfile(ROOT / "data/workshop" / name, target / name)
        self.path = target / "recording-review.csv"
        with self.path.open(newline="", encoding="utf-8") as f:
            self.rows = list(csv.DictReader(f))

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


if __name__ == "__main__":
    unittest.main()
