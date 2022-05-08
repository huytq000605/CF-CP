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
        a1 = get_list()
        a2 = get_list()
        print(solve(a1, a2, n))


def solve(a1, a2, n):
    later = defaultdict(int)
    i1, i2 = n-1, n-1
    while i1 >= 0 and i2 >= 0:
        if a1[i1] == a2[i2]:
            i1 -= 1
            i2 -= 1
        else:
            if i2 + 1 < n and a2[i2] == a2[i2 + 1]:
                later[a2[i2]] += 1
                i2 -= 1
            elif a1[i1] in later:
                later[a1[i1]] -= 1
                if later[a1[i1]] == 0:
                    later.pop(a1[i1])
                i1 -= 1
            else:
                return "NO"
    return "YES"


if __name__ == "__main__":
    main()