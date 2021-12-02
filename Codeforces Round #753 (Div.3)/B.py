import sys
def get_int(): return int(input())
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_list(): return list(map(int, sys.stdin.readline().strip().split()))
def get_string(): return sys.stdin.readline().strip()


def main():
	testcases = get_int()
	for i in range(testcases):
		x, n = get_ints()
		print(solve(x, n))
		
		# even => odd => odd => even => even => 
		# 1			2		3		4		5
def solve(x, n):
	mod = n % 4
	cur = n - mod + 1
	while cur <= n:
		if x % 2 == 0:
			x -= cur
		else:
			x += cur
		cur += 1
	return x

if __name__ == "__main__":
	main()