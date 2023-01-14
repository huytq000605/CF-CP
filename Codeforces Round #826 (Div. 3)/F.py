from functools import lru_cache as cache
from collections import Counter, defaultdict, deque
import math
import bisect
import string
from heapq import *
# from sortedcontainers import SortedSet, SortedList, SortedDict
 
import sys
def get_int(): return int(input())
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_list(): return list(map(int, sys.stdin.readline().strip().split()))
def get_str(): return sys.stdin.readline().strip()

def main():
    testcases = get_int()
    for _ in range(testcases):
        n = get_int()
        intervals = []
        for _ in range(n):
            l, r, c = get_ints()
            intervals.append((l, r, c))
        print(solve(n, intervals))


def solve(n, intervals):
    result = [math.inf for i in range(n)]
    test = []

    intervals = sorted([(l, r, c, i) for i, (l, r, c) in enumerate(intervals)])
    seen = [[-1, -1], [-2, -1]]
    for l, r, c, i in intervals:
        if seen[0][1] != -1 and seen[0][1] != c:
            result[i] = min(result[i], max(0, l - seen[0][0]))
        if seen[1][1] != -1 and seen[1][1] != c:
            result[i] = min(result[i], max(0, l - seen[1][0]))

        if seen[0][1] == c:
            seen[0][0] = max(seen[0][0], r)
        elif seen[1][1] == c:
            seen[1][0] = max(seen[1][0], r)
        elif seen[0][0] <= seen[1][0] and seen[0][0] < r:
            seen[0] = [r, c]
        elif  seen[0][0] > seen[1][0] and seen[1][0] < r:
            seen[1] = [r, c]

    seen = [[10**10, -1], [10**11, -1]]
    for l, r, c, i in reversed(intervals):
        if seen[0][1] != -1 and seen[0][1] != c:
            result[i] = min(result[i], max(0, seen[0][0] - r))
        if seen[1][1] != -1 and seen[1][1] != c:
            result[i] = min(result[i], max(0, seen[1][0] - r))


        if seen[0][1] == c:
            seen[0][0] = min(seen[0][0], l)
        elif seen[1][1] == c:
            seen[1][0] = min(seen[1][0], l)
        elif seen[0][0] >= seen[1][0] and seen[0][0] > l:
            seen[0] = [l, c]
        elif  seen[0][0] < seen[1][0] and seen[1][0] > l:
            seen[1] = [l, c]
    return " ".join(map(str, result))





if __name__ == "__main__":
    main()
