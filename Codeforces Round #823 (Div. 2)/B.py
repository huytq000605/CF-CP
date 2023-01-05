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
        x = get_list()
        t = get_list()
        print(solve(n, x, t))
 
def solve(n, x, t):
    start = max(t)
    end = 2*(10**8)
    def find_range(max_move):
        s1 = x[0] - (max_move - t[0])
        e1 = x[0] + (max_move - t[0])
        for i in range(1, n):
            s2 = x[i] - (max_move - t[i])
            e2 = x[i] + (max_move - t[i])
            if max(s1, s2) > min(e1, e2):
                return -1
            s1 = max(s1, s2)
            e1 = min(e1, e2)
        return (e1 + s1) / 2

    iterations = 30
    while iterations > 0:
        iterations -= 1
        mid = start + (end - start) / 2
        intersect = find_range(mid)
        if intersect != -1:
            result = intersect
            end = mid
        else:
            start = mid + 1
    return result

 
if __name__ == "__main__":
    main()
 


