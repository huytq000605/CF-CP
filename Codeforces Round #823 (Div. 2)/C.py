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
        s = get_string()
        print(solve(s))
 
def solve(s):
    counter = Counter()
    n = len(s)
    stack = []
    for i in range(n-1, -1, -1):
        c = int(s[i])
        if not stack or c <= stack[-1]:
            stack.append(c)
        else:
            counter[min(c+1, 9)] += 1
    for num in stack:
        counter[num] += 1
    result = ""
    for i in range(10):
        result += str(i) * counter[i]
    return result
        

 
if __name__ == "__main__":
    main()
