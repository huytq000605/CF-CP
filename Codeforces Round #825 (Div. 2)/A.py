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
        b = get_list()
        print(solve(a, b, n))
 
def solve(a, b, n):
    result = 0
    for i in range(n):
        if a[i] != b[i]:
            result += 1
    counterA = Counter(a)
    counterB = Counter(b)
    result = min(result, 1 + abs(counterA[1] - counterB[1]))
    return result




if __name__ == "__main__":
    main()
