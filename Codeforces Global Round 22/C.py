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
    even = 0
    for num in a:
        if num % 2 == 0:
            even += 1
    odd = n - even
    @cache(None)
    def dfs(odd, even, winning, aliceTurn):
        if odd == 0 and even == 0:
            return winning
        if aliceTurn:
            result = False
            if odd > 0:
                result = result or dfs(odd-1, even, not winning, False)
            if even > 0:
                result = result or dfs(odd, even-1, winning, False)
        else:
            result = True
            if odd > 0:
                result = result and dfs(odd-1, even, winning, True) 
            if even > 0:
                result = result and dfs(odd, even-1, winning, True)
        return result
    if dfs(odd, even, True, True):
        return "Alice"
    else:
        return "Bob"




 
if __name__ == "__main__":
    main()
