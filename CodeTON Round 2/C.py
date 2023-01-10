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
        n, m = get_ints()
        infected = list(map(lambda e: e - 1, get_list()))
        print(solve(n, m, infected))

def solve(n, m, infected):
    infected.sort()
    intervals = []
    first_last = infected[0] + (n - 1 - infected[-1])
    heappush(intervals, -first_last)
    for i in range(m-1):
        heappush(intervals, infected[i] - infected[i+1] + 1)
    turns = 0
    non_infected = 0
    while intervals:
        d = -heappop(intervals)
        d -= turns * 2
        if d <= 0:
            break
        non_infected += d - 1 if d > 1 else 1 # Edge case: interval = [a, a]
        turns += 2
    return n - non_infected



if __name__ == "__main__":
    main()
