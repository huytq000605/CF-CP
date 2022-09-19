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
    testcases = get_int()
    for tc in range(testcases):
        n = get_int()
        balls = get_list()
        print(solve(balls, n))



def solve(balls, n):
    t, remain = 0, 0
    for i, num in enumerate(balls):
        color = i + 1
        if remain < num:
            t = color
            remain = num - remain
        else:
            remain -= num
    return t



if __name__ == "__main__":
    main()
