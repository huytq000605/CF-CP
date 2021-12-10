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
	score =  {
		")": 1,
		"]": 2,
		"}": 3,
		">": 4
	}
	mapping = {
		"(": ")",
		"[": "]",
		"{": "}",
		"<": ">"
	}
	scores = []
	for line in lines:
		stack = []
		corrupt = False
		for l in line:
			if l in "([{<":
				stack.append(l)
			else:
				if len(stack) == 0 or stack[-1] != mapping[stack[-1]] != l:
					corrupt = True
					break
				else:
					stack.pop()
		if not corrupt:
			complete = ""
			for l in stack[::-1]:
				complete += mapping[l]
			current = 0
			for l in complete:
				current *= 5
				current += score[l]
			scores.append(current)
	scores.sort()
	result = scores[len(scores) // 2]
		
	return result


if __name__ == "__main__":
	main()
