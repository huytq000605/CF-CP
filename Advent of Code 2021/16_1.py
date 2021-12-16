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
	print("original packet length", len(packet))
	def bin_to_dec(s):
		n = len(s)
		dec = 0
		for i in range(n-1, -1, -1):
			if s[i] == "1":
				dec += 1 << (n - 1 - i)
		return dec

	version_nums = 0

	def decode(idx):
		startIndex = idx
		nonlocal version_nums
		version_number = bin_to_dec(packet[idx: idx + 3])
		version_nums += version_number
		idx += 3
		type_id = packet[idx: idx + 3]
		idx += 3
		if type_id == "100": # Literal Value
			loop = True
			s = ""
			while loop:
				if packet[idx] == "0":
					loop = False
				idx += 1
				s += packet[idx:idx + 4]
				idx += 4
		else: # Operator
			length_type_id = packet[idx]
			idx += 1
			if length_type_id == "0":
				total_length = bin_to_dec(packet[idx: idx + 15])
				idx += 15
				endIdx = total_length + idx
				while idx < endIdx:
					idx += decode(idx)
			else:
				number_of_subpackets = bin_to_dec(packet[idx: idx + 11])
				idx += 11
				while number_of_subpackets > 0:
					idx += decode(idx)
					number_of_subpackets -= 1
		return idx - startIndex
	
	decode(0)
	return version_nums

				
if __name__ == "__main__":
	main()
