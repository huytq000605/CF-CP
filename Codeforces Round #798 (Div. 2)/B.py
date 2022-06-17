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
        print(solve(a, n))


def solve(p, n):
    if n == 1:
        return -1
    q = sorted(p)
    for i in range(n):
        if p[i] == q[i]:
            if i+1 < n:
                q[i], q[i+1] = q[i+1], q[i]
            else:
                q[i], q[i-1] = q[i-1], q[i]
    return " ".join(map(str, q))

if __name__ == "__main__":
    main()
