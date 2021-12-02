import sys
def get_int(): return int(input())
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_list(): return list(map(int, sys.stdin.readline().strip().split()))
def get_string(): return sys.stdin.readline().strip()


def main():
	testcases = get_int()
	for i in range(testcases):
		n = get_int()
		arr = get_list()
		print(solve(arr, n))

def solve(arr, n):
	arr.sort(reverse = True)
	result = arr[-1]
	plus = 0
	while len(arr) > 1:
		plus = plus - (arr.pop() + plus)
		result = max(result, arr[-1] + plus)
	return result


if __name__ == "__main__":
	main()