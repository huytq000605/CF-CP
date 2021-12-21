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
	print(solve(2, 7))

class BreakOutException(Exception):
	pass

def solve(p1, p2):
	@lru_cache(None)
	def dp(s1, s2, p1, p2, turn1):
		if s2 >= 21:
			return 0
		if s1 >= 21:
			return 1
		s, p = 0, 0
		result = 0
		for step1 in range(1, 4):
			for step2 in range(1, 4):
				for step3 in range(1, 4):
					if turn1:
						s, p = s1, p1
					else:
						s, p = s2, p2
					steps = step1 + step2 + step3
					p = p + steps
					if p > 10:
						p %= 10
					s += p
					if turn1:
							result += dp(s, s2, p, p2, not turn1)
					else:
							result += dp(s1, s, p1, p, not turn1)
			
		return result

	
	print(dp(0, 0, p1, p2, True))
	print(dp(0, 0, p2, p1, False))


	
if __name__ == "__main__":
	main()
