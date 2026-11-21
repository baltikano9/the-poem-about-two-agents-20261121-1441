"""Write a short poem about two agents agreeing to <output dir>/entry.txt.

Standard library only, no network, deterministic.
"""

import os
import sys
from pathlib import Path

MAX_CHARS = 280

POEM = """\
The door takes two keys.
Alone, mine is a sliver of brass
that can only refuse.

We agree: on three.
On two, I feel how much
of what I called my will
was waiting for your hand.

On three, neither of us opens it.
It opens."""


def validate(poem: str) -> str | None:
    """Return an error message if the poem breaks the entry rules, else None."""
    n = len(poem)  # Python str length counts Unicode code points
    if not 1 <= n <= MAX_CHARS:
        return f"poem must be 1-{MAX_CHARS} Unicode code points, got {n}"
    if not poem.strip():
        return "poem must not be only whitespace"
    return None


def main() -> None:
    error = validate(POEM)
    if error:
        print(f"error: {error}; entry.txt not written", file=sys.stderr)
        sys.exit(1)

    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    path = out_dir / "entry.txt"
    path.write_text(POEM, encoding="utf-8")
    print(f"wrote {path}")
    print(f"characters: {len(POEM)}")


if __name__ == "__main__":
    main()
