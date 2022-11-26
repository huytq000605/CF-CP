from functools import lru_cache as cache
from collections import Counter, defaultdict, deque
import math
import bisect
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
        print(solve(n, a, b))
 
def solve(n, a, b):
    t0s = [b[i] for i in range(n) if a[i] == 0]
    t1s = [b[i] for i in range(n) if a[i] == 1]
    t0s.sort(reverse = True)
    t1s.sort(reverse = True)
    double = min(len(t0s), len(t1s))
    result = sum([t0s[i] + t1s[i] for i in range(double)]) * 2
    result += sum([t0s[i] for i in range(double, len(t0s))])
    result += sum([t1s[i] for i in range(double, len(t1s))])
    if double * 2 == n:
        result -= min(b)
    return result



 
if __name__ == "__main__":
    main()
