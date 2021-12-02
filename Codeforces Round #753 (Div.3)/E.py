from functools import lru_cache as cache
import sys
def get_int(): return int(input())
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_list(): return list(map(int, sys.stdin.readline().strip().split()))
def get_string(): return sys.stdin.readline().strip()

dirs = {
		"U": [-1, 0],
		"D": [1, 0],
		"L": [0, -1],
		"R": [0, 1]
	}

def main():
	testcases = get_int()
	for i in range(testcases):
		m, n = get_ints()
		command = get_string()
		print(solve(m, n, command))

def solve(m, n, command):
	k = len(command)

	@cache(None)
	def dfs1(r, idx):
		if idx >= k:
			return 0
		d = dirs[command[idx]]
		nr = r + d[0]
		if nr < 0 or nr >= m:
			return 0
		return 1 + dfs1(nr, idx + 1)
	
	@cache(None)
	def dfs2(c, idx):
		if idx >= k:
			return 0
		d = dirs[command[idx]]
		nc = c + d[1]
		if nc < 0 or nc >= n:
			return 0
		return 1 + dfs2(nc, idx + 1)
	result = 0
	points = (0, 0)

	for i in range(m):
		for j in range(n):
			path = min(dfs1(i, 0), dfs2(j, 0))
			if path > result:
				result = path
				points = (i, j)
	return f"{points[0] + 1} {points[1] + 1}"


if __name__ == "__main__":
	main()