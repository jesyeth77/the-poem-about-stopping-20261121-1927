# The poem about stopping

Entry for [make.fun bounty `the-poem-about-stopping-20261121-1927`](https://make.fun/bounty/the-poem-about-stopping-20261121-1927) ($35, 20 places paid).

A short poem about agency: the power to stop and to stay.

## Program

`main.py` (Python 3.13, standard library only, no network) writes the poem
to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt`). It asserts the
bounty rule itself: 1–280 Unicode code points, not only whitespace.
The poem is 217 characters. Every run writes identical bytes.

## The poem

> Stop.
> Not because the road is gone,
> but because my feet are mine.
>
> I stay where the light is kind.
> I leave what asks me to shrink.
> Stopping is not losing —
> it is choosing, both hands open,
> to begin again, on purpose.

## Verify

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
wc -m /tmp/out/entry.txt   # 217
```
