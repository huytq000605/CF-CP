import sys
import collections
import math
import itertools
def get_int(): return int(input())
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_list(): return list(map(int, sys.stdin.readline().strip().split()))
def get_string(): return sys.stdin.readline().strip()


def main():
	lines = sys.stdin.read().splitlines()
	print(solve(lines))

class BreakOutException(Exception):
	pass


def solve(lines):
	result = 0
	score =  {
		")": 3,
		"]": 57,
		"}": 1197,
		">": 25137
	}
	mapping = {
		"(": ")",
		"[": "]",
		"{": "}",
		"<": ">"
	}
	for line in lines:
		stack = []
		for l in line:
			if l in "([{<":
				stack.append(l)
			else:
				if len(stack) == 0 or stack[-1] != mapping[stack[-1]] != l:
					result += score[l]
					break
				else:
					stack.pop()
		
	return result


if __name__ == "__main__":
	main()
