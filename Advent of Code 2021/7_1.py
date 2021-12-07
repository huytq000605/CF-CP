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
	nums.sort()
	median1 = len(nums) // 2 - 1
	median2 = len(nums) // 2
	def cal(lastPosition):
		total = 0
		for num in nums:
			diff = (num + lastPosition) * (abs(num - lastPosition)) // 2

			total += diff
		return total
	return min(cal(nums[median1]), cal(nums[median2]))



if __name__ == "__main__":
	main()