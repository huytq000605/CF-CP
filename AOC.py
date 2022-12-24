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
                    new_grid[nr][nc].sort()
        grid = new_grid
    count = 0

    def get_state(r, c):
        return (r, c, str(grid))

    result = 0


    try:
        goal = (m-1, lines[-1].index("."))
        cur = 0
        q = deque([(0, lines[0].index("."), 0)])
        seen = set()
        while q:
            r, c, s = q.popleft()
            count += 1
            if s == cur:
                cur += 1
                move()
            for dr, dc in ds.values():
                nr, nc = r + dr, c + dc
                if (nr, nc) == goal:
                    print("1st", s+1)
                    result += s + 1
                    raise BreakOutException
                if nr == m-1 or nc == n-1 or nr <= 0 or nc <= 0 or len(grid[nr][nc]) > 0:
                    continue
                if get_state(nr, nc) in seen:
                    continue
                seen.add(get_state(nr, nc))
                q.append((nr, nc, s + 1))
            if len(grid[r][c]) == 0 and get_state(r, c) not in seen:
                q.append((r, c, s + 1))
    except BreakOutException:
        pass

    try:
        goal = (0, 1)
        cur = 0
        q = deque([(m-1, n-2, 0)])
        seen = set()
        while q:
            r, c, s = q.popleft()
            count += 1
            if s == cur:
                cur += 1
                move()
            for dr, dc in ds.values():
                nr, nc = r + dr, c + dc
                if (nr, nc) == goal:
                    print("2nd", s+1)
                    result += s+1
                    raise BreakOutException
                if nr >= m-1 or nc >= n-1 or nr <= 0 or nc <= 0 or len(grid[nr][nc]) > 0:
                    continue
                if get_state(nr, nc) in seen:
                    continue
                seen.add(get_state(nr, nc))
                q.append((nr, nc, s + 1))
            if len(grid[r][c]) == 0 and get_state(r, c) not in seen:
                q.append((r, c, s + 1))
    except BreakOutException:
        pass

    try: 
        goal = (m-1, lines[-1].index("."))
        cur = 0
        q = deque([(0, lines[0].index("."), 0)])
        seen = set()
        while q:
            r, c, s = q.popleft()
            count += 1
            if s == cur:
                cur += 1
                move()
            for dr, dc in ds.values():
                nr, nc = r + dr, c + dc
                if (nr, nc) == goal:
                    print("3rd", s+1)
                    result += s+1
                    raise BreakOutException
                if nr == m-1 or nc == n-1 or nr <= 0 or nc <= 0 or len(grid[nr][nc]) > 0:
                    continue
                if get_state(nr, nc) in seen:
                    continue
                seen.add(get_state(nr, nc))
                q.append((nr, nc, s + 1))
            if len(grid[r][c]) == 0 and get_state(r, c) not in seen:
                q.append((r, c, s + 1))
    except BreakOutException:
        pass


    print("FINISH")
    print(result)
    




if __name__ == "__main__":
    main()

