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
        a, b, c = get_ints()
        print(solve(a, b, c))



def solve(a, b, c):
    first = a
    second = abs(b-c) + c
    if first < second:
        return 1
    elif first > second:
        return 2
    else:
        return 3



if __name__ == "__main__":
    main()
