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
        d = get_list()
        solve(n, d)


def solve(n, d):
    result = []
    cur = 0
    for num in d:
        if cur - num >= 0 and num != 0:
            print(-1)
            return
        else:
            cur += num
            result.append(cur)
    print(" ".join(map(str, result)))



if __name__ == "__main__":
    main()

