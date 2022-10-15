from functools import lru_cache as cache
from collections import Counter, defaultdict
import math
import bisect
from heapq import *
# from sortedcontainers import SortedSet, SortedList, SortedDict

import sys
def get_int(): return int(input())
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_list(): return list(map(int, sys.stdin.readline().strip().split()))
def get_string(): return sys.stdin.readline().strip()

def main():
    testcases = get_int()
    for tc in range(testcases):
        n = get_int()
        solve(n)

def solve(n):
    for floor in range(1, n+1):
        torches = [0 for i in range(floor)]
        torches[0], torches[-1] = 1, 1
        print(" ".join(map(str, torches)))
            
            
            

if __name__ == "__main__":
    main()

