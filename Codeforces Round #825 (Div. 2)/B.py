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
def get_string(): return sys.stdin.readline().strip()
 
def main():
    testcases = get_int()
    for tc in range(testcases):
        n = get_int()
        a = get_list()
        print(solve(n, a))

def lcm(a, b):
    return a * b // math.gcd(a, b)

def solve(n, a):
    # math.gcd(b[i], b[i+1]) = a[i]
    # math.gcd(b[i+1], b[i+2]) = a[i+1]
    # b[i] % a[i] == 0
    # b[i] % a[i-1] == 0
    b = [0 for i in range(n+1)]
    for i in range(1, n):
        b[i] = lcm(a[i-1], a[i])
    b[0] = a[0]
    b[-1] = a[-1]
    for i in range(n):
        if math.gcd(b[i], b[i+1]) != a[i]:
            return "NO"
    return "YES"


if __name__ == "__main__":
    main()
