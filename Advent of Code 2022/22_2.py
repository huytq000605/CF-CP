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
    grid = lines[:-2]
    ds = [(0, 1), (1, 0), (0, -1), (-1, 0)]


    wrap_map = {}
# wrap 1
    e1 = [(0+k, 50) for k in range(50)]
    e2 = [(149-k, 0) for k in range(50)]
    for k in range(50):
        wrap_map[(e1[k][0], e1[k][1], (0, -1))] = (e2[k][0], e2[k][1], (0, 1))
        wrap_map[(e2[k][0], e2[k][1], (0, -1))] = (e1[k][0], e1[k][1], (0, 1))
# wrap 2
    e1 = [(50+k, 50) for k in range(50)]
    e2 = [(100, 0+k) for k in range(50)]
    for k in range(50):
        wrap_map[(e1[k][0], e1[k][1], (0, -1))] = (e2[k][0], e2[k][1], (1, 0))
        wrap_map[(e2[k][0], e2[k][1], (-1, 0))] = (e1[k][0], e1[k][1], (0, 1))
# wrap 3
    e1 = [(0, 50+k) for k in range(50)]
    e2 = [(150+k, 0) for k in range(50)]
    for k in range(50):
        wrap_map[(e1[k][0], e1[k][1], (-1, 0))] = (e2[k][0], e2[k][1], (0, 1))
        wrap_map[(e2[k][0], e2[k][1], (0, -1))] = (e1[k][0], e1[k][1], (1, 0))
# wrap 4
    e1 = [(49, 100+k) for k in range(50)]
    e2 = [(50+k, 99) for k in range(50)]
    for k in range(50):
        wrap_map[(e1[k][0], e1[k][1], (1, 0))] = (e2[k][0], e2[k][1], (0, -1))
        wrap_map[(e2[k][0], e2[k][1], (0, 1))] = (e1[k][0], e1[k][1], (-1, 0))
# wrap 5
    e1 = [(149, 50+k) for k in range(50)]
    e2 = [(150+k, 49) for k in range(50)]
    for k in range(50):
        wrap_map[(e1[k][0], e1[k][1], (1, 0))] = (e2[k][0], e2[k][1], (0, -1))
        wrap_map[(e2[k][0], e2[k][1], (0, 1))] = (e1[k][0], e1[k][1], (-1, 0))
# wrap 6
    e1 = [(0+k, 149) for k in range(50)]
    e2 = [(149-k, 99) for k in range(50)]
    for k in range(50):
        wrap_map[(e1[k][0], e1[k][1], (0, 1))] = (e2[k][0], e2[k][1], (0, -1))
        wrap_map[(e2[k][0], e2[k][1], (0, 1))] = (e1[k][0], e1[k][1], (0, -1))
# wrap 7
    e1 = [(0, 100+k) for k in range(50)]
    e2 = [(199, 0+k) for k in range(50)]
    for k in range(50):
        wrap_map[(e1[k][0], e1[k][1], (-1, 0))] = (e2[k][0], e2[k][1], (-1, 0))
        wrap_map[(e2[k][0], e2[k][1], (1, 0))] = (e1[k][0], e1[k][1], (1, 0))

    def get_next():
        nonlocal ds, di, r, c
        if (r, c, ds[di]) in wrap_map:
            nr, nc, nd = wrap_map[(r, c, ds[di])]
            return (nr, nc, ds.index(nd))
        dr, dc = ds[di]
        nr, nc = r + dr, c + dc
        return (nr, nc, di)
    
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

    di = 0
    r, c = 0, grid[0].index(".")

    cur = 0
    for i, ch in enumerate(cmds):
        if ch.isdigit():
            cur = cur * 10 + int(ch)
        if i == len(cmds) - 1 or not ch.isdigit():
            for _ in range(cur):
                nr, nc, ndi = get_next()
                if grid[nr][nc] == "#":
                    break
                r, c, di = nr, nc, ndi
            if not ch.isdigit():
                rotate(ch)
            cur = 0
    print(r+1, c+1)
    print(1000 * (r+1) + 4 * (c+1) + di)





if __name__ == "__main__":
    main()

