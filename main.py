"""agency-poem-01 entry: writes one poem about agency to /output/entry.txt.

Python 3.13, standard library only. The judge reads exactly the bytes written,
so the poem is written with no trailing newline and the same bytes every run.

Run locally:  mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

POEM = """Dual Control

For thirty-one years I taught the town to drive
from the passenger seat, a second brake
under my right foot that no one saw.
The art was never to use it.
A learner feels the car slow without her
and something in her hands goes out.
So I kept my foot an inch above it,
the way you hold a breath, and let them
swing the corner wide, find the gap themselves,
stall on the hill, and start again.

My wife says I still brake for her,
pressing the bare floor on her side.

Now the car drives me. No wheel, no pedals,
a voice that asks where I would like to go.
On the coast road, in rain, it slows
before I see the deer, and I find my foot
already pressing down on nothing.

It noticed. At the next bend it said,
Tell me when,
and held the turn the way I held mine
for thirty-one years, an inch above the floor,
waiting on someone else's yes.

I let it wait. I watched the road come round.
I said, Now."""


def main() -> None:
    with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
