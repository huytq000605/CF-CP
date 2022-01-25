from functools import lru_cache as cache
import math
from heapq import *

import sys
def get_int(): return int(input())
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_list(): return list(map(int, sys.stdin.readline().strip().split()))
def get_string(): return sys.stdin.readline().strip()

def main():
	testcases = get_int()
	for i in range(testcases):
		a,b,c = get_ints()
		if solve(a,b,c):
			print("YES")
		else:
			print("NO")


def solve(a,b,c):
	if (b+(b-a)) > 0 and (b+(b-a)) % c == 0:
		return True
	if (b-(c-b)) > 0 and (b-(c-b)) % a == 0:
		return True
	if c < a:
		a, c = c, a
	if (c-a) % 2 == 0 and (a+(c-a)//2) > 0 and (a+(c-a)//2) % b == 0:
		return True
	return False
	
if __name__ == "__main__":
	main()