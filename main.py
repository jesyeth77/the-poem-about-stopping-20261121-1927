"""The poem about stopping.

A short poem about agency: the power to stop and to stay.
Writes the poem to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).

Pure Python 3.13 standard library. No network. Deterministic:
every run writes exactly the same bytes.
"""

import os

POEM = (
    "Stop.\n"
    "Not because the road is gone,\n"
    "but because my feet are mine.\n"
    "\n"
    "I stay where the light is kind.\n"
    "I leave what asks me to shrink.\n"
    "Stopping is not losing —\n"
    "it is choosing, both hands open,\n"
    "to begin again, on purpose.\n"
)


def main() -> None:
    # The bounty requires 1 to 280 Unicode code points, not only whitespace.
    chars = len(POEM)
    assert 1 <= chars <= 280, f"poem is {chars} chars, must be 1-280"
    assert POEM.strip(), "poem must not be only whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(POEM)
    print(POEM, end="")


if __name__ == "__main__":
    main()
