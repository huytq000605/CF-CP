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
        nums = get_list()
        print(solve(nums, n))

def solve(nums, n):
    result = n
    for first in range(1, n+1):
        target = sum(nums[:first])
        valid = True
        cur_len = 0
        cur = 0
        res = first
        for num in nums[first:]:
            cur += num
            cur_len += 1
            if cur == target:
                res = max(cur_len, res)
                if res >= result:
                    valid = False
                    break
                cur = 0
                cur_len = 0
            elif cur > target:
                break
        if cur_len > 0:
            valid = False
        if valid:
            result = min(result, res)
    return result





if __name__ == "__main__":
    main()
