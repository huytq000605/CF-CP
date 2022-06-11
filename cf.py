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
        s = get_string()
        p = get_list()
        print(solve(n, s, p))

def solve(n, s, p):
    count = [0 for i in range(n)]
    done = set()
    for i in range(n):
        current = set()
        if i in done:
            continue
        ori = p[i] - 1
        cur = p[i] - 1
        current.add(i)
        current.add(cur)
        done.add(cur)
        while cur != i:
            print(i, cur)
            cur = p[i] - 1
            current.add(cur)
            done.add(cur)
        for idx in current:
            count[idx] = len(current)

    result = 1
    for i in range(n):
        result = lcm(result, count[i])
    return result
        
def lcm(a, b):
    return a*b / gcd(a, b)

def gcd(a, b):
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    return gcd(b, a % b)


if __name__ == "__main__":
    main()
