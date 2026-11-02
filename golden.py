"""Golden tests: freeze what your rules decide today, so any change tomorrow is visible.

Before a model joins a rules-based workflow, record every verdict for a fixed set of cases.
After any change (a rule tweak, a model added, a library upgrade), rerun and diff.
A changed verdict is never silent: it needs `--update` and a reason. Standard library only.
"""
import difflib
import json
import os


def render(results):
    return json.dumps(results, indent=2, sort_keys=True, ensure_ascii=False) + "\n"


def check(name, fn, cases, golden_dir="golden", update=False):
    """Return (ok, diff_text). Writes the golden file when update=True or it doesn't exist."""
    results = {c["id"]: fn(c) for c in cases}
    path = os.path.join(golden_dir, f"{name}.json")
    current = render(results)
    if update or not os.path.exists(path):
        os.makedirs(golden_dir, exist_ok=True)
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(current)
        return True, f"golden file written: {path}"
    with open(path, encoding="utf-8") as fh:
        expected = fh.read()
    if expected == current:
        return True, f"{name}: {len(results)} cases match golden"
    diff = difflib.unified_diff(expected.splitlines(), current.splitlines(),
                                f"{path} (approved)", f"{name} (now)", lineterm="", n=1)
    return False, "\n".join(diff)
