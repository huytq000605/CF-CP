from functools import lru_cache as cache
from collections import Counter
import math
from heapq import *

import sys
def get_int(): return int(input())
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_list(): return list(map(int, sys.stdin.readline().strip().split()))
def get_string(): return sys.stdin.readline().strip()

def main():
	testcases = get_int()
	for _ in range(testcases):
		n = get_int()
		grid = [None for i in range(2*n)]
		for i in range(2*n):
			grid[i] = get_list()
		print(solve(grid, n))


def solve(grid, n):
	result = 0
	for row in range(n, n*2):
		for col in range(n, n*2):
			result += grid[row][col]
	return result + min(grid[0][n], grid[0][2*n-1], grid[n-1][n], grid[n-1][2*n-1], grid[n][n-1], grid[n][0], grid[2*n-1][0], grid[2*n-1][n-1])

if __name__ == "__main__":
	main()