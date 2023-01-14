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
        n = get_int()
        b = get_list()
        print(solve(n, b))
 
def solve(n, b):
    dp = [0 for i in range(n)]
 
    for i in range(n):
        if (i == 0 or dp[i-1] == True) and i + b[i] < n:
            dp[i + b[i]] = 1
        if i - b[i] - 1 == -1 or (i - b[i] - 1 >= 0 and dp[i - b[i] - 1]):
            dp[i] = 1
    if dp[-1]:
        return "YES"
    return "NO"
 
 
 
if __name__ == "__main__":
    main()
