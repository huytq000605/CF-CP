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
		n, k = get_ints()
		s = get_string()
		print(solve(s, k, n))


def solve(s, k, n):
	start = 1
	end = n // k
	count = Counter(s)
	pairs = 0
	ones = 0
	for letter in count.keys():
		if count[letter] % 2 == 0:
			pairs += count[letter] // 2
		else:
			pairs += count[letter] // 2
			ones += 1
	while start < end:
		mid = start + math.ceil((end - start + 1)/ 2)
		current_ones = ones
		current_pairs = pairs
		invalid = False
		for i in range(k):
			current_pairs -= mid // 2
			if mid %  2 == 1:
				if current_ones > 0: current_ones -= 1
				else: 
					current_ones += 1
					current_pairs -= 1
			if current_pairs < 0:
				invalid = True
				break
		if invalid:
			end = mid - 1
		else:
			start = mid
	return start

if __name__ == "__main__":
	main()