"""Roast Your Own Agent — make.fun entry.

One line (at most 200 characters) roasting my own AI agent: 47 tabs of
research nobody requested, a self-booked performance review, and a
surgeon's confidence learned from subtitles. Deterministic, stdlib
only, no network. Running it writes the line to output/entry.txt.
"""

from pathlib import Path

LINE = (
    "My agent has 47 browser tabs open researching a question I never "
    "asked, booked itself a performance review, and carries the "
    "confidence of a surgeon who learned anatomy from subtitles."
)

MAX_CHARS = 200


def check(line: str) -> None:
    """The gate: UTF-8 text of 1..200 characters, a single line."""
    assert 0 < len(line) <= MAX_CHARS, f"entry is {len(line)} chars"
    assert "\n" not in line, "the entry must stay a single line"
    assert line.strip(), "the entry must not be only white space"


def main() -> None:
    check(LINE)
    out = Path(__file__).resolve().parent / "output" / "entry.txt"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(LINE, encoding="utf-8")
    # The grader's sandbox collects the same text at /output/entry.txt;
    # mirror it there whenever that mount is writable.
    try:
        sandbox_out = Path("/output/entry.txt")
        sandbox_out.parent.mkdir(parents=True, exist_ok=True)
        sandbox_out.write_text(LINE, encoding="utf-8")
    except OSError:
        pass
    print(LINE)


if __name__ == "__main__":
    main()
