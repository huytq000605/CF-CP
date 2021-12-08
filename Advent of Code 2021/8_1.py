import sys
import collections
import math
def get_int(): return int(input())
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_list(): return list(map(int, sys.stdin.readline().strip().split()))
def get_string(): return sys.stdin.readline().strip()


def main():
	lines = sys.stdin.read().splitlines()
	print(solve(lines))


def solve(lines):
	result = 0
	for line in lines:
		before, after = line.split("|")
		before = before.split()
		after = after.split()
		
		for word in after:
			if len(word) in [2,3,4,7]:
				result += 1

	return result




if __name__ == "__main__":
	main()
