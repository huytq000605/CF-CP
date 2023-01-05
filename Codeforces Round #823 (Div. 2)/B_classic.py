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
        x = get_list()
        t = get_list()
        print(solve(n, x, t))
 
def solve(n, x, t):
    a = []
    # we can sure that the maximum distance from x[i] + t[i] and x[i] - t[i]
    # would still be the same with abs(x[i] - x_goal) + t[i]
    mx, mn = x[0] + t[0], x[0] + t[0]
    for i in range(n):
        mx = max(mx, x[i] + t[i])
        mn = min(mn, x[i] - t[i])

    return (mx + mn) / 2


 
if __name__ == "__main__":
    main()
 


