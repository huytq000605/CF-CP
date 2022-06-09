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
        arrival = get_list()
        finished = get_list()
        print(solve(arrival, finished, n))


def solve(arrival, finished, n):
    result = []
    current = 0
    for i in range(n):
        current = max(current, arrival[i])
        result.append(finished[i] - current)
        current = finished[i]
    return " ".join(map(str, result))


if __name__ == "__main__":
    main()
