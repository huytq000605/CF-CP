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

	def dfs(current, seen, haveTwice):
		if current == "end":
			return 1
		result = 0
		for nextNode in graph[current]:
			if nextNode == "start":
				continue
			if nextNode in seen and haveTwice:
				continue
			currentTwice = False
			if nextNode.islower():
				if nextNode not in seen:
					seen.add(nextNode)
				else:
					currentTwice = True
			result += dfs(nextNode, seen, haveTwice or currentTwice)
			if nextNode.islower() and currentTwice == False:
					seen.remove(nextNode)
		return result
	
	return dfs("start", set(["start"]), False)




if __name__ == "__main__":
	main()
