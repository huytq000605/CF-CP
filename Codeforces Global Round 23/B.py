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
    ones = [0 for i in range(n+1)]
    zeros = [0 for i in range(n+1)]
    for i, num in enumerate(a):
        ones[i+1] = ones[i]
        zeros[i+1] = zeros[i]
        if num == 1: ones[i+1] += 1
        else: zeros[i+1] += 1
    if ones[-1] == 0:
        return 0
    result = zeros[-1]
    for last_zero in range(n):
        if a[last_zero] == 0:
            result = min(result, ones[last_zero] + max(0, (zeros[-1] - zeros[last_zero+1] - ones[last_zero])))
    return result


if __name__ == "__main__":
    main()
