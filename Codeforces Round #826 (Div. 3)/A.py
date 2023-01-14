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
        ss = get_str()
        a, b = ss.split()
        print(solve(a, b))

def solve(a, b):
    # "S", "M", "L"
    if a[-1] < b[-1]:
        return ">"
    if a[-1] > b[-1]:
        return "<"
    if a[-1] == "S":
        if len(a) > len(b):
            return "<"
        if len(a) < len(b):
            return ">"
    if a[-1] == "L":
        if len(a) > len(b):
            return ">"
        if len(a) < len(b):
            return "<"
    return "="

if __name__ == "__main__":
    main()
