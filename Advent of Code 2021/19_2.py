import sys
import collections
from functools import lru_cache
from typing import *
import math
import copy
import itertools
from heapq import heappush, heappop
import json
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
	scanners = collections.defaultdict(set)
	key = -1
	for line in lines:
		if line[0:3] == "---":
			key += 1
			continue
		if line == "":
			continue
		scanners[key].add(tuple(map(int, line.split(","))))
	print(solve(scanners))

class BreakOutException(Exception):
	pass


def solve(scanners):
	n = len(scanners)
	known_scanners = dict()
	all_beacons = set()
	for beacon in scanners[0]:
		all_beacons.add(beacon)
	known_scanners[0] = (0, 0, 0)
	known_scanners_with_beacons = dict()
	known_scanners_with_beacons[0] = scanners[0]
	scanners.pop(0)

	tried = set()

	while len(known_scanners) < n:
		print(known_scanners)
		print(len(scanners))
		try:
			for i, scanner1 in known_scanners_with_beacons.items():
				for j, scanner2 in scanners.items():
					if (i, j) in tried:
						continue
					tried.add((i, j))
					for position in itertools.permutations([0,1,2], 3):
						for sign in [(1, 1, 1), (1, 1, -1), (1, -1, 1), (1, -1, -1), (-1, 1, 1), (-1, 1, -1), (-1, -1, 1), (-1, -1, -1)]:
							copy_scanner2 = set()
							for k, beacon in enumerate(scanner2):
								copy_scanner2.add((sign[0] * beacon[position[0]], sign[1] * beacon[position[1]], sign[2] * beacon[position[2]]))
							for beacon1 in scanner1:
								for beacon2 in copy_scanner2:
									shift = tuple(beacon1[k] - beacon2[k] for k in range(3))
									tmp_scanner2 = set()
									for beacon in copy_scanner2:
										tmp_scanner2.add(tuple(beacon[l] + shift[l] for l in range(3)))
									ori_tmp_scanner2 = set(tmp_scanner2)
									for beacon in list(tmp_scanner2):
										for k in range(3):
											if abs(known_scanners[i][k] - beacon[k]) > 1000:
												tmp_scanner2.remove(beacon)
												break
									if len(scanner1 & tmp_scanner2) >= 12:
										known_scanners[j] = tuple(shift[l] for l in range(3))
										known_scanners_with_beacons[j] = ori_tmp_scanner2
										scanners.pop(j)
										all_beacons.update(ori_tmp_scanner2)
										raise BreakOutException
		except BreakOutException:
			continue
	result = 0
	for i, pos1 in known_scanners.items():
		for j, pos2 in known_scanners.items():
			if i == j:
				continue
			result = max(result, sum([abs(pos1[k] - pos2[k]) for k in range(3)]))
	print(known_scanners)
	
	return result

	
if __name__ == "__main__":
	main()
