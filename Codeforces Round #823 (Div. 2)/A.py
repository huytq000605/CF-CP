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
        n, c = get_ints()
        a = get_list()
        print(solve(a, n, c))
 
def solve(a, n, c):
    counter = Counter(a)
    result = 0
    for orbit, freq in counter.items():
        if c < freq:
            result += c
        else:
            result += freq
    return result

    
 
if __name__ == "__main__":
    main()
 

