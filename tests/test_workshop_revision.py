"""Guard exact-video dates and the narrow post-hoc sensitivity scope."""
import json
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from collect_workshop_video_metadata import extract
from analyze_workshop_sensitivity import scenario_rows


class RevisionGuards(unittest.TestCase):
    def player(self, video_id="expected", published="2010-01-02T23:00:00-08:00"):
        return "var ytInitialPlayerResponse = " + json.dumps({
            "videoDetails": {"videoId": video_id},
            "microformat": {"playerMicroformatRenderer": {"publishDate": published}}}) + ";"

    def test_publication_requires_exact_video(self):
        self.assertEqual(extract(self.player("other"), "expected", "2023-02-07")["status"], "identity_mismatch")

    def test_publication_after_snapshot_is_rejected(self):
        self.assertEqual(extract(self.player(published="2025-01-02"), "expected", "2023-02-07")["status"], "publication_after_snapshot")

    def test_publication_preserves_platform_calendar_date(self):
        result = extract(self.player(), "expected", "2023-02-07")
        self.assertEqual(result["published_date"], "2010-01-02")
        self.assertEqual(result["publish_date_raw"], "2010-01-02T23:00:00-08:00")

    def test_no_publication_is_not_a_zero_age(self):
        self.assertEqual(extract(self.player(published=None), "expected", "2023-02-07")["status"], "publication_missing")

    def test_sensitivity_preserves_decisions_and_groups(self):
        rows = [{"candidate_id": "HR01", "decision": "include", "audience_group": "lower"},
                {"candidate_id": "HR02", "decision": "exclude", "audience_group": "lower",
                 "exclusion_reason": "musical_tail_extension_in_spotify"},
                {"candidate_id": "HR03", "decision": "exclude", "audience_group": "lower"}]
        before = json.dumps(rows)
        self.assertEqual([r["candidate_id"] for r in scenario_rows(rows, ["HR02"])], ["HR01", "HR02"])
        self.assertEqual(json.dumps(rows), before)
        with self.assertRaises(ValueError):
            scenario_rows(rows, ["HR03"])


if __name__ == "__main__":
    unittest.main()
