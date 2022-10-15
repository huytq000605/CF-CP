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
        sticks = get_list()
        print(solve(sticks, n))

def solve(sticks, n):
    sticks.sort()
    result = math.inf
    for i in range(1, n-1):
        result = min(sticks[i] - sticks[i-1] + sticks[i+1] - sticks[i], result)
    return result

if __name__ == "__main__":
    main()

