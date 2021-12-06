import sys
import collections
def get_int(): return int(input())
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_list(): return list(map(int, sys.stdin.readline().strip().split()))
def get_string(): return sys.stdin.readline().strip()


def main():
	lines = sys.stdin.read().splitlines()
	line = lines[0]
	nums = list(map(int, line.split(",")))
	print(solve(nums))


def solve(points):
	n = 256
	freqs = collections.defaultdict(int)
	result = len(points)
	for point in points:
		freqs[point] += 1
	for day in range(n):
		day = day % 9
		for num in range(9):
			freq = freqs[num]
			if num == day:
				result += freq
				freqs[day] = 0
				freqs[(day + 7) % 9] += freq
				freqs[(day + 9) % 9] += freq
	
	return result

if __name__ == "__main__":
	main()