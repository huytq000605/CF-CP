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
from copy import copy, deepcopy
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_list(): return list(map(int, sys.stdin.readline().strip().split()))
def get_string(): return sys.stdin.readline().strip()


class BreakOutException(Exception):
    pass

class UF:
    def __init__(self):
        self.p = dict()
        self.r = defaultdict(lambda: 1)

    def find(self, u):
        if u not in self.p:
            self.p[u] = u
        if u != self.p[u]:
            self.p[u] = self.find(self.p[u])
        return self.p[u]
    
    def union(self, u, v):
        u, v = self.find(u), self.find(v)
        if self.r[u] < self.r[v]:
            u, v = v, u
        self.p[v] = u
        self.r[u] += self.r[v]

def main():
    lines = sys.stdin.read().splitlines()
    from itertools import combinations
    print(lines)
    grid = {i+j*1j: c for i,r in enumerate(lines)
                    for j,c in enumerate(r) if c != '#'}

    start, = (p for p in grid if grid[p] == 'S')


    dist = {start: 0}
    todo = [start]

    for pos in todo:
        for new in pos-1, pos+1, pos-1j, pos+1j:
            if new in grid and new not in dist:
                dist[new] = dist[pos] + 1
                todo += [new]


    a = b = 0

    for (p,i), (q,j) in combinations(dist.items(), 2):
        d = abs((p-q).real) + abs((p-q).imag)
        if d == 2 and j-i-d >= 100: a += 1
        if d < 21 and j-i-d >= 100: b += 1

    print(a, b)
    

    


        

        
if __name__ == "__main__":
    main()



