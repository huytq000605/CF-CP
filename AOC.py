import sys
def get_int(): return int(input())
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_list(): return list(map(int, sys.stdin.readline().strip().split()))
def get_string(): return sys.stdin.readline().strip()


def main():
	lines = sys.stdin.read().splitlines()
	arr = []
	for line in lines:
		action, step = line.split(" ")
		step = int(step)
		arr.append([action, step])
	print(solve(arr))
	

		
def solve(arr):
	aim = 0
	depth = 0
	horizontal = 0
	for action, step in arr:
		if action == "forward":
			horizontal += step
			depth += step * aim
		elif action == "down":
			aim += step
		else:
			aim -= step
	return depth * horizontal


if __name__ == "__main__":
	main()