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
    m, n = len(lines), len(lines[0])
    grid = [[[] for j in range(n)] for i in range(m)]
    for r in range(m):
        for c in range(n):
            if lines[r][c] != "." and lines[r][c] != "#":
                grid[r][c].append(lines[r][c])
    ds = {">": (0, 1), "<": (0, -1), "^": (-1, 0), "v": (1, 0)}
    goal = (m-1, lines[-1].index("."))
    cur = 0
    q = deque([(0, lines[0].index("."), 0)])

    def move():
        nonlocal grid
        new_grid = [[[] for j in range(n)] for i in range(m)]
        for r in range(1, m-1):
            for c in range(1, n-1):
                while grid[r][c]:
                    d = grid[r][c].pop()
                    dr, dc = ds[d]
                    nr, nc = r + dr, c + dc
                    if nr == m - 1:
                        nr = 1
                    if nc == n - 1:
                        nc = 1
                    if nr == 0:
                        nr = m-2
                    if nc == 0:
                        nc = n-2
                    new_grid[nr][nc].append(d)
        grid = new_grid


    result = 0

    def bfs(start, end):
        nonlocal result, grid
        cur = 0
        seen = set()
        q = deque([(start[0], start[1], 0)])
        while q:
            r, c, s = q.popleft()
            if s == cur:
                seen = set()
                cur += 1
                move()
            for dr, dc in ds.values():
                nr, nc = r + dr, c + dc
                if (nr, nc) == end:
                    print(s+1)
                    result += s + 1
                    return
                if nr >= m-1 or nc >= n-1 or nr <= 0 or nc <= 0 or len(grid[nr][nc]) > 0:
                    continue
                if (nr, nc) in seen:
                    continue
                seen.add((nr, nc))
                q.append((nr, nc, s + 1))
            if len(grid[r][c]) == 0 and (r, c) not in seen:
                q.append((r, c, s + 1))
    bfs((0, 1), (m-1, n-2))


    print("FINISH")
    print(result)
    




if __name__ == "__main__":
    main()


