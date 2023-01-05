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
    for u in vertices:
        if flow_rate[u] != 0 or u == "AA":
            distances[u] = bfs(u, dict())

    opened = set()
    def dfs(u, s, elephant):
        nonlocal distances
        res = 0
        for v, d in distances[u].items():
            if v in opened:
                continue
            if s - d - 1 >= 0:
                opened.add(v)
                res = max(res, dfs(v, s - d - 1, elephant) + flow_rate[v] * (s - d - 1))
                opened.remove(v)

        if not elephant:
            res = max(res, dfs("AA", 26, True))

        return res
    
    print(dfs("AA", 26, False))

            






if __name__ == "__main__":
    main()
