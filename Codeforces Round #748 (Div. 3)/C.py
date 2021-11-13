import sys
def get_int(): return int(input())
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_list(): return list(map(int, sys.stdin.readline().strip().split()))
def get_string(): return sys.stdin.readline().strip()



def main():
	testcases = get_int()
	for i in range(testcases):
		n, k = get_ints()
		positions = get_list()
		print(solve(n, k, positions))
		
def solve(n, k , positions):
	result = 0
	goal = n
	cat = 1
	positions.sort(reverse = True)
	for i in range(len(positions)):
		if (goal - positions[i]) > n or cat > positions[i]:
			return result
		else:
			result += 1
			cat += (goal - positions[i])
			n -= (goal - positions[i])
	return result


if __name__ == "__main__":
	main()