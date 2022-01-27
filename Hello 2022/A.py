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
		n, k = get_ints()
		solve(n, k)


def solve(n, k):
	grid = [["." for j in range(n)] for i in range(n)]
	col = 0
	row = 0
	while row < n and col < n and k > 0:
		grid[row][col] = "R"
		k -= 1
		row += 2
		col += 2
	if k > 0:
		print("-1")
	else:
		for row in range(n):
			print("".join(map(str, grid[row])))



if __name__ == "__main__":
	main()