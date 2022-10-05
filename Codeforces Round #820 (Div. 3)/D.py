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
    testcases = get_int()
    for tc in range(testcases):
        n = get_int()
        x = get_list()
        y = get_list()
        print(solve(n, x, y))



def solve(n, x, y):
    a = [y[i] - x[i] for i in range(n)]
    a.sort(reverse = True)
    i, j = 0, n-1
    result = 0
    while i < j:
        if a[i] < 0:
            break

        while j > i and a[i] + a[j] < 0:
            j -= 1

        if j == i:
            break
        
        i += 1
        j -= 1
        result += 1
    return result

            


        



if __name__ == "__main__":
    main()
