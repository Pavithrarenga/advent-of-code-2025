# Advent of Code — Day 2 "Gift Shop"
# This code computes the sum of all "invalid IDs" in a comma-separated list of ranges.
# An invalid ID is a decimal number formed by repeating a digit-sequence twice (e.g. 11, 6464, 123123).
# No leading zeros are allowed (so the repeated half must have the correct number of digits and not start with 0).

"""
Advent of Code 2025 — Day 2: Gift Shop

Solution file that computes the sum of all invalid IDs in given ranges.

Usage: python3 solution.py input1.txt
"""

def is_invalid_id_part1(number):
    s = str(number)

    # Only even-length numbers can be "X repeated twice"
    if len(s) % 2 != 0:
        return False

    half = len(s) // 2
    first = s[:half]
    second = s[half:]

    return first == second

def is_invalid_id_part2(number):
    s = str(number)
    length = len(s)

    # Try every possible chunk size
    for chunk_size in range(1, length):   # chunk must be smaller than whole
        if length % chunk_size == 0:      # chunk must divide evenly
            chunk = s[:chunk_size]
            repeated = chunk * (length // chunk_size)
            if repeated == s:
                return True
    return False

def sum_invalid_ids(ranges_line):
    # Split input into individual ranges
    parts = [p.strip() for p in ranges_line.split(",") if p.strip()]

    total = 0

    for part in parts:
        # Each part is like "11-22"
        lo_str, hi_str = part.split("-")
        lo = int(lo_str)
        hi = int(hi_str)

        # Check all numbers in the range
        for num in range(lo, hi + 1):
            if is_invalid_id_part2(num):
                total += num

    return total

# Example input
example = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"
print("Example sum:", sum_invalid_ids(example))


def sum_from_file(path: str) -> int:
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read().strip()
    return sum_invalid_ids(text)

sum_invalid_ids = sum_from_file("input.txt")
print("Invalid Ids sum:", sum_invalid_ids)



