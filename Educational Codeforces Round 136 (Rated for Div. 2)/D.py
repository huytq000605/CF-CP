
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
        n, k = get_ints()
        ps = [-1, *list(map(lambda i: i-1, get_list()))]
        print(solve(n, k, ps))

def solve(n, k, ps):
    start = 1
    end = n
    degree = [0 for i in range(n)]
    for p in ps:
        degree[p] += 1
    leafs = [degree[i] for i in range(n) if degree[i] == 0]

    def valid(mid):
        q = deque([(leaf, 0) for leaf in leafs])
        deg = degree[:]
        depth = [0 for i in range(n)]
        times = 0
        while q:
            u, d = q.popleft()
            p = ps[u]
            if p == -1: continue
            
            nd = d + 1
            if nd == mid:
                times += 1
                if times > k:
                    return False
                nd = 0

            depth[p] = max(depth[p], nd)
            deg[p] -= 1
            if deg[p] == 0:
                q.append((p, depth[p]))
            


    while start < end:
        mid = start + (end - start) // 2
        if valid(mid):
            end = mid
        else:
            start = mid + 1
    return start
    

if __name__ == "__main__":
    main()

