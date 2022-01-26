from functools import lru_cache as cache
from collections import Counter
import math
from heapq import *

import sys
def get_int(): return int(input())
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_list(): return list(map(int, sys.stdin.readline().strip().split()))
def get_string(): return sys.stdin.readline().strip()

def main():
	testcases = get_int()
	for _ in range(testcases):
		get_string()
		vertices, edges = get_ints()
		graph = [[] for i in range(vertices + 1)]
		for i in range(edges):
			u, v, w = get_ints()
			graph[u].append((v, w))
			graph[v].append((u, w))
		print(solve(graph, vertices))


def solve(graph, vertices):
	not_in_ans = 0
	ans = (1<<30) - 1
	for i in range(30, -1, -1):
		not_in_ans |= (1<<i)
		seen = set()
		stack = [1]
		while stack:
			for next_node, weight in graph[stack.pop()]:
				if next_node in seen or (weight & not_in_ans):
					continue
				seen.add(next_node)
				stack.append(next_node)
		not_in_ans &= ~(1<<i)

		if len(seen) == vertices:
			not_in_ans |= (1 << i)
			ans &= ~(1 << i)
	return ans
		


if __name__ == "__main__":
	main()