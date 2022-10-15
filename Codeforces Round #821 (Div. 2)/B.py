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
        print(solve(n, x, y))



def solve(n, x, y):
    if x != 0 and y != 0:
        return -1
    y = max(x, y)
    x = 0
    if y == 0:
        return -1
    if (n-1) % y != 0:
        return -1
    result = [0 for i in range(n-1)]
    win = 0
    for i in range(n-1):
        if i % y == 0:
            win = i+2
        result[i] = win
    return " ".join(map(str, result))


if __name__ == "__main__":
    main()
