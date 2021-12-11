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
	grid = [[int(lines[i][j]) for j in range(n)] for i in range(m)]
	print(solve(grid))

class BreakOutException(Exception):
	pass


def solve(grid):
	dirs = [[0,1], [1,0], [0,-1], [-1,0], [1,1], [-1, -1], [-1, 1], [1, -1]]
	m = len(grid)
	n = len(grid[0])
	step = 0
	while True:
		queue = []
		flash = 0
		for i in range(m):
			for j in range(n):
				queue.append([i, j])
		while queue:
			i, j = queue.pop()
			if grid[i][j] == 10:
				continue
			grid[i][j] += 1
			if grid[i][j] == 10:
				for d in dirs:
					nr, nc = i + d[0], j + d[1]
					if nr < 0 or nr >= m or nc < 0 or nc >= n or grid[nr][nc] == 10:
						continue
					queue.append([nr, nc])
		for i in range(m):
			for j in range(n):
				if grid[i][j] == 10:
					flash += 1
					grid[i][j] = 0
		if flash == m * n:
			return step + 1
		step += 1
	
	
if __name__ == "__main__":
	main()
