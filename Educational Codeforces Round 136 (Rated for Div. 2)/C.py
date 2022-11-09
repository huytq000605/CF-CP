from functools import lru_cache as cache
from collections import Counter, defaultdict, deque
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

def dfs(n):
    if n == 2:
        return [1, 0, 1]
    ans = dfs(n-2)
    # swap A with B after 2
    # for A to win, just take the biggest
    # for B to win, take 2 biggest
    # Continue: B take biggest, A take the remaining
    return [math.comb(n-1, n//2) + ans[1], math.comb(n-2, n//2) + ans[0], 1]

def solve(n):
    result = dfs(n)
    MOD = 998244353
    print(f"{result[0]%MOD} {result[1]%MOD} {result[2]%MOD}")
    




if __name__ == "__main__":
    main()

