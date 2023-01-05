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
    cmds = lines[-1]
    lines = lines[:-1]
    m = len(lines)
    n = 0
    for line in lines:
        n = max(n, len(line))
    grid = [["" for j in range(n)] for i in range(m)]
    for i in range(m):
        for j in range(n):
            if j >= len(lines[i]):
                break
            grid[i][j] = lines[i][j]
    ds = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    di = 0

    def get_next(r, c):
        nonlocal ds, di, grid
        dr, dc = ds[di]
        while True:
            r, c = r + dr, c + dc
            if r == -1:
                r = m-1
            if c == -1:
                c = n-1
            if r == m:
                r = 0
            if c == n:
                c = 0
            if grid[r][c] != " " and grid[r][c] != "":
                break
        return (r, c)
    
    def rotate(d):
        nonlocal di
        if d == "R":
            di += 1
        elif d == "L":
            di -= 1
        if di == 4:
            di = 0
        if di == -1:
            di = 3

    r, c = -1, -1
    valid = False

    for i in range(m):
        for j in range(n):
            if grid[i][j] != " ":
                r, c = i, j
                valid = True
                break
        if valid:
            break
        
    print(r, c)
    cur = 0
    for i, ch in enumerate(cmds):
        if ch.isdigit():
            cur = cur * 10 + int(ch)
        if i == len(cmds) - 1 or not ch.isdigit():
            for _ in range(cur):
                nr, nc = get_next(r, c)
                if grid[nr][nc] == "#":
                    break
                r, c = nr, nc
            if not ch.isdigit():
                rotate(ch)
            cur = 0
    print(r, c)
    print(1000 * (r+1) + 4 * (c+1) + di)







            


if __name__ == "__main__":
    main()

