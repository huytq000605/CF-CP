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
        nums = get_list()
        print(solve(nums, n))


def solve(nums, n):
    total = sum(nums) - n
    if total % 2:
        return "errorgorn"
    else:
        return "maomao90"

if __name__ == "__main__":
    main()
