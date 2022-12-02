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
        print(solve(n, a))



def solve(n, a):
    # a[0] must be the minimum

    # prove why a[0] will always be achiveable
    # If a[i] >= 2 * a[0]:
    #   Cut 2 * a[0] - 1 from a[i]
    #   If that makes the last part < a[0]
    #   That means before doing the last cut, the remaining value
    #   is in the range [2 * a[0], 3 * a[0] - 2]
    #   So we can always do the last cut differently to make it satisfy
    
    # if x < a[0]: That makes us need to cut more than a[0]
    result = 0
    for num in a:
        result += (num-1) // (2 * a[0] - 1)
    return result






if __name__ == "__main__":
    main()

