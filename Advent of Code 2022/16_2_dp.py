import sys
from functools import lru_cache as cache
from collections import Counter, defaultdict, deque
import math
import bisect
import math
import copy
import itertools
from heapq import heappush, heappop
import json
import re
def get_int(): return int(input())
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_list(): return list(map(int, sys.stdin.readline().strip().split()))
def get_string(): return sys.stdin.readline().strip()

class BreakOutException(Exception):
    pass

def main():
    lines = sys.stdin.read().splitlines()
    flow_rate = dict()
    vertices = []
    graph = defaultdict(list)
    for line in lines:
        line = line.split(" ")
        u = line[1]
        vertices.append(u)
        flow_rate[u] = int(line[4][5:-1])
        n = len(line)
        for i in range(9, n-1):
            graph[u].append(line[i][:-1])
        graph[u].append(line[-1])

    def bfs(start, d):
        q = deque([(start, 0)])
        seen = set()
        while q:
            u, s = q.popleft()
            for v in graph[u]:
                if v in seen:
                    continue
                seen.add(v)
                if flow_rate[v] != 0:
                    d[v] = s + 1
                q.append((v, s+1))
        return d

    distances = dict()
    key_to_idx = dict()
    idx = 0
    for u in vertices:
        if flow_rate[u] != 0 or u == "AA":
            key_to_idx[u] = idx
            idx += 1
            distances[u] = bfs(u, dict())

    @cache(None)
    def dfs(p1, p2, s1, s2, mask):
        nonlocal distances
        res = 0
        for v, d1 in distances[p1].items():
            idx = key_to_idx[v]
            if (mask >> idx) & 1 or s1 - d1 - 1 < 0:
                continue
            res = max(res, dfs(v, p2, s1 - d1 - 1, s2, mask | ( 1 << idx )) + flow_rate[v] * (s1 - d1 - 1))

        for t, d2 in distances[p2].items():
            idx = key_to_idx[t]
            if (mask >> idx) & 1 or s2 - d2 - 1 < 0:
                continue
            res = max(res, dfs(p1, t, s1, s2 - d2 - 1, mask | (1 << idx)) + flow_rate[t] * (s2 - d2 - 1))

        return res
    
    print(dfs("AA", "AA", 26, 26, 0))

            






if __name__ == "__main__":
    main()

