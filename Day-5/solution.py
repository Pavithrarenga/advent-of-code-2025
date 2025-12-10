"""
Advent of Code 2025 — Day 5: Cafeteria

Determine which ingredient IDs are fresh by checking if they fall within
any of the fresh ranges. Count the fresh IDs.

Usage: python3 solution.py input.txt
"""
from pathlib import Path
import sys


def parse_input(path: str):
    """Parse input into fresh ranges and available ingredient IDs."""
    with open(path, 'r', encoding='utf-8') as f:
        lines = f.read().strip().split('\n')
    
    ranges = []
    ingredient_ids = []
    blank_found = False
    
    for line in lines:
        line = line.strip()
        
        if not line:  # blank line separates ranges from IDs
            blank_found = True
            continue
        
        if not blank_found:
            # Parse a range like "3-5"
            parts = line.split('-')
            if len(parts) == 2:
                start, end = int(parts[0]), int(parts[1])
                ranges.append((start, end))
        else:
            # Parse an ingredient ID
            ingredient_ids.append(int(line))
    
    return ranges, ingredient_ids


def is_fresh(ingredient_id: int, ranges: list) -> bool:
    """Check if an ingredient ID falls into any fresh range."""
    for start, end in ranges:
        if start <= ingredient_id <= end:
            return True
    return False


def count_fresh_ingredients(ranges: list, ingredient_ids: list) -> int:
    """Count how many ingredient IDs are fresh."""
    count = 0
    for iid in ingredient_ids:
        if is_fresh(iid, ranges):
            count += 1
    return count


def count_all_fresh_ids(ranges: list) -> int:
    """Count total unique ingredient IDs considered fresh by all ranges.
    
    Strategy: merge overlapping ranges, then sum the counts.
    """
    if not ranges:
        return 0
    
    # Sort ranges by start position
    sorted_ranges = sorted(ranges, key=lambda x: x[0])
    merged = []
    
    for start, end in sorted_ranges:
        if merged and start <= merged[-1][1] + 1:
            # Overlapping or adjacent: merge
            merged[-1] = (merged[-1][0], max(merged[-1][1], end))
        else:
            # Non-overlapping: add as new range
            merged.append((start, end))
    
    # Count total unique IDs
    total = 0
    for start, end in merged:
        total += end - start + 1
    
    return total


def main():
    infile = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
    if not Path(infile).exists():
        print(f'Input file not found: {infile}')
        return
    
    ranges, ingredient_ids = parse_input(infile)
    
    # Part 1: count fresh IDs from available list
    part1 = count_fresh_ingredients(ranges, ingredient_ids)
    
    # Part 2: count total unique IDs across all ranges
    part2 = count_all_fresh_ids(ranges)
    
    print(f'Part 1 (available fresh IDs): {part1}')
    print(f'Part 2 (total fresh IDs across ranges): {part2}')


if __name__ == '__main__':
    main()
