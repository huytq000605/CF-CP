import math
def main():
	testcases = int(input())
	for i in range(testcases):
		num = input()
		print(solve(num))
		
END_WITH = ["00", "25", "50", "75"]
def solve(num: str):
	result = math.inf
	for end in END_WITH:
		pos = 1
		res = 0
		for i in range(len(num) - 1, -1, -1):
			if num[i] == end[pos]:
				pos -= 1
				if pos == -1:
					result = min(result, res)
					break
			else:
				res += 1
	return result


if __name__ == "__main__":
	main()