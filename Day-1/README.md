# Day 1 - Secret Entrance

This folder contains my solution to Advent of Code 2025 - Day 1: Secret Entrance.

Puzzle synopsis
- A dial with numbers 0..99 starts at 50.
- Each instruction is Lx or Rx which rotates left (toward lower numbers) or right
  (toward higher numbers) by x clicks. The dial wraps (mod 100).

Part 1: Count how many times the dial ends a rotation pointing at 0.
Part 2: Count every time the dial points at 0 during any click (including
intermediate clicks within a rotation).

Result (my input):
- Part 1 answer: 969
- Part 2 answer: 5887

Files
- `solution.py` - Python solution that prints both part answers for a given input
  (default: `input1.txt`).
- `input.txt` - example input from puzzle description.
- `input1.txt` - my puzzle input (the one I solved).

How I solved it
- For part 1 we simply compute final position of every rotation using modulo
  arithmetic and count how many final positions equal 0.
- For part 2 we simulate each individual click inside a rotation and increment
  a counter whenever the dial hits 0.

How to run
```sh
python3 solution.py input1.txt
```
