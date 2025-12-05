# Day 3 - Lobby

This folder contains my solution to Advent of Code 2025 - Day 3: Lobby.

Puzzle synopsis

Each line represents a bank of batteries (a string of digits, possibly with non-digit characters).
You must turn on exactly k batteries (preserving their order) to form a k-digit number.
The joltage output for the bank is that k-digit number.

- **Part 1:** Find the maximum 2-digit number per bank and sum them.
- **Part 2:** Find the maximum 12-digit number per bank and sum them.

Result (my input)

- **Part 1 answer:** 17095
- **Part 2 answer:** 168794698570517

Files

- `solution.py` - Python solution that prints both part 1 and part 2 answers for a given input
  (default: `input.txt`).
- `input.txt` - example input from puzzle description (4 banks).
- `input1.txt` - my puzzle input (the one I solved).

How I solved it

- For both parts, I extract only the digit characters from each bank.
- To find the maximum k-digit subsequence, I use a **greedy monotonic-stack algorithm** (O(n)):
  - Iterate through the digits, maintaining a stack of selected digits.
  - When a larger digit appears, greedily pop smaller digits from the stack
    (if we still have digits we can skip) to make room for the larger one.
  - This ensures we pick the lexicographically largest digit subsequence of length k,
    which gives the largest numeric value.
  - If any digits remain to skip (monotonic non-decreasing case), trim from the end.

How to run

```sh
python3 solution.py input.txt
python3 solution.py input1.txt
```

