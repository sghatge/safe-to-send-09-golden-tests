"""The rules under test: a tiny subject-line and send-window checker."""

SUBJECT_LIMIT = 50
WINDOW = ("08:00", "21:00")


def verdict(delivery, subject_limit=None, window=None):
    limit = subject_limit or SUBJECT_LIMIT
    start, end = window or WINDOW
    issues = []
    if len(delivery["subject"]) > limit:
        issues.append(f"subject over {limit}")
    if not start <= delivery["send_time"] <= end:
        issues.append("outside send window")
    return {"verdict": "fail" if issues else "pass", "issues": issues}
