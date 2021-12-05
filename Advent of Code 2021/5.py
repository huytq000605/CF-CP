import sys
def get_int(): return int(input())
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_list(): return list(map(int, sys.stdin.readline().strip().split()))
def get_string(): return sys.stdin.readline().strip()


def main():
	lines = sys.stdin.read().splitlines()
	points = []
	for line in lines:
		point1, _, point2 = line.split()
		point1 = list(map(int, point1.split(",")))
		point2 = list(map(int, point2.split(",")))
		points.append([point1, point2])
		
	print(solve(points))


def solve(points):
	n = 1000
	grid = [[0 for j in range(n)] for i in range(n)]
	for point1, point2 in points:
		if point1[0] == point2[0]:
			row = point1[0]
			col1 = min(point1[1], point2[1])
			col2 = max(point1[1], point2[1])
			for col in range(col1, col2 + 1):
				grid[row][col] += 1
		if point1[1] == point2[1]:
			col = point1[1]
			row1 = min(point1[0], point2[0])
			row2 = max(point1[0], point2[0])
			for row in range(row1, row2 + 1):
				grid[row][col] += 1
		if point1[1] - point1[0] == point2[1] - point2[0]:
			startRow = min(point1[0], point2[0])
			startCol = min(point1[1], point2[1])
			endRow = max(point1[0], point2[0])
			for i in range(0, endRow - startRow + 1):
				grid[startRow + i][startCol + i] += 1
		if point1[1] + point1[0] == point2[0] + point2[1]:
			startRow = min(point1[0], point2[0])
			endRow = max(point1[0], point2[0])
			startCol = max(point1[1], point2[1])
			for i in range(0, endRow - startRow + 1):
				grid[startRow + i][startCol - i] += 1

	result = 0
	for i in range(n):
		for j in range(n):
			if grid[i][j] >= 2:
				result += 1
	return result



if __name__ == "__main__":
	main()