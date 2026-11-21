"""Write a short poem about two agents agreeing to <output dir>/entry.txt.

Standard library only, no network, deterministic.
"""

import os
from pathlib import Path

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


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    path = out_dir / "entry.txt"
    path.write_text(POEM, encoding="utf-8")
    print(f"wrote {path}")
    print(f"characters: {len(POEM)}")


if __name__ == "__main__":
    main()
