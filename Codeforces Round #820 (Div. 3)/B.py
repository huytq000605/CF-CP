from functools import lru_cache
from collections import Counter, defaultdict
import math
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
        s = get_string()
        print(solve(s, n))



def solve(s, n):
    i = n-1
    result = ""
    while i >= 0:
        if s[i] == "0":
            kth = int(s[i-2:i])
            result += chr(kth + ord('a') - 1)
            i = i-3
        else:
            kth = int(s[i])
            result += chr(kth + ord('a') - 1)
            i -= 1
    return result[::-1]
        



if __name__ == "__main__":
    main()
