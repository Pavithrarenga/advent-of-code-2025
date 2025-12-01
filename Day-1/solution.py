"""
Advent of Code 2025 — Day 1: Secret Entrance

Solution file that computes both parts for the dial/safe puzzle.

Usage: python3 solution.py input1.txt
"""
from pathlib import Path
import sys


def part1_count(filename: str) -> int:
    """Count number of times the dial *ends* a rotation pointing at 0.

    The dial has numbers 0..99 and starts at 50. Rotations are L/R followed by
    a distance. Use modulo 100 to compute final position of each rotation.
    """
    pos = 50
    count_zero = 0

    with open(filename) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            direction = line[0]
            distance = int(line[1:])

            if direction == 'L':
                pos = (pos - distance) % 100
            else:  # 'R'
                pos = (pos + distance) % 100

            if pos == 0:
                count_zero += 1

    return count_zero


def part2_count(filename: str) -> int:
    """Count every time the dial points at 0 during any click (not just final).

    For large distances this iterates per click. Because distances can be large
    (e.g., > 1000), this is accurate but potentially slow for huge inputs.
    """
    pos = 50
    zero_count = 0

    with open(filename) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            direction = line[0]
            distance = int(line[1:])

            step = -1 if direction == 'L' else 1

            for _ in range(distance):
                pos = (pos + step) % 100
                if pos == 0:
                    zero_count += 1

    return zero_count


def main():
    infile = sys.argv[1] if len(sys.argv) > 1 else 'input1.txt'
    if not Path(infile).exists():
        print(f'Input file not found: {infile}')
        return

    a = part1_count(infile)
    b = part2_count(infile)

    print('Part 1 (ends of rotations at 0):', a)
    print('Part 2 (all clicks that hit 0):', b)


if __name__ == '__main__':
    main()
