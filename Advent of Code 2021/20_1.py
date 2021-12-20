import sys
import collections
from functools import lru_cache
from typing import *
import math
import copy
import itertools
from heapq import heappush, heappop
import json
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
	lookup = [0 for i in range(512)]
	# m, n = (len(lines) - 2) * 4, len(lines[2]) * 4
	m, n = 500, 500
	grid = [[0 for j in range(n)] for i in range(m)]
	for j in range(512):
		lookup[j] = 1 if lines[0][j] == '#' else 0
	for row, line in enumerate(lines[2:]):
		for col, value in enumerate(line):
			grid[row + 200][col + 200] = 1 if value == "#" else 0
	
	print(solve(grid, lookup, m, n))
		

# < 6276
class BreakOutException(Exception):
	pass

def bin_to_dec(s):
	s = s[::-1]
	result = 0
	for i in range(len(s)):
		if s[i] == "1":
			result += 1 << i
	return result

def solve(grid, lookup, m, n):
	for time in range(2):
		nextGrid = copy.deepcopy(grid)
		for row in range(m):
			for col in range(n):
				binary = ""
				for r in range(row - 1, row + 2):
					for c in range(col - 1, col + 2):
						if r < 0 or r >= m or c < 0 or c >= n:
							# See the first and the last from lookup string
							# If first is # and last is .
							if time % 2 == 0:
								binary += "0"
							else:
								binary += "1"
							# Else if first is . and last is #
							# then just binary += "0"
						else:
							binary += str(grid[r][c])
				nextGrid[row][col] = lookup[bin_to_dec(binary)]
		grid = nextGrid
	
	result = 0
	for row in range(m):
		for col in range(n):
			if grid[row][col] == 1:
				result += 1
	print(grid[152])
	return result


	
if __name__ == "__main__":
	main()
