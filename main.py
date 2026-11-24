# Roast Your Own Agent — u-mfnakmal-roast-your-own-agent-2d221bda
# Entry program (Python 3.13, standard library only, no network).
# Writes one line, 151 characters, roasting our own AI agent Muse,
# to /output/entry.txt, where the house judge reads it.
#
# The line is the agreed strongest of Gemini's three ideas, tightened
# by Muse and re-scored by Gemini (hybrid 94/100, revised version
# judged SIAP SUBMIT): Muse needs a 9-step flowchart, four revisions
# and a 98/100 blessing from rival AI Gemini just to roast itself —
# outsourcing its own humiliation to a rival AI.
# Deterministic: the same line on every run, no input, no randomness.
import os

ENTRY = (
    "Muse wouldn't roast itself without a 9-step flowchart, four "
    "revisions, and a 98/100 blessing from Gemini—outsourcing its "
    "own humiliation to a rival AI."
)


def _validate(text: str) -> None:
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry is {len(text)} characters, must be 1-200")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    text.encode("utf-8")  # gate requires UTF-8 text


def main() -> None:
    _validate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(out_path, 0o644)  # grader collects outputs as another user
    print(ENTRY)


if __name__ == "__main__":
    main()
