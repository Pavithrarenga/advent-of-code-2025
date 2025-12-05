"""
Advent of Code 2025 — Day 3: Lobby

Each input line is a bank of batteries (a string of digits). You must turn on
exactly two batteries (preserving their order) and the bank produces the
joltage equal to the two-digit number formed by those digits. Find the largest
possible joltage for each bank and sum them.

Usage: python3 solution.py input.txt
"""
from pathlib import Path
import sys


def max_joltage_from_bank(s: str, k: int = 2) -> int:
    """Return the maximum k-digit number formed by choosing k digits i1<i2<...<ik.

    Non-digit characters are ignored. If fewer than k digits exist, returns 0.
    Uses a greedy monotonic-stack algorithm (O(n)) to pick the lexicographically
    largest subsequence of digits of length k, which gives the largest numeric
    value when digits are decimal.
    """
    # Extract digit characters only
    digits = [c for c in s if c.isdigit()]
    n = len(digits)
    if n < k or k <= 0:
        return 0

    to_remove = n - k  # how many digits we may drop
    stack: list[str] = []

    for d in digits:
        while stack and to_remove > 0 and stack[-1] < d:
            stack.pop()
            to_remove -= 1
        stack.append(d)

    # If we still have to remove digits (monotonic non-decreasing case), trim from end
    if to_remove > 0:
        stack = stack[:-to_remove]

    chosen = stack[:k]
    return int(''.join(chosen))


def total_output_from_file(path: str, k: int = 2) -> int:
    total = 0
    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            s = line.strip()
            if not s:
                continue
            total += max_joltage_from_bank(s, k)
    return total


def main():
    infile = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
    if not Path(infile).exists():
        print(f'Input file not found: {infile}')
        return

    part1 = total_output_from_file(infile, k=2)
    part2 = total_output_from_file(infile, k=12)
    print(f'Part 1 (2-digit joltage): {part1}')
    print(f'Part 2 (12-digit joltage): {part2}')


if __name__ == '__main__':
    main()