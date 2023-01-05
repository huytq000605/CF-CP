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
def get_string(): return sys.stdin.readline().strip()
 
def main():
    n = get_int()
    a = get_list()
    q = get_int()
    queries = []
    for i in range(q):
        p, x = get_ints()
        queries.append((p, -x, i))
    queries.sort()
    solve(n, a, queries)

def solve(n, a, queries):
    dp = [0 for i in range(n)]
    dp[0] = 1
    prefix = [0 for i in range(n)]
    suffix = [0 for i in range(n+5)]
    for i, x in enumerate(a):
        dp[i] = min(dp[i-1] + 1, x)
        if i > 0:
            prefix[i] = prefix[i-1]
        prefix[i] += dp[i]
    for i in range(n-1, -1, -1):
        if i < n-1:
            suffix[i] = suffix[i+1]
        suffix[i] += dp[i]
    print(dp)
    print(suffix)
    result = [0 for i in range(len(queries))]
    lowest_idx_not_affected = 0
    for p, x, i  in queries:
        x = -x
        res = 0
        p = p-1
        # find lowest index (>p) satisfy new_dp[i] 
        lowest_idx_not_affected = max(lowest_idx_not_affected, p + 1)
        new_dp = x
        if p > 0:
            res += prefix[p-1]
            new_dp = min(new_dp, dp[p-1]+1)
        new_dp_p = new_dp
        while lowest_idx_not_affected < n:
            new_dp = min(a[lowest_idx_not_affected], new_dp + 1) 
            if new_dp >= a[lowest_idx_not_affected]:
                break
            lowest_idx_not_affected += 1
        print(a, p, x, lowest_idx_not_affected)


        no_of_num = lowest_idx_not_affected - p
        print(no_of_num)
        print(new_dp_p)
        print(res)
        res += no_of_num * (no_of_num - 1) // 2
        res += new_dp_p * no_of_num
        res += suffix[lowest_idx_not_affected]
        result[i] = res

    for res in result:
        print(res)


if __name__ == "__main__":
    main()
