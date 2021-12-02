from functools import lru_cache as cache
from math import *
from heapq import *
import sys
def get_int(): return int(input())
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_list(): return list(map(int, sys.stdin.readline().strip().split()))
def get_string(): return sys.stdin.readline().strip()

dirs = {
		"U": [-1, 0],
		"D": [1, 0],
		"L": [0, -1],
		"R": [0, 1]
	}

def main():
	testcases = get_int()
	for i in range(testcases):
		m, n = get_ints()
		command = get_string()
		print(solve(m, n, command))

def solve(m, n, command):
	k = len(command)
	left = [0] * k
	right = [0] * k
	up = [0] * k
	down = [0] * k
	cur = [0,0]
	for i in range(k):
		d = dirs[command[i]]
		cur[0] += d[0]
		cur[1] += d[1]
		if i > 0:
			left[i] = left[i-1]
			right[i] = right[i-1]
			up[i] = up[i-1]
			down[i] = down[i-1]
		left[i] = max(left[i], -cur[1])
		right[i] = max(right[i], cur[1])
		up[i] = max(up[i], -cur[0])
		down[i] = max(down[i], cur[0])
	for i in range(k - 1, -1, -1):
		# Greedy, if go out side the board => unvalid
		if(left[i] + right[i] + 1 > n): continue
		if(up[i] + down[i] + 1 > m): continue
		# Because we know it cannot go outside
		# Just pick a valid point from one side
		return f"{up[i] + 1} {left[i] + 1} "
	return "1 1"


if __name__ == "__main__":
	main()