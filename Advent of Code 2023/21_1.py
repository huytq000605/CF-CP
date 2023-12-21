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
import ast
def get_int(): return int(input())
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_list(): return list(map(int, sys.stdin.readline().strip().split()))
def get_string(): return sys.stdin.readline().strip()


class BreakOutException(Exception):
    pass


def main():
    lines = sys.stdin.read().splitlines()
    grid = [[c for c in line] for line in lines]
    m, n = len(grid), len(grid[0])
    ds = [(0,1),(1,0),(-1,0),(0,-1)]
    dq = []
    for r in range(m):
        for c in range(n):
            if grid[r][c] == "S":
                grid[r][c] = "."
                dq.append((r, c))
                break
    dq = deque(dq)
    for _ in range(64):
        ndq = set()
        while dq:
            r, c = dq.popleft()
            for dr, dc in ds:
                nr, nc = r + dr, c + dc
                if nr < 0 or nr >= m or nc < 0 or nc >= n:
                    continue
                if grid[nr][nc] == ".": 
                    ndq.add((nr, nc))
        dq = deque(ndq)
    print(len(dq))
            

if __name__ == "__main__":
    main()

