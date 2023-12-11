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
def get_int(): return int(input())
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_list(): return list(map(int, sys.stdin.readline().strip().split()))
def get_string(): return sys.stdin.readline().strip()


class BreakOutException(Exception):
    pass


def main():
    lines = sys.stdin.read().splitlines()

    grid = lines
    galaxies = []
    big_rows, big_cols = set(), set()
    m, n = len(lines), len(lines[0])
    for r in range(m):
        have_galaxy = False
        for c in range(n):
            if grid[r][c] == "#":
                have_galaxy = True
        if not have_galaxy:
            big_rows.add(r)
    

    for c in range(n):
        have_galaxy = False
        for r in range(m):
            if grid[r][c] == "#":
                have_galaxy = True
        if not have_galaxy:
            big_cols.add(c)

    for r in range(m):
        for c in range(n):
            if grid[r][c] == "#":
                galaxies.append((r, c))
    # for lll in grid:
        # print(''.join(lll))

    result = 0
    ds = [(0,1), (1,0), (0,-1), (-1,0)]
    for i, g in enumerate(galaxies):
        distances = defaultdict(lambda: math.inf)
        distances[g] = 0
        pq = [(0, g[0], g[1])]

        while pq:
            d, r, c = heappop(pq)
            for dr, dc in ds:
                nr, nc = r + dr, c + dc
                if nr < 0 or nr >= m or nc < 0 or nc >= n:
                    continue
                dd = 1
                if nr in big_rows:
                    dd += 1000000 - 1
                if nc in big_cols:
                    dd += 1000000 - 1
                if d + dd < distances[(nr, nc)]:
                    distances[(nr, nc)] = d + dd
                    heappush(pq, (d+dd, nr, nc))

        for j in range(i+1, len(galaxies)):
            g2 = galaxies[j]
            result += distances[g2]
    print(result)

            



if __name__ == "__main__":
    main()

