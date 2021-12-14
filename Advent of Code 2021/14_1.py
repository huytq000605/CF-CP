import sys
import collections
from typing import *
import math
import itertools
def get_int(): return int(input())
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_list(): return list(map(int, sys.stdin.readline().strip().split()))
def get_string(): return sys.stdin.readline().strip()

class Node:
	def __init__(self, val):
		self.val = val
		self.next = None

def main():
	lines = sys.stdin.read().splitlines()
	head = None
	current = None
	commands = collections.defaultdict(dict)
	for i, line in enumerate(lines):
		if i == 0:
			for l in line:
				if not head:
					head = Node(l)
					current = head
				else:
					current.next = Node(l)
					current = current.next
		elif i == 1:
			continue
		else:
			line = line.split(" ")
			u, v, inserted = line[0][0], line[0][1], line[2]
			commands[u][v] = inserted


	print(solve(head, commands))


class BreakOutException(Exception):
	pass


def solve(head: Node, commands):
	current = head
	for i in range(40):
		current = head
		while current.next != None:
			currentLetter = current.val
			nextLetter = current.next.val
			if nextLetter in commands[currentLetter]:
				originalNext = current.next
				current.next = Node(commands[currentLetter][nextLetter])
				current.next.next = originalNext
				current = current.next
			current = current.next
	freq = collections.Counter()
	current = head
	while current:
		freq[current.val] += 1
		current = current.next

	return max(freq.values()) - min(freq.values())
	

if __name__ == "__main__":
	main()
