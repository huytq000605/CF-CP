
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
    slopes = {
            ">": (0, 1),
            "<": (0, -1),
            "^": (-1, 0),
            "v": (1, 0)
    }
    ds = [(0,1), (0,-1), (1,0), (-1,0)]
    m,n = len(grid), len(grid[0])
    start = [(0, c) for c in range(n) if grid[0][c] == "."][0]
    end = [(m-1, c) for c in range(n) if grid[m-1][c] == "."][0]
    print(start, end)
    dq = deque([(start[0], start[1], 0, set([start]))])
    result = 0
    while dq:
        r, c, s, seen = dq.popleft()
        seen = set(seen)
        if (r,c) == end:
            result = max(result, s)
            continue
        for dr, dc in ds:
            nr, nc = r + dr, c + dc
            if nr < 0 or nr >= m or nc < 0 or nc >= n: continue
            if grid[nr][nc] == "#": continue
            if (nr, nc) in seen: continue
            is_slop = 0
            if grid[nr][nc] in slopes.keys():
                is_slop = 1
                dr, dc = slopes[grid[nr][nc]]
                nr, nc = nr + dr, nc + dc
                if (nr, nc) in seen:
                    continue
            seen.add((nr, nc))
            dq.append((nr, nc, s + 1 + is_slop, seen))
    print(result)
    


if __name__ == "__main__":
    main()


