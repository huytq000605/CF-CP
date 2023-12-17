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
    
    grid = lines
    m, n = len(grid), len(grid[0])

    ds = [(0,1),(1,0),(0,-1),(-1,0)]
    pq = [(0,0,0,0,1,0), (0,0,0,1,0,0)]
    min_s = defaultdict(lambda: math.inf)
    for _, r, c, pdr, pdc, sd in pq:
        min_s[(r, c, pdr, pdc, sd)] = 0

    while pq:
        s, r, c, pdr, pdc, sd = heappop(pq)
        if (r, c) == (m-1, n-1):
            print(s, pdr, pdc, sd)
            break

        for dr, dc in ds:
            if sd == 3 and (dr, dc) == (pdr, pdc):
                continue
            if (dr, dc) != (pdr, pdc) and pdr*dr + pdc*dc != 0:
                continue
            nr, nc = r + dr, c + dc
            if nr < 0 or nc < 0 or nr >= m or nc >= n:
                continue

            if (pdr, pdc) == (dr, dc):
                nsd = sd + 1
            else:
                nsd = 1

            ns = s + int(grid[nr][nc])
            if ns < min_s[(nr, nc, dr, dc, nsd)]:
                min_s[(nr, nc, dr, dc, nsd)] = ns
                heappush(pq, (ns, nr, nc, dr, dc, nsd))

if __name__ == "__main__":
    main()

