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
        a = get_list()
        b = get_list()
        print(solve(a, b, n))


def solve(a, b, n):
    result = 0
    pqa, pqb = [], []
    for num in a: heappush(pqa, -num)
    for num in b: heappush(pqb, -num)
    while pqa:
        x, y = heappop(pqa), heappop(pqb)
        if x == y:
            continue
        elif -x > -y:
            heappush(pqb, y)
            x = -math.floor(math.log10(-x) + 1)
            heappush(pqa, x)
        else:
            heappush(pqa, x)
            y = -math.floor(math.log10(-y) + 1)
            heappush(pqb, y)
        result += 1
    return result




if __name__ == "__main__":
    main()
