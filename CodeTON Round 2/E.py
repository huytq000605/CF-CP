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
def get_str(): return sys.stdin.readline().strip()

MOD = 998244353
def main():
    testcases = get_int()
    for _ in range(testcases):
        n, m = get_ints()
        a = get_list()
        graph = [[] for _ in range(n)]
        indegree = [0 for _ in range(n)]
        for _ in range(m):
            u, v = get_ints()
            u, v = u-1, v-1
            graph[u].append(v)
            indegree[v] += 1
        print(solve(graph, indegree, n, a))

def merge_intervals(intervals):
    intervals.sort()
    merged_intervals = []
    for start_time, size in intervals:
        if not merged_intervals or start_time > merged_intervals[-1][0] + merged_intervals[-1][1]:
            merged_intervals.append([start_time, size])
        else:
            merged_intervals[-1][1] += size
            if merged_intervals[-1][1] >= MOD:
                merged_intervals[-1][1] = merged_intervals[-1][1] % MOD + MOD
    return merged_intervals



def solve(graph, indegree, n, a):
    q = deque()
    top_sorted = []
    result = 0
    for u in range(n):
        if indegree[u] == 0:
            q.append(u)
    while q:
        u = q.popleft()
        top_sorted.append(u)
        for v in graph[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                q.append(v)
    
    intervals = [[] for _ in range(n)]
    for u in range(n):
        if a[u] != 0:
            intervals[u].append([0, a[u]])
    for u in top_sorted:
        if len(intervals[u]) > 0:
            intervals[u] = merge_intervals(intervals[u])
            for v in graph[u]:
                for start_time, size in intervals[u]:
                    intervals[v].append([start_time + 1, size])
    last = top_sorted[-1]
    if len(intervals[last]) > 0:
        result = intervals[last][-1][1] + max(map(lambda e: e[0], intervals[last]))
    return result % MOD

if __name__ == "__main__":
    main()
