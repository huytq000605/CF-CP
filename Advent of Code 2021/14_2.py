import sys
import collections
from typing import *
import math
import copy
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
	s = ""
	pair_count = collections.defaultdict(Counter)
	commands = collections.defaultdict(dict)
	for i, line in enumerate(lines):
		if i == 0:
			s = line
			n = len(line)
			for j in range(0, n - 1):
				pair_count[line[j]][line[j+1]] += 1
		elif i == 1:
			continue
		else:
			line = line.split(" ")
			u, v, inserted = line[0][0], line[0][1], line[2]
			commands[u][v] = inserted

	print(solve(pair_count, commands, s))


class BreakOutException(Exception):
	pass


def solve(pair_count, commands, s):
	for i in range(40):
		next_pair_count = copy.deepcopy(pair_count)
		for fromLetter in commands.keys():
			for toLetter, insertLetter in commands[fromLetter].items():
					freq = pair_count[fromLetter][toLetter]
					if freq > 0: 
						next_pair_count[fromLetter][insertLetter] += freq
						next_pair_count[fromLetter][toLetter] -= freq
						next_pair_count[insertLetter][toLetter] += freq
		pair_count = next_pair_count


	freq = collections.Counter()

	for fromLetter in pair_count.keys():
		for toLetter, num in pair_count[fromLetter].items():
			freq[fromLetter] += num
			freq[toLetter] += num
	
	for letter, f in freq.items():
		if letter == s[0] or letter == s[-1]:
			freq[letter] = (f - 1) // 2 + 1
		else:
			freq[letter] = f // 2

	
	return max(freq.values()) - min(freq.values())
	

if __name__ == "__main__":
	main()
