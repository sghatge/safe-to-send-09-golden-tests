import json
import shutil
import tempfile
import unittest

from golden import check
from qa_rules import verdict

with open("examples/cases.json", encoding="utf-8") as fh:
    CASES = json.load(fh)


class GoldenTest(unittest.TestCase):
    def setUp(self):
        self.dir = tempfile.mkdtemp()
        shutil.copy("golden/qa_rules.json", self.dir)

    def tearDown(self):
        shutil.rmtree(self.dir)

    def test_committed_golden_matches_current_rules(self):
        ok, msg = check("qa_rules", verdict, CASES, "golden")
        self.assertTrue(ok, msg)

    def test_rule_change_is_caught(self):
        ok, diff = check("qa_rules", lambda d: verdict(d, subject_limit=60), CASES, self.dir)
        self.assertFalse(ok)
        self.assertIn("HU-bf-long", diff.replace('"', "") or diff)

    def test_update_accepts_new_behaviour(self):
        fn = lambda d: verdict(d, subject_limit=60)
        check("qa_rules", fn, CASES, self.dir, update=True)
        self.assertTrue(check("qa_rules", fn, CASES, self.dir)[0])


if __name__ == "__main__":
    unittest.main()
