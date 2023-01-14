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

def main():
    testcases = get_int()
    for _ in range(testcases):
        n, m = get_ints()
        graph = [[] for _ in range(n)]
        for _ in range(m):
            u, v = get_ints()
            u -= 1
            v -= 1
            graph[u].append(v)
            graph[v].append(u)
        f = get_int()
        h = list(map(lambda i: i - 1, get_list()))
        k = get_int()
        ks = sorted(map(lambda i: i-1, get_list()))
        print(solve(graph, n, f, h, k, ks))



def solve(graph, n, f, h, k, ks):
    dq = deque([0])
    # shorest distance
    dist = [-1 for _ in range(n)]
    dist[0] = 0

    seen_masks = [set() for _ in range(n)]
    seen_masks[0] = set([0])

    vertice_masks = [0 for _ in range(n)]
    for i, friend in enumerate(ks):
        house = h[friend]
        vertice_masks[house] |= (1<<i)

    while dq:
        u = dq.popleft()
        for v in graph[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                dq.append(v)
            if dist[v] == dist[u] + 1:
                for mask in seen_masks[u]:
                    seen_masks[v].add(mask | vertice_masks[v])

    can = set([0])
    j = 0
    for friend in range(f):
        if j < k and friend == ks[j]:
            j += 1
            continue
        house = h[friend]
        new = set()
        
        for seen_mask in seen_masks[house]:
            for already_can in can:
                new.add(already_can | seen_mask)

        can.update(new)

    result = k
    for mask in can:
        walk = 0
        for i in range(k):
            if mask & (1<<i) == 0:
                walk += 1
        result = min(result, walk)
    return result

if __name__ == "__main__":
    main()
