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
def get_string(): return sys.stdin.readline().strip()
 
def main():
    testcases = get_int()
    for tc in range(testcases):
        n = get_int()
        a = get_list()
        print(solve(a, n))

def solve(a, n):
    start = 0
    result = 0
    for i, num in enumerate(a):
        while num <= (i - start):
            start += 1
        result += (i - start + 1)
    return result


if __name__ == "__main__":
    main()
