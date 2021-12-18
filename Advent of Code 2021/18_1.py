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
	arr = None
	for i, line in enumerate(lines):
		if arr == None:
			arr = to_array(line)
		else:
			for i, (num, level) in enumerate(arr):
				arr[i] = [num, level + 1]
			line = to_array(line)
			for i, (num, level) in enumerate(line):
				line[i] = [num, level + 1]
			arr = arr + line
			arr = handle_arr(arr)
	for target_level in range(4, 0, -1):
		arr = magnitude(arr, target_level)
	return arr[0][0]
	
if __name__ == "__main__":
	main()
