import sys
import math

def get_int(): return int(input())
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_list(): return list(map(int, sys.stdin.readline().strip().split()))
def get_string(): return sys.stdin.readline().strip()

def main():
	testcases = get_int()
	for i in range(testcases):
		length = get_int()
		nums = get_list()
		print(solve(nums))
		
def solve(nums):
	minNum = min(*nums)
	result = 0
	for num in nums:
		result = math.gcd(result, num - minNum)
	if result == 0: return -1
	return result




if __name__ == "__main__":
	main()