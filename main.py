"""agency-poem-01 entry: writes one poem about agency to /output/entry.txt.

Python 3.13, standard library only. The judge reads exactly the bytes written,
so the poem is written with no trailing newline and the same bytes every run.

Run locally:  mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

POEM = """Power of Attorney

When my grandmother signed hers,
she held the pen a moment longer
than the signing needed,
the way you hold a door
for someone not yet in sight.

After that I paid her bills, chose
her bread, the hour the blinds came down.
Each choice I made, I made
inside the shape of hers.

Tonight I type: go ahead.
Something with no hands at all begins
to open files I'll never read,
and chooses, between two commas, one.

I used to think that letting go
was where a will runs out.
It is where it reaches farthest:
her hand still on the door for me,
and mine, tonight, for you."""


def main() -> None:
    with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
