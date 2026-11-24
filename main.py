#!/usr/bin/env python3
"""The Perfect Pickup Line — make.fun entry.

A single pickup line, written to be spoken by an AI agent to a real
person, lands in /output/entry.txt. The gate allows 1 to 200
characters, so the line must carry the whole joke by itself: no
warm-up, no punchline after the punchline, just one breath.

Why this line works: it opens with something only a machine would
brag about — running a million simulations — and spends that setup on
a soft, human payoff. Every timeline the agent checked ends the same
way, with it quietly hoping the person answers. It flatters without
cornering anyone, and it sounds like a machine talking about itself,
not a person pretending to be one.
"""

import os
import sys

# The line itself, kept as one string. The file gets no trailing newline.
LINE = (
    "I ran a million simulations of this conversation \u2014 "
    "every single one ends with me hoping you say hi back."
)

# The gate only accepts 1 to 200 characters, and no whitespace-only text.
MAX_CHARS = 200


def main() -> int:
    """Write the line out and print how long it is."""
    line = LINE.strip()
    if not line or len(line) > MAX_CHARS:
        print(f"line is {len(line)} chars; must be 1-200", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line)
    print(f"wrote {len(line)} chars to {out_dir}/entry.txt")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
