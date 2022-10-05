from functools import lru_cache
from collections import Counter, defaultdict
import math
from heapq import *
# from sortedcontainers import SortedSet, SortedList, SortedDict

import sys
def get_int(): return int(input())
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_list(): return list(map(int, sys.stdin.readline().strip().split()))
def get_string(): return sys.stdin.readline().strip()

def main():
    # testcases = get_int()
    testcases = 1
    for tc in range(testcases):
        n, l, k = get_ints()
        signs = get_list()
        limits = get_list()
        print(solve(signs, limits, n, l, k))



def solve(signs, limits, n, l, k):
    @lru_cache(None)
    def dfs(cur, sign, k):
        if sign >= n:
            return (l - signs[cur]) * limits[cur]
        remove_sign = math.inf
        if k > 0:
            remove_sign = dfs(cur, sign + 1, k-1)
        hold_sign = (signs[sign] - signs[cur]) * limits[cur] + dfs(sign, sign + 1, k)
        result = min(remove_sign, hold_sign)
        return result
    return dfs(0, 0, k)



if __name__ == "__main__":
    main()
