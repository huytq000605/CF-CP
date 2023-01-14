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
        print(solve(n))

def solve(n):
    if n == 3:
        return -1
    if n == 2:
        return "2 1"
    result = [i for i in range(3, n+1)]
    result += [2, 1]
    return " ".join(map(str, result))



if __name__ == "__main__":
    main()
