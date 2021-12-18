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
	print(solve(lines))

class BreakOutException(Exception):
	pass

def to_array(s):
	arr = []
	level = 0
	for l in s:
		if l == "[":
			level += 1
		elif l == "]":
			level -= 1
		elif l == ",":
			continue
		else:
			arr.append([int(l), level])
	return arr

def explodes(arr):
	i = 0
	modify = False
	while i < len(arr):
		num, level = arr[i]
		if level > 4:
			modify = True
			if i > 0:
				arr[i-1][0] += arr[i][0]
			if i < len(arr) - 2:
				arr[i+2][0] += arr[i+1][0]
			arr = arr[:i] + [[0, level - 1]] + arr[i+2:]
			break
		i += 1
	
	return modify, arr

def splits(arr):
	i = 0
	modify = False
	while i < len(arr):
		num, level = arr[i]
		if num >= 10:
			modify = True
			arr = arr[:i] + [[num // 2, level + 1]] + [[num - num // 2, level + 1]] + arr[i+1:]
			break
		i += 1

	return modify, arr

def handle_arr(arr):
	while True:
		modify, newArr = explodes(arr)
		if modify:
			arr = newArr
			continue
		modify, newArr = splits(arr)
		if modify:
			arr = newArr
			continue
		break
	return arr

def magnitude(arr, target_level):
	i = 0
	while i < len(arr):
		num, level = arr[i]
		if level == target_level:
			arr = arr[:i] + [[arr[i][0] * 3 + arr[i+1][0] * 2, level - 1]] + arr[i+2:]
			i -= 1
		i += 1
	return arr



def solve(lines):
	biggest = 0
	for i, line1 in enumerate(lines):
		ori = line1
		for j, line2 in enumerate(lines):
			line1 = ori
			if i == j:
				continue
			line1 = to_array(line1)
			line2 = to_array(line2)
			for k, (num, level) in enumerate(line1):
				line1[k] = [num, level + 1]
			for k, (num, level) in enumerate(line2):
				line2[k] = [num, level + 1]
			arr = handle_arr(line1 + line2)
			for target_level in range(4, 0, -1):
				arr = magnitude(arr, target_level)
			biggest = max(biggest, arr[0][0])
			
	return biggest
	
if __name__ == "__main__":
	main()
