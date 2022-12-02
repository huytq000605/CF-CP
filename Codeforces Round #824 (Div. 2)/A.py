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
        print(solve(n))


def solve(n):
    # l1 = 1
    # l2 = (n - 3) // 3
    # l3 = n-3 - l2 - l1
    l1 = 1
    l2 = (n-3) // 3
    l3 = n-3 - l2 - l1
    return min(l2 - l1, l3 - l2)



if __name__ == "__main__":
    main()

