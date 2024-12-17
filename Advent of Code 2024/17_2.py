import sys
from functools import lru_cache as cache
from collections import Counter, defaultdict, deque
import math
import bisect
import math
import copy
import itertools
from heapq import heappush, heappop
import json
import re
from copy import copy, deepcopy
def get_int(): return int(input())
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_list(): return list(map(int, sys.stdin.readline().strip().split()))
def get_string(): return sys.stdin.readline().strip()


class BreakOutException(Exception):
		pass

def main():
		# lines = sys.stdin.read().splitlines()
		input();
		input();
		input();
		input()
		g = list(map(int, get_string()[8:].split(",")))
		def solve( p, r ):
				if p < 0:
						print( r )
						return True
				for d in range( 8 ):
						a, i = r << 3 | d, 0
						while i < len( g ):
								if   g[ i + 1 ] <= 3: o = g[ i + 1 ]
								elif g[ i + 1 ] == 4: o = a
								elif g[ i + 1 ] == 5: o = b
								elif g[ i + 1 ] == 6: o = c
								if   g[ i ] == 0: a >>= o
								elif g[ i ] == 1: b  ^= g[ i + 1 ]
								elif g[ i ] == 2: b   = o & 7
								elif g[ i ] == 3: i   = g[ i + 1 ] - 2 if a != 0 else i
								elif g[ i ] == 4: b  ^= c
								elif g[ i ] == 5: w   = o & 7; break
								elif g[ i ] == 6: b   = a >> o
								elif g[ i ] == 7: c   = a >> o
								i += 2
						if w == g[ p ] and solve( p - 1, r << 3 | d ):
								return True
				return False  
		
		solve( len( g ) - 1, 0 )  



if __name__ == "__main__":
		main()



