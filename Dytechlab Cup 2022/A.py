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
        n, k = get_ints()
        s = get_string()
        print(solve(n, k, s))
 
def solve(n, k, s):
    counter = [0 for i in range(26)]
    each = n // k
    for c in s:
        idx = ord(c) - ord('a')
        counter[idx] += 1
    a = [0 for i in range(k)]
    cur = k
    for c in range(26):
        cur = min(cur, counter[c])
        for i in range(cur):
            a[i] = min(a[i] + 1, each)
    result = ""
    for c in a:
        result += chr(c + ord("a"))
    return result



if __name__ == "__main__":
    main()
