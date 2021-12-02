import sys
def get_int(): return int(input())
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_list(): return list(map(int, sys.stdin.readline().strip().split()))
def get_string(): return sys.stdin.readline().strip()


def main():
	testcases = get_int()
	for i in range(testcases):
		order = get_string()
		st = get_string()
		print(solve(st, order))
		
def solve(st, order):
	lookup = dict()
	for i, l in enumerate(order):
		lookup[l] = i
	n = len(st)
	result = 0
	for i in range(1, n):
		result += abs(lookup[st[i]] - lookup[st[i-1]])
	return result



if __name__ == "__main__":
	main()