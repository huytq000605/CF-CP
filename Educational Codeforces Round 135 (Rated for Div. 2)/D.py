from functools import lru_cache as cache
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
    testcases = get_int()
    for tc in range(testcases):
        s = get_string()
        print(solve(s))

def solve(s):
    n = len(s)
    skip = 0
    draw = True

    for i in range(n // 2):
        if s[i] != s[n-1-i]:
            draw = False
            break
        else:
            skip += 1
    if draw:
        return "Draw"
    for i in range(skip, n-skip, 2):
        if s[i] != s[i+1]:
            return "Alice"
    return "Draw"

if __name__ == "__main__":
    main()
