
"""
Advent of Code 2025 — Day 4: Printing Department

Count how many paper rolls (`@`) are accessible to forklifts. A roll is
accessible if strictly fewer than four of its eight neighbors are also `@`.

Usage: python3 solution.py input.txt
"""
from pathlib import Path
import sys


def parse_grid(path: str):
	with open(path, 'r', encoding='utf-8') as f:
		grid = [list(line.rstrip('\n')) for line in f]
	return grid


def get_deltas():
	return [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]


def count_accessible_rolls(grid) -> int:
	rows = len(grid)
	deltas = get_deltas()
	total = 0

	for r in range(rows):
		for c in range(len(grid[r])):
			if grid[r][c] != '@':
				continue
			neigh = 0
			for dr, dc in deltas:
				nr, nc = r + dr, c + dc
				if 0 <= nr < rows and 0 <= nc < len(grid[nr]) and grid[nr][nc] == '@':
					neigh += 1
			if neigh < 4:
				total += 1
	return total


def total_removable_rolls(grid) -> int:
	"""Iteratively remove accessible rolls until none remain."""
	deltas = get_deltas()
	removed = 0
	
	while True:
		rows = len(grid)
		to_remove = []
		
		for r in range(rows):
			for c in range(len(grid[r])):
				if grid[r][c] != '@':
					continue
				neigh = 0
				for dr, dc in deltas:
					nr, nc = r + dr, c + dc
					if 0 <= nr < rows and 0 <= nc < len(grid[nr]) and grid[nr][nc] == '@':
						neigh += 1
				if neigh < 4:
					to_remove.append((r, c))
		
		if not to_remove:
			break
		
		for r, c in to_remove:
			grid[r][c] = '.'
		
		removed += len(to_remove)
	
	return removed


def main():
	infile = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
	if not Path(infile).exists():
		print(f'Input file not found: {infile}')
		return

	grid1 = parse_grid(infile)
	part1 = count_accessible_rolls(grid1)
	
	grid2 = parse_grid(infile)
	part2 = total_removable_rolls(grid2)
	
	print(f'Part 1 (accessible rolls): {part1}')
	print(f'Part 2 (total removable rolls): {part2}')


if __name__ == '__main__':
	main()

