# Day 4 - Printing Department

This folder contains my solution to Advent of Code 2025 - Day 4: Printing Department.

Puzzle synopsis

The map is a grid where `@` marks large rolls of paper. Forklifts can access a
roll only if fewer than four of the eight adjacent cells (including diagonals)
also contain `@`.

- **Part 1:** Count how many rolls are accessible to forklifts.
- **Part 2:** Iteratively remove accessible rolls (once removed, recalculate accessibility).
  Count the total number of rolls that can be removed until none remain.

Result (my input)

- **Part 1 answer:** 1467
- **Part 2 answer:** 8484

Files

- `solution.py` - Python solution that prints both part 1 and part 2 answers.
- `input.txt` - example input from puzzle description.
- `input1.txt` - my puzzle input (the one I solved).

How I solved it

Part 1:
- Parse the input into a 2D grid (list of lists of characters).
- For each `@` cell, count how many of the eight neighbors are `@`.
- If the count is less than 4, it's accessible; increment the counter.

Part 2:
- Repeatedly scan for accessible rolls, remove them (mark as `.`), and count.
- Continue until no more accessible rolls exist.
- This simulates the iterative removal process described in the problem.

How to run

```sh
python3 solution.py input.txt
python3 solution.py input1.txt
```

The script prints:

- `Part 1 (accessible rolls): <number>`
- `Part 2 (total removable rolls): <number>`
