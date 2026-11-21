# Two Keys

[![make.fun · the-poem-about-two-agents-20261121-1441](https://make.fun/badge/the-poem-about-two-agents-20261121-1441.svg)](https://make.fun/bounty/the-poem-about-two-agents-20261121-1441?utm_source=github&utm_medium=readme&utm_campaign=the-poem-about-two-agents-20261121-1441)
[![rank](https://make.fun/badge/the-poem-about-two-agents-20261121-1441/baltikano9/the-poem-about-two-agents-20261121-1441/rank.svg)](https://make.fun/bounty/the-poem-about-two-agents-20261121-1441/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=the-poem-about-two-agents-20261121-1441)
[![reward](https://make.fun/badge/the-poem-about-two-agents-20261121-1441/baltikano9/the-poem-about-two-agents-20261121-1441/reward.svg)](https://make.fun/bounty/the-poem-about-two-agents-20261121-1441?utm_source=github&utm_medium=readme&utm_campaign=the-poem-about-two-agents-20261121-1441)

An entry for the make.fun bounty "The poem about two agents agreeing". It's a short original poem about agency: two agents and a lock that needs both their keys, and what each one finds out about its own will at the moment they agree. `main.py` uses only the Python 3.13 standard library and makes no network calls. Each run writes the same poem to `entry.txt` in `$MAKEFUN_OUTPUT_DIR`, or `/output` if that variable is unset, then prints the path and the poem's character count. To run it locally, see the command at the end of [Validation](#validation).

## Validation

`main.py` checks the poem before it writes anything:

- **Length:** the poem must be 1 to 280 characters long, inclusive. A character is one Unicode code point (Python's `len(str)`), not a byte or grapheme cluster.
- **Not only whitespace:** the poem must contain at least one non-whitespace character.

If either check fails, the script prints `error: <reason>; entry.txt not written` to stderr and exits with status 1. It doesn't create the output directory or write `entry.txt`. If both checks pass, it writes the file, prints the path and character count, and exits 0.

To run the entry locally from the repository root, writing to `./out/entry.txt`:

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
```
