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
        n, m = get_ints()
        solve(n, m)


def solve(n, m):
    ds = [(-1, 2), (1, 2), (-1, -2), (1, -2), (-2, 1), (-2, 1), (2, -1), (2, 1)]
    for r in range(n):
        for c in range(m):
            valid = False
            for dr, dc in ds:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < m:
                    valid = True
                    break
            if not valid:
                print(f"{r+1} {c+1}")
                return
    print("1 1")


if __name__ == "__main__":
    main()

