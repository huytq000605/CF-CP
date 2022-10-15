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
        n, x, y = get_ints()
        a = get_string()
        b = get_string()
        print(solve(n, x, y, a, b))

def solve(n, x, y, a, b):
    diffs = []
    for i in range(n):
        if a[i] != b[i]:
            diffs.append(i)
    if len(diffs) % 2 == 1:
        return -1
    if x >= y:
        return solve1(x, y, diffs)
    else:
        return solve2(x, y, diffs)

def solve1(x, y, diffs):
    if len(diffs) == 2 and diffs[0] + 1 == diffs[1]:
        return min(x, y*2)
    return y * len(diffs) // 2
        
def solve2(x, y, diffs):
    m = len(diffs)
    @cache(None)
    def dfs(i, drop):
        if i >= m:
            if drop == 0:
                return 0
            return math.inf
        result = dfs(i+1, drop+1)
        if drop:
            result = min(result, dfs(i+1, drop-1) + y)
        if i < m-1:
            result = min(result, dfs(i+2, drop) + min(y, x * (diffs[i+1] - diffs[i])))
        return result
    return dfs(0, 0)


if __name__ == "__main__":
    main()

