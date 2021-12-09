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
	m = len(lines)
	n = len(lines[0])
	grid = [[None for j in range(n)] for j in range(m)]
	for row, line in enumerate(lines):
		for col, num in enumerate(line):
			grid[row][col] = int(num)

	print(solve(grid, m, n))

class BreakOutException(Exception):
	pass


def solve(grid, m, n):
	dirs = [[0,1], [1,0], [-1,0], [0,-1]]
	result = 0
	
	for i in range(m):
		for j in range(n):
			low = True
			for d in dirs:
				nr, nc = i + d[0], j + d[1]
				if nr < 0 or nr >=m or nc < 0 or nc >= n:
					continue
				if grid[i][j] >= grid[nr][nc]:
					low = False
					break
			if low:
				result += grid[i][j] + 1
	return result




if __name__ == "__main__":
	main()
