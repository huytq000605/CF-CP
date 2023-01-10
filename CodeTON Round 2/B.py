from functools import lru_cache as cache
from collections import Counter, defaultdict, deque
import math
import bisect
import string
from heapq import *
# from sortedcontainers import SortedSet, SortedList, SortedDict
 
import sys
def get_int(): return int(input())
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_list(): return list(map(int, sys.stdin.readline().strip().split()))
def get_str(): return sys.stdin.readline().strip()
 
def main():
    testcases = get_int()
    for _ in range(testcases):
        n, x = get_ints()
        piles = get_list()
        print(solve(n, x, piles))

def solve(n, x, piles):
    mn, mx = piles[0] - x, piles[0] + x
    result = 0
    for p in piles:
        l, r = p - x, p + x
        if r < mn or l > mx:
            mn = l
            mx = r
            result += 1
        mn = max(mn, l)
        mx = min(mx, r)
    return result



if __name__ == "__main__":
    main()
