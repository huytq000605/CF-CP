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
import z3
def get_int(): return int(input())
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

    import networkx
    graph = networkx.Graph()
    vertices = set()
    for line in lines:
        u, vs = line.split(": ")
        vertices.add(u)
        for v in vs.split(" "):
            vertices.add(v)
            graph.add_edge(u, v, capacity = 1)

    for u in vertices:
        for v in vertices:
            if u == v: continue
            cut_value, (L, R) = networkx.minimum_cut(graph, u, v)
            if cut_value == 3:
                print(len(L) * len(R))
                return

    

    

    


        

        
if __name__ == "__main__":
    main()



