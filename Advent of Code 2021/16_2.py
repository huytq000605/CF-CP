import sys
import collections
from functools import lru_cache
from typing import *
import math
import copy
import itertools
from heapq import heappush, heappop
def get_int(): return int(input())
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_list(): return list(map(int, sys.stdin.readline().strip().split()))
def get_string(): return sys.stdin.readline().strip()

class Node:
	def __init__(self, val):
		self.val = val
		self.next = None

def main():
	decode = {
	"0": "0000",
	"1": "0001",
	"2": "0010",
	"3": "0011",
	"4": "0100",
	"5": "0101",
	"6": "0110",
	"7": "0111",
	"8": "1000",
	"9": "1001",
	"A": "1010",
	"B": "1011",
	"C": "1100",
	"D": "1101",
	"E": "1110",
	"F": "1111"
	}
	lines = sys.stdin.read().splitlines()
	for line in lines:
		s = ""
		for l in line:
			s += decode[l]
	print("RESULT", solve(s))

class BreakOutException(Exception):
	pass


def solve(packet):
	def bin_to_dec(s):
		n = len(s)
		dec = 0
		for i in range(n-1, -1, -1):
			if s[i] == "1":
				dec += 1 << (n - 1 - i)
		return dec

	def decode(idx):
		startIndex = idx
		version_number = bin_to_dec(packet[idx: idx + 3])
		idx += 3
		type_id = bin_to_dec(packet[idx: idx + 3])
		idx += 3
		if type_id == 4: # Literal Value
			loop = True
			s = ""
			while loop:
				if packet[idx] == "0":
					loop = False
				idx += 1
				s += packet[idx:idx + 4]
				idx += 4
			result = bin_to_dec(s)
		else: # Operator
			length_type_id = packet[idx]
			idx += 1
			arr = []
			if length_type_id == "0":
				total_length = bin_to_dec(packet[idx: idx + 15])
				idx += 15
				endIdx = total_length + idx
				while idx < endIdx:
					length, result = decode(idx)
					arr.append(result)
					idx += length
			else:
				number_of_subpackets = bin_to_dec(packet[idx: idx + 11])
				idx += 11
				while number_of_subpackets > 0:
					length, result = decode(idx)
					arr.append(result)
					idx += length
					number_of_subpackets -= 1
		if type_id == 0:
			result = sum(arr)
		elif type_id == 1:
			product = 1
			for num in arr:
				product *= num
			result = product
		elif type_id == 2:
			result = min(arr)
		elif type_id == 3:
			result =  max(arr)
		elif type_id == 5:
			result = 1 if arr[0] > arr[1] else 0
		elif type_id == 6:
			result =  1 if arr[0] < arr[1] else 0
		elif type_id == 7:
			result =  1 if arr[0] == arr[1] else 0 
		return idx - startIndex, result
	
	_, result = decode(0)
	return result

				


if __name__ == "__main__":
	main()
