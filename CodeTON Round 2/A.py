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
        n, m = get_ints()
        a = get_str()
        b = get_str()
        if solve(a, b, n, m):
            print("YES")
        else:
            print("NO")

def solve(a, b, n, m):
    if n < m:
        return False
    while m > 1:
        if a[n-1-(len(b)-m)] != b[m-1]:
            return False
        m -= 1
    for i in range(n-len(b)+1):
        if a[i] == b[0]:
            return True
    return False


if __name__ == "__main__":
    main()
