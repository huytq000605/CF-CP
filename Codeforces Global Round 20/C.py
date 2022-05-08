from functools import lru_cache as cache
from collections import Counter
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
        arr = get_list()
        print(solve(arr, n))


def solve(arr, n):
    equals = []
    for i in range(n-1):
        if arr[i] == arr[i+1]:
            equals.append(i)
    if len(equals) <= 1:
        return 0
    equals.sort()
    m = len(equals)
    if m == 2:
        if equals[1] - equals[0] == 1:
            return 1
        else:
            return equals[1] - equals[0] - 1
    result = min(equals[m//2] - equals[0] + equals[-1] - equals[m//2],
            equals[m//2+1] - equals[0] + equals[-1] - equals[m//2+1]) - 1
    return result


if __name__ == "__main__":
    main()