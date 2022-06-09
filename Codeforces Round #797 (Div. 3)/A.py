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
        print(solve(n))


def solve(n):
    one, two, three = 2, 1, 0
    n -= 3
    while n > 0:
        n -= 1
        one += 1
        if n > 0:
            two += 1
            n -= 1
        if n > 0:
            three += 1
            n -= 1
    return f"{two} {one} {three}"



if __name__ == "__main__":
    main()
