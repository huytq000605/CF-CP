import sys
def get_int(): return int(input())
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_list(): return list(map(int, sys.stdin.readline().strip().split()))
def get_string(): return sys.stdin.readline().strip()


def main():
	lines = sys.stdin.read().splitlines()
	nums = list(map(int, lines[0].split(",")))
	arrs = []
	for i in range(len(lines)):
		if i == 0: continue
		line = lines[i]
		if line == "":
			arrs.append([])
		else:
			arrs[-1].append([])
			arrs[-1][-1] = list(map(int, line.split()))
	sums = [0] * len(arrs)
	for k in range(len(arrs)):
		total = 0
		for i in range(len(arrs[k])):
			for j in range(len(arrs[k][i])):
				arrs[k][i][j] = [arrs[k][i][j], 0]
				total += arrs[k][i][j][0]
		sums[k] = total
			
	print(solve(nums, arrs, sums))

def mark(arr, value):
	m = len(arr)
	n = len(arr[0])
	for row in range(m):
		for col in range(n):
			if arr[row][col][0] == value:
				arr[row][col][1] = 1
				return

def marked(arr):
	result = 0
	for row in range(5):
		for col in range(5):
			if arr[row][col][1] == 1:
				result += arr[row][col][0]
	return result


def check(arr, all):
	rows = len(arr)
	cols = len(arr[0])

	for row in range(rows):
		valid = True
		for col in range(cols):
			if arr[row][col][1] == 0:
				valid = False
				break
		if valid:
			markedValue = marked(arr)
			return all - markedValue
	
	for col in range(cols):
		valid = True
		for row in range(rows):
			if arr[row][col][1] == 0:
				valid = False
				break
		if valid:
			markedValue = marked(arr)
			return all - markedValue

	return -1
	
	

def solve(nums, arrs, sums):
	result = 0
	done = set()
	for num in nums:
		for i in range(len(arrs)):
			if i in done:
				continue
			mark(arrs[i], num)
			value = check(arrs[i], sums[i])
			if value != -1:
				done.add(i)
				result = value * num
	return result



if __name__ == "__main__":
	main()