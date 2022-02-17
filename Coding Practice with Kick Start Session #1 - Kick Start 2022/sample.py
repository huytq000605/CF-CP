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
	for i in range(testcases):
		n, m = get_ints()
		candies = get_list()
		
		print(f"Case #{i + 1}: {solve(candies, m)}")


def solve(candies, kids):
	total = sum(candies)
	return total - total // kids * kids

if __name__ == "__main__":
	main()