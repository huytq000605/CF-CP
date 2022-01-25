from functools import lru_cache as cache
import math
from heapq import *

import sys
def get_int(): return int(input())
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_list(): return list(map(int, sys.stdin.readline().strip().split()))
def get_string(): return sys.stdin.readline().strip()

def main():
	testcases = get_int()
	for i in range(testcases):
		n = get_int()
		arr = get_list()
		if solve(arr, n):
			print("YES")
		else:
			print("NO")


def solve(arr, n):
	count = [0 for i in range(n + 1)]
	for i in range(n):
		num = arr[i]
		while num > 0:
			if num <= n:
				count[num] += 1
			num >>= 1
	
	for i in range(n, 0, -1):
		num = i
		if count[num] == 0:
			return False
		while num > 0:
			count[num] -= 1
			num >>= 1

	return True
	
if __name__ == "__main__":
	main()