import sys
import collections
import math
import itertools
def get_int(): return int(input())
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_list(): return list(map(int, sys.stdin.readline().strip().split()))
def get_string(): return sys.stdin.readline().strip()


def main():
	lines = sys.stdin.read().splitlines()
	graph = collections.defaultdict(list)
	for line in lines:
		a, b = line.split("-")
		graph[a].append(b)
		graph[b].append(a)
	print(solve(graph))


class BreakOutException(Exception):
	pass


def solve(graph):

	def dfs(current, seen):
		if current == "end":
			return 1
		result = 0
		for nextNode in graph[current]:
			if nextNode not in seen:
				if nextNode.islower():
					seen.add(nextNode)
				result += dfs(nextNode, seen)
				if nextNode.islower():
					seen.remove(nextNode)
		return result
	
	return dfs("start", set(["start"]))



	
	


if __name__ == "__main__":
	main()
