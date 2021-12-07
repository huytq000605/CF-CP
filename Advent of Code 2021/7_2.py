import sys
import collections
import math
def get_int(): return int(input())
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_list(): return list(map(int, sys.stdin.readline().strip().split()))
def get_string(): return sys.stdin.readline().strip()


def main():
	lines = sys.stdin.read().splitlines()
	line = lines[0]
	nums = list(map(int, line.split(",")))
	print(solve(nums))


def solve(nums):
	n = len(nums)
	result = [0] * (max(nums) - min(nums) + 1)
	for j in range(min(nums), max(nums) + 1):
		for i in range(n):
			diff = abs(nums[i] - j)
			result[j] += diff * (diff + 1) / 2
	return min(result)






if __name__ == "__main__":
	main()
