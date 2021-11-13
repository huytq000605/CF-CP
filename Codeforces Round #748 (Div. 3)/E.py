import sys
from collections import deque
input = sys.stdin.readline

def get_int(): return int(sys.stdin.readline())
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_list(): return list(map(int, sys.stdin.readline().strip().split()))
def get_string(): return sys.stdin.readline().strip()

def main():
	testcases = get_int()
	for i in range(testcases):
		get_string()
		lines, operations = get_list()
		graph = {}
		for j in range(lines - 1):
			edge1, edge2 = get_ints()
			if edge1 not in graph:
				graph[edge1] = {}
			if edge2 not in graph:
				graph[edge2] = {}
			graph[edge1][edge2] = True
			graph[edge2][edge1] = True
		print(solve(graph, operations))
		
def solve(graph, operations):
	removed = set()
	total = len(graph)
	queue = deque()
	queue2 = deque()
	operations -= 1
	for vertice in graph.keys():
		if len(graph[vertice]) <= 1:
			queue.append(vertice)
			removed.add(vertice)
	while operations > 0 and len(queue) > 0:
		while len(queue):
			node = queue.popleft()
			for connect in graph[node]:
				graph[connect].pop(node)
				if len(graph[connect]) <= 1 and connect not in removed:
					queue2.append(connect)
					removed.add(connect)
		queue, queue2 = queue2, queue
		operations -= 1
	
	return total - len(removed)


if __name__ == "__main__":
	main()