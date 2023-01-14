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
        print(solve(n, nums))

def solve(n, nums):
    def dfs(start, end, mn, mx):
        result = 0
        if start >= end:
            return 0
        mid = start + (end - start) // 2
        mid_num = mn + (mx - mn) // 2
        
        right_bigger = nums[end] > nums[start]
        for i in range(mid+1, end+1):
            if right_bigger and nums[i] <= mid_num:
                return math.inf
            if not right_bigger and nums[i] > mid_num:
                return math.inf
        if right_bigger:
            result += dfs(start, mid, mn, mid_num)
            result += dfs(mid+1, end, mid_num+1, mx)
            return result
        else:
            result += dfs(start, mid, mid_num+1, mx)
            result += dfs(mid+1, end, mn, mid_num)
            return result + 1
    result = dfs(0, n-1, 1, n)
    if result == math.inf:
        return -1
    return result






if __name__ == "__main__":
    main()
