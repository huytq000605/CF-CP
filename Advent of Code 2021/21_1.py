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
	turns = 0
	die = 1
	t1, t2 = 0, 0
	s1, s2 = 0, 0
	while s1 < 1000 and s2 < 1000:
		if turns % 2 == 0:
			t = t1
			p = p1
			s = s1
		else:
			t = t2
			p = p2
			s = s2
		
		t += 1
		steps = 0
		for i in range(3):
			steps += die
			die += 1
			if die == 101:
				die = 1
		
		steps %= 10
		p = p + steps
		if p > 10:
			p = p % 10
		s += p

		if turns % 2 == 0:
			t1 = t
			p1 = p
			s1 = s
		else:
			t2 = t
			p2 = p
			s2 = s
		turns += 1
	
	if s1 >= 1000:
		return s2 * turns * 3
	else:
		return s1 * turns * 3


if __name__ == "__main__":
	main()
