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
        a = get_list()
        print(solve(a, n))

def solve(a, n):
    result = [1 for i in range(n)]
    for i in range(n-1):
        if a[i+1] - a[i] < 0:
            result[a[i]-1] = (i+1) + 1 # +1 due to 1-index
    return " ".join(map(str, result))




if __name__ == "__main__":
    main()
