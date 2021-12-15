import sys
import collections
from functools import lru_cache
from typing import *
import math
import copy
import itertools
from heapq import heappush, heappop
def get_int(): return int(input())
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_list(): return list(map(int, sys.stdin.readline().strip().split()))
def get_string(): return sys.stdin.readline().strip()

class Node:
	def __init__(self, val):
		self.val = val
		self.next = None

def main():
	lines = sys.stdin.read().splitlines()
	m = len(lines)
	n = len(lines[0])
	grid = [[0 for j in range(n)] for i in range(m)]
	for row, line in enumerate(lines):
		for col, num in enumerate(line):
			grid[row][col] = int(num)
	newGrid = [[0 for j in range(n * 5)] for i in range(m * 5)]
	gridState = copy.deepcopy(grid)
	for repeatRow in range(0, 5):
		if repeatRow > 0:
			for i in range(m):
				for j in range(n):
					gridState[i][j] += 1
					if gridState[i][j] == 10:
						gridState[i][j] = 1
		grid = copy.deepcopy(gridState)
		for repeatCol in range(0, 5):
			if repeatCol > 0:
				for i in range(m):
					for j in range(n):
						grid[i][j] += 1
						if grid[i][j] == 10:
							grid[i][j] = 1
			for i in range(m):
				for j in range(n):
					newGrid[i + m * repeatRow][j + n * repeatCol] = grid[i][j]
	print(solve(newGrid, len(newGrid), len(newGrid[0])))


class BreakOutException(Exception):
	pass


def solve(grid, m, n):
	dirs = [[0,1], [1,0], [-1, 0], [0,-1]]
	distance = [[math.inf for j in range(n)] for i in range(m)]
	distance[0][0] = 0
	queue = [[0, 0, 0]]
	while queue:
		risk, r, c = heappop(queue)
		if r == m - 1 and c == n - 1:
			return risk
		for d in dirs:
			nr, nc = r + d[0], c + d[1]
			if nr < 0 or nr >= m or nc < 0 or nc >= n or risk + grid[nr][nc] >= distance[nr][nc]:
				continue
			distance[nr][nc] = risk + grid[nr][nc]
			heappush(queue, [distance[nr][nc], nr, nc])
			
	

if __name__ == "__main__":
	main()
