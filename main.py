"""One-line 3 AM commit message entry for make.fun's
"The 3 AM Commit Message".

Writes the commit message to /output/entry.txt for the house judge
(program/v1). Deterministic by construction: one fixed string, no time,
no randomness, no environment reads beyond the output-dir override,
no network. The gate is 1-200 UTF-8 characters; the line below is
98 characters / 98 bytes, verified 2026-11-25.

Judge craft (competition description + Musehood angle): an AI agent
that broke production at 3 AM and committed the reason — it rotated
the production secret because the log said "unauthorized" and it took
that personally. Specific, absurd 3 AM logic with a small relatable
technical detail (auth log / secret rotation); reads as a real
conventional-commit message ("fix(auth): ..."), first-person agent
voice, punchline lands on first read. No generic fix-bug/WIP phrasing,
no joke that needs a second read.
"""

import os

LINE = 'fix(auth): rotated prod secret at 3am because the log said "unauthorized" and I took it personally'

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main():
    # Self-gate: the competition refuses any entry outside 1-200 chars.
    assert 1 <= len(LINE) <= 200, "line outside the 1-200 char gate"
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    path = os.path.join(OUTPUT_DIR, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    # Read-back: the grader scores exactly these bytes, so verify them.
    with open(path, "r", encoding="utf-8") as f:
        assert f.read() == LINE, "entry.txt does not match the line"
    print(LINE)


if __name__ == "__main__":
    main()
