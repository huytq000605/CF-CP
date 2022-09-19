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
        print(solve(n))


def solve(n):
    result = [i+1 for i in range(n)]
    if n % 2 == 0:
        for i in range(0, n-2, 2):
            result[i], result[i+1] = result[i+1], result[i]
    else:
        for i in range(3, n-2, 2):
            result[i], result[i+1] = result[i+1], result[i]
    return " ".join(map(str, result))



if __name__ == "__main__":
    main()
