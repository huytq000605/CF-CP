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
		n = get_int()
		papers = get_list()
		print(f"Case #{i + 1}: {solve(papers, n)}")


def solve(papers, n):
	counter = Counter()
	level = 0
	current = 0
	result = []
	for paper in papers:
		if paper > level:
			current += 1
			counter[paper] += 1
			if current > level:
				level += 1
				current -= counter[level]
		result.append(level)
	return " ".join(map(str, result))

if __name__ == "__main__":
	main()