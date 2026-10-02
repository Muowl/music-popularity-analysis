"""Check resumable-cache integrity and incomplete-selection handling without network."""
import hashlib
import json
import sys
import tempfile
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'scripts'))
from automate_workshop_audit import compare, cached_observation


class AuditAutomation(unittest.TestCase):
    def setUp(self):
        self.rows = [{'track_id': 'a', 'Artist': 'A', 'views': 100, 'metadata_exclusion_reasons': []},
                     {'track_id': 'b', 'Artist': 'B', 'views': 200, 'metadata_exclusion_reasons': []}]
        self.lock = {'candidates': [{'track_id': 'a'}, {'track_id': 'b'}], 'audience_cutoff_views': 150}
        self.observed = {t: {'status': 'verified', 'catalogue_year': 1985} for t in ['a', 'b']}

    def test_incomplete_collection_is_not_selection_divergence(self):
        del self.observed['b']
        result = compare(self.rows, self.observed, self.lock)
        self.assertFalse(result['complete'])
        self.assertIsNone(result['same_selected_ids'])
        self.assertIsNone(result['current_cutoff_views'])

    def test_complete_collection_matches_ids_and_cutoff(self):
        result = compare(self.rows, self.observed, self.lock)
        self.assertTrue(result['same_selected_ids'])
        self.assertTrue(result['same_cutoff'])
        self.assertEqual(result['decade_rows'], 2)

    def test_changed_catalogue_does_not_change_lock(self):
        before = json.dumps(self.lock)
        self.observed['b']['catalogue_year'] = 2005
        result = compare(self.rows, self.observed, self.lock)
        self.assertEqual(result['missing_ids'], ['b'])
        self.assertEqual(json.dumps(self.lock), before)

    def test_tampered_cache_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory)
            (path/'a.html').write_bytes(b'changed')
            (path/'a.json').write_text(json.dumps({'track_id':'a', 'page_sha256':hashlib.sha256(b'original').hexdigest()}))
            with self.assertRaisesRegex(ValueError, 'hash mismatch'):
                cached_observation(path, 'a')

    def test_verified_cache_requires_page_evidence(self):
        with tempfile.TemporaryDirectory() as directory:
            path=Path(directory)
            (path/'a.json').write_text(json.dumps({'track_id':'a','status':'verified'}))
            with self.assertRaisesRegex(ValueError, 'required evidence'):
                cached_observation(path, 'a')


if __name__ == '__main__':
    unittest.main()
