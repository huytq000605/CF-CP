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

"""
Even if you give lots of operation 1 to array a, the sum of (ai×i) remains. Thus, you can easily find ck.
Operaton 2 will add 1 to the result of ∑ai×i.
Just minus the initial ∑ai×i and you will get the number of operations applied.
"""
 
def main():
    testcases = get_int()
    for _ in range(testcases):
        n, m = get_ints()
        cs = []
        for _ in range(n):
            cs.append(get_list())

        idx, ops = solve(n, m, cs)
        print(idx+1, ops)

def solve(n, m, cs):
    def sum_val_idx(c):
        res = 0
        for i, num in enumerate(c):
            res += i * num
        return res
    s = [0, 0]
    for i in range(2):
        s[i] = sum_val_idx(cs[i])
    if s[0] == s[1]:
        for i in range(2, n):
            cur = sum_val_idx(cs[i])
            if cur != s[0]:
                return i, cur - s[0]
    else:
        cur = sum_val_idx(cs[2])
        if cur != s[0]:
            return 0, s[0] - s[1]
        else:
            return 1, s[1] - s[0]





if __name__ == "__main__":
    main()
