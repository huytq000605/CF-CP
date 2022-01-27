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
		n = get_int()
		segments = []
		for i in range(n):
			l, r, c = get_ints()
			segments.append((l, r, c))
		solve(segments, n)



def solve(segments, n):
	cur_min = segments[0][0]
	cur_max = segments[0][1]
	hold_min = 0
	hold_max = 0
	fit_all = 0
	print(segments[0][2])
	for i in range(1, n):
		l, r, c = segments[i]

		if l < cur_min:
			cur_min = l
			hold_min = i
		elif l == cur_min:
			if c < segments[hold_min][2]:
				hold_min = i

		if r > cur_max:
			cur_max = r
			hold_max = i
		elif r == cur_max:
			if c < segments[hold_max][2]:
				hold_max = i

		if fit_all >= 0 and (segments[fit_all][0] != cur_min or segments[fit_all][1] != cur_max):
			fit_all = -1

		if l == cur_min and r == cur_max:
			if fit_all >= 0 and segments[fit_all][2] < c:
				fit_all = fit_all
			else:
				fit_all = i
			
		if fit_all >= 0:
			print(min(segments[hold_min][2] + segments[hold_max][2], segments[fit_all][2]))
		else:
			print(segments[hold_min][2] + segments[hold_max][2])



if __name__ == "__main__":
	main()