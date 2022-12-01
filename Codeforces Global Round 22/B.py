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
        n, k = get_ints()
        prefix = get_list()
        print(solve(n, k, prefix))
 
def solve(n, k, prefix):
    prev = math.inf
    for i in range(k-1, 0, -1):
        num = prefix[i] - prefix[i-1]
        if num > prev:
            return "No"
        prev = num
    if n == k:
        if prefix[0] > prev:
            return "NO"
    if n > k:
        if prev * (n-k+1) >= prefix[0]:
            return "YES"
        return "NO"
    return "YES"


 
if __name__ == "__main__":
    main()
