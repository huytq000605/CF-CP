import sys
import collections
import math
import itertools
def get_int(): return int(input())
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_list(): return list(map(int, sys.stdin.readline().strip().split()))
def get_string(): return sys.stdin.readline().strip()


def main():
	lines = sys.stdin.read().splitlines()
	maxRow = 0
	maxCol = 0

	instruction = False
	instructions = []
	for line in lines:
		if line == "":
			instruction = True
			continue
		if instruction:
			line = line.split(" ")[2]
			instructions.append([line[0], int(line[2:])])
		else:
			col, row = list(map(int, line.split(",")))
			maxCol = max(maxCol, col)
			maxRow = max(maxRow, row)
		
	grid = [[0 for j in range(maxCol + 1)] for i in range(maxRow + 1)]
	for line in lines:
		if line == "":
			break
		else:
			col, row = list(map(int, line.split(",")))
			grid[row][col] = 1

	print(solve(grid, instructions))


class BreakOutException(Exception):
	pass


def solve(grid, instructions):
	maxRow = len(grid)
	maxCol = len(grid[0])
	result = 0

	for i in range(1):
		axis, pos = instructions[i]
		
		if axis == "x":
			for row in range(0, maxRow):
				for col in range(pos - 1, -1, -1):
					if pos + pos - col > maxCol:
						break
					grid[row][col] |= grid[row][pos + pos - col]
			maxCol = pos - 1
		else:
			for col in range(0, maxCol):
				for row in range(pos - 1, -1, -1):
					if pos + (pos - row) > maxRow:
						break
					grid[row][col] |= grid[pos + pos - row][col]
			maxRow = pos - 1
		
	for row in range(maxRow):
		for col in range(maxCol):
			if grid[row][col] == 1:
				result += 1
	return result


if __name__ == "__main__":
	main()
