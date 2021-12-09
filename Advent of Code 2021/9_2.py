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
	result = []
	seen = set()

	def dfs(i, j):
		nonlocal seen, howmany
		howmany += 1
		for d in dirs:
			nr, nc = i + d[0], j + d[1]
			if nr < 0 or nr >= m or nc < 0 or nc >= n or (nr,nc) in seen or grid[nr][nc] == 9:
				continue
			seen.add((nr, nc))
			dfs(nr, nc)

	for i in range(m):
		for j in range(n):
			if (i, j) not in seen and grid[i][j] < 9:
				seen.add((i, j))
				howmany = 0
				dfs(i, j)
				result.append(howmany)
	result.sort(reverse = True)
	return result[0] * result[1] * result[2]




if __name__ == "__main__":
	main()
