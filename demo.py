"""Shows golden tests catching a 'harmless' rule change."""
import json
import shutil
import tempfile

from golden import check
from qa_rules import verdict

with open("examples/cases.json", encoding="utf-8") as fh:
    CASES = json.load(fh)

tmp = tempfile.mkdtemp()
shutil.copy("golden/qa_rules.json", tmp)

print("1. Rules unchanged")
print("  ", check("qa_rules", verdict, CASES, tmp)[1])

print("\n2. Someone 'just relaxes' the subject limit to 60 and the window to 22:00")
ok, diff = check("qa_rules", lambda d: verdict(d, subject_limit=60, window=("08:00", "22:00")), CASES, tmp)
print("   PASS" if ok else "   FAIL: verdicts changed\n")
print(diff)
shutil.rmtree(tmp)
