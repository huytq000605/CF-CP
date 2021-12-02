from functools import lru_cache as cache
import sys
def get_int(): return int(input())
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_list(): return list(map(int, sys.stdin.readline().strip().split()))
def get_string(): return sys.stdin.readline().strip()


def main():
	testcases = get_int()
	for i in range(testcases):
		arr = get_list()
		colors = get_string()
		print(solve(arr, colors))

def solve(arr, colors):
	n = len(arr)
	blue = []
	red = []
	# Greedy choose Blue for all small numbers and Red for all big numbers
	for num, color in zip(arr, colors):
		if color == "B":
			blue.append(num)
		else:
			red.append(num)
	blue.sort(reverse= True)
	red.sort(reverse=True)
	num = 1
	while num <= n:
		if blue:
			if blue[-1] < num:
				return "NO"
			else:
				blue.pop()
		else:
			if red[-1] > num:
				return "NO"
			else:
				red.pop()
		num += 1
	return "YES"



if __name__ == "__main__":
	main()