from functools import lru_cache
from collections import Counter, defaultdict
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
    start, end = 3, 10**18
    while start < end:
        mid = start + math.ceil((end - start + 1) / 2)
        print(f"? {start} {mid}")
        l = get_int()
        if l == 0:
            return 0
        elif l == -1:
            end = mid - 1
        else:
            start = l
    print(f"! {start}")




if __name__ == "__main__":
    main()
