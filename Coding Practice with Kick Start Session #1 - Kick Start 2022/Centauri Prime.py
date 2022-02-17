from functools import lru_cache as cache
from collections import Counter
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
		kingdom = get_string()
		print(f"Case #{i + 1}: {solve(kingdom)}")


def solve(kingdom):
	if kingdom[-1] in "UEOAIueoai":
		return f"{kingdom} is ruled by Alice."
	elif kingdom[-1] in "yY":
		return f"{kingdom} is ruled by nobody."
	else:
		return f"{kingdom} is ruled by Bob."

if __name__ == "__main__":
	main()