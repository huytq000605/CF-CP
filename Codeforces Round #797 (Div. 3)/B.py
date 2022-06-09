from functools import lru_cache as cache
from collections import Counter, defaultdict
import math
from heapq import *

import sys
def get_int(): return int(input())
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_list(): return list(map(int, sys.stdin.readline().strip().split()))
def get_string(): return sys.stdin.readline().strip()

def main():
    testcases = get_int()
    for i in range(testcases):
        n = get_int()
        a = get_list()
        b = get_list()
        print(solve(a, b, n))


def solve(a, b, n):
    max_changes = max([a[i] - b[i] for i in range(n)])

    for i in range(n):
        if b[i] > a[i]:
            return "NO"
        changes = a[i] - b[i]
        if b[i] != 0 and changes < max_changes:
            return "NO"
    return "YES"




if __name__ == "__main__":
    main()
