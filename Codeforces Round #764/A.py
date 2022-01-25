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
	for testcase in testcases:
		n = get_int()
		arr = get_ints()
		print(solve(arr))


def solve(arr):
	return max(arr) - min(arr)


if __name__ == "__main__":
	main()