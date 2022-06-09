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
        n, k = get_ints()
        ws = get_list()
        print(solve(ws, n, k))


def solve(ws, n, k):
    result = 0
    for i in range(n):
        result += ws[i] // k
        ws[i] %= k
    i, j = 0, n - 1
    ws.sort()
    while i < j:
        if ws[i] + ws[j] == k:
            result += 1
            i += 1
            j -= 1
        elif ws[i] + ws[j] < k:
            i += 1
        else:
            i += 1
            j -= 1
            result += 1
    return result


if __name__ == "__main__":
    main()
