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
        n, k = get_ints()
        a = get_list()
        print(solve(a))

def solve(a):
    for num in a:
        if num == 1:
            return "YES"
    return "NO"

if __name__ == "__main__":
    main()
