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
        n = get_int()
        nums = get_list()
        solve(nums, n)


def solve(nums, n):
    if n == 1:
        print(0)
        return
    if (nums[0] + nums[-1]) % 2 == 0:
        nums[0] = nums[-1]
    else:
        nums[-1] = nums[0]
    ops = [(1, n)]
    for i in range(1, n-1):
        if (nums[i] + nums[0]) % 2 == 0:
            ops.append((i+1, n))
        else:
            ops.append((1, i+1))
    print(len(ops))
    for l, r in ops:
        print(l, r)


if __name__ == "__main__":
    main()
