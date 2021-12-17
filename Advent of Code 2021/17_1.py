import sys
import collections
from functools import lru_cache
from typing import *
import math
import copy
import itertools
from heapq import heappush, heappop
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
	x = []
	y = []
	for line in lines:
		line = line.split()
		x = line[2][2:].split("..")
		x[1] = x[1][:len(x[1]) - 1]
		x = list(map(int, x))
		y = list(map(int, line[3][2:].split("..")))
	print(solve(x, y))

class BreakOutException(Exception):
	pass

# x[0] <= x*n - n*(n+1)/2 <= x[1]
# y[0] <= y*n - n*(n+1)/2 <= y[1]
def solve(x, y):
	bestY = 0
	for x_v in range(1, x[1] + 1):
		for y_v in range(-500, 500):
			xVec, yVec = x_v, y_v
			i, j = 0, 0
			best = 0
			ok = False
			while j >= y[0] and i <= x[1]:
				i += xVec
				j += yVec
				best = max(best, j)
				if xVec > 0:
					xVec -= 1
				yVec -= 1
				if i >= x[0] and i <= x[1] and j >= y[0] and j <= y[1]:
					ok = True
			if ok:
				bestY = max(bestY, best)
					
	return bestY

if __name__ == "__main__":
	main()
