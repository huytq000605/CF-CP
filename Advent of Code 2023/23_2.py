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
    ds = [(0,1), (0,-1), (1,0), (-1,0)]
    m,n = len(grid), len(grid[0])
    start = [(0, c) for c in range(n) if grid[0][c] == "."][0]
    end = [(m-1, c) for c in range(n) if grid[m-1][c] == "."][0]
    result = 0

    intersections = set()
    sub_paths = dict()

    def explore(r, c, sr, sc):
        seen = set([(r, c), (sr, sc)])
        sr, sc = r, c
        dq = deque([(r, c)])
        s = 0
        while dq:
            r, c = dq.popleft()
            if ((r,c) == start or (r,c) == end or (r,c) in intersections) and (r,c) != (sr, sc):
                sub_paths[(sr, sc)] = (r, c, s)
                assert len(dq) == 0
                return
            s += 1

            for dr, dc in ds:
                nr, nc = r + dr, c + dc
                if nr < 0 or nr >= m or nc < 0 or nc >= n: continue
                if grid[nr][nc] == "#": continue
                if (nr, nc) in seen: continue
                seen.add((nr, nc))
                dq.append((nr,nc))


    for r in range(m):
        for c in range(n):
            if grid[r][c] == "#": continue
            valid_moves = 0
            for dr, dc in ds:
                nr, nc = r + dr, c + dc
                if nr < 0 or nr >= m or nc < 0 or nc >= n: continue
                if grid[nr][nc] == "#": continue
                valid_moves += 1
            if valid_moves > 2:
                intersections.add((r, c))
    
    for r, c in intersections:
        for dr, dc in ds:
            nr, nc = r + dr, c + dc
            if nr < 0 or nr >= m or nc < 0 or nc >= n: continue
            if grid[nr][nc] == "#": continue
            explore(nr, nc, r, c)
    explore(start[0], start[1], start[0], start[1])
    explore(end[0], end[1], end[0], end[1])

    dq = [(start[0], start[1], set([start]), 0)]
    dq = deque(dq)

    dp = dict()

    result = 0
    def dfs(r, c, seen):
        seen_key = str(sorted(list(seen)))
        result = -math.inf
        if (r, c, seen_key) in dp:
            return dp[(r,c,seen_key)]
        if (r,c) == end:
            result =  0
        elif (r,c) == start:
            nr, nc, ss = sub_paths[(r, c)]
            seen.add((nr, nc))
            result = ss + dfs(nr, nc, seen)
        else:
            for dr, dc in ds:
                nr, nc = r + dr, c + dc
                if nr < 0 or nr >= m or nc < 0 or nc >= n: continue
                if grid[nr][nc] == "#": continue
                nnr, nnc, ss = sub_paths[(nr, nc)]
                if (nnr, nnc) in seen: continue
                new_seen = set(seen)
                # new_seen.add((nr, nc))
                new_seen.add((nnr, nnc))
                result = max(result, 1 + ss + dfs(nnr, nnc, new_seen))
        dp[(r,c,seen_key)] = result
        return result

    result = dfs(start[0], start[1], set([start]))
    print(result)



if __name__ == "__main__":
    main()



