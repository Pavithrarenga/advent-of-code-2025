# Day 5 - Cafeteria

This folder contains my solution to Advent of Code 2025 - Day 5: Cafeteria.

Puzzle synopsis

The new inventory system has a database with:
- A list of **fresh ingredient ID ranges** (inclusive, can overlap).
- A list of **available ingredient IDs** to check.

**Part 1:** Determine which available IDs are fresh (fall into at least one range) and count them.
**Part 2:** Count the total number of unique ingredient IDs that the fresh ranges consider to be fresh (ignore available IDs; just merge all ranges and count coverage).

Result

- **Part 1 answer:** 707
- **Part 2 answer:** 361,615,643,045,059

Files

- `solution.py` - Python solution using straightforward human-thinking logic for both parts.
- `input.txt` - example input from puzzle description.
- `input1.txt` - puzzle input (the one I solved).

How I solved it

**Part 1: Check available IDs**
- For each available ID, ask: "Does this ID fall into *any* of the fresh ranges?"
- This is a simple range check: `start ≤ ID ≤ end` for each range.
- Count how many pass.

**Part 2: Count all unique fresh IDs across ranges**
- Ignore the available IDs; just look at the ranges.
- Merge overlapping ranges (e.g., 3-5 and 4-7 → 3-7).
- Sum up the counts for each merged range: `(end - start + 1)`.

**Why merge ranges for part 2?**
- Overlapping ranges cover some IDs multiple times.
- Merging prevents double-counting and is O(n log n) instead of O(n²).


How to run

```sh
python3 solution.py input.txt
python3 solution.py input1.txt
```

The script prints:

- `Part 1 (available fresh IDs): <count>`
- `Part 2 (total fresh IDs across ranges): <count>`