from functools import lru_cache
from collections import Counter, defaultdict
import math
from heapq import *
from sortedcontainers import SortedSet, SortedList, SortedDict

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
        print(solve(nums, n))



def solve(nums, n):
    seen = dict()
    result = -1
    for i, num in enumerate(nums):
        if num in seen:
            result = max(result, seen[num] + (n - i))
        seen[num] = i
    return result



if __name__ == "__main__":
    main()
