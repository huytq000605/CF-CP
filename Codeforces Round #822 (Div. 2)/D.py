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
        n, k = get_ints()
        a = get_list()
        k = k-1
        print(solve(a, n, k))


def solve(a, n, k):
    left, right = deque(), deque()
    cur, worst = 0, 0
    for i in range(k-1, -1, -1):
        cur += a[i]
        worst = min(worst, cur)
        if cur >= 0:
            left.appendleft((cur, worst))
            cur, worst = 0, 0
    left.appendleft((cur, worst))

    cur, worst = 0, 0
    for i in range(k+1, n):
        cur += a[i]
        worst = min(worst, cur)
        if cur >= 0:
            right.append((cur, worst))
            cur, worst = 0, 0
    right.append((cur, worst))

    cur = a[k]
    while left and right:
        acted = False
        if -left[-1][1] <= cur:
            acted = True
            cur += left.pop()[0]

        if -right[0][1] <= cur:
            acted = True
            cur += right.popleft()[0]

        if not acted:
            return "NO"


    

    return "YES"

if __name__ == "__main__":
    main()

