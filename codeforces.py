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
		s = get_string()
		print(solve(s, n))

def solve(s, n):
	result = math.inf
	a = 0
	b = 0
	c = 0
	start = 0
	for i in range(n):
		if s[i] == "a": a += 1
		if s[i] == "b": b += 1
		if s[i] == "c": c += 1

		while i - start + 1 > 2 and (s[start] == 'b' or s[start] == 'c' or (s[start] == "a" and a - 1 > b and a - 1 > c)):
			if s[start] == "a": a -= 1
			if s[start] == "b": b -= 1
			if s[start] == "c": c -= 1
			start += 1

		if b > a or c > a or b + c > a:
			start = i + 1
			a = b = c = 0
		
		if i - start + 1 >= 2 and a > b and a > c:
			result = min(result, i - start + 1)
	
	if result == math.inf:
		return -1
	return result


if __name__ == "__main__":
	main()