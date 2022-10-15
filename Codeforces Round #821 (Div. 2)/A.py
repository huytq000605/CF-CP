from functools import lru_cache as cache
from collections import Counter, defaultdict
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
        n, k = get_ints()
        nums = get_list()
        print(solve(nums, k, n))


def solve(nums, k, n):
    max_num = [0 for i in range(k)]
    for i, num in enumerate(nums):
        max_num[i%k] = max(max_num[i%k], num)
    return sum(max_num)


if __name__ == "__main__":
    main()
