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
		get_string()
		n, m = get_ints()
		knew_numbers = []
		for j in range(n):
			knew_numbers.append(get_string())
		new_numbers = get_string()
		result = solve(knew_numbers, new_numbers, m)
		if len(result) == 0:
			print("-1")
		else:
			print(len(result))
			for triplet in result:
				print(triplet)


def solve(knew_nums, new_nums, m):
	strs = dict()
	for idx, num in enumerate(knew_nums):
		for i in range(m - 1):
			two = num[i:i+2]
			three = num[i:i+3]
			strs[two] = f"{i+1} {i+2} {idx+1}"
			if len(three) == 3:
				strs[three] = f"{i+1} {i+3} {idx+1}"
	
	dp = [0 for i in range(m)]
	dp.append(1)
	dp.append(1)
	for i in range(m - 2, -1, -1):
		if dp[i+2] == 1 and new_nums[i:i+2] in strs:
			dp[i] = 1
		if dp[i+3] == 1 and new_nums[i:i+3] in strs:
			dp[i] = 1
	
	if dp[0] == 1:
		result = []
		idx = 0
		while idx < m:
			if dp[idx + 2] == 1:
				result.append(strs[new_nums[idx:idx+2]])
				idx += 2
			else:
				result.append(strs[new_nums[idx:idx+3]])
				idx += 3
		return result
	else:
		return []

if __name__ == "__main__":
	main()