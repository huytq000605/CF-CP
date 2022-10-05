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
        s = get_string()
        solve(s)



def solve(s):
    n = len(s)
    a = [(ord(s[i]), i) for i in range(1, n-1)]
    a.sort()
    first, last = ord(s[0]), ord(s[-1])
    m1, m2 = min(first, last), max(first, last)
    result = [1]
    for c, i in a:
        if m1 <= c <= m2:
            result.append(i+1)
    result.append(n)
    print(m2 - m1, len(result))
    if first > last:
        result[1:len(result)-1] = result[len(result)-2:0:-1]
    print(" ".join(map(str, result)))

        



if __name__ == "__main__":
    main()
