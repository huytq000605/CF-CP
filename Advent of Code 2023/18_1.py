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

    mn_r, mn_c, mx_r, mx_c = math.inf, math.inf, -math.inf, -math.inf

    r, c = 0, 0
    for line in lines:
        d, s, _ = line.split(" ")
        s = int(s)
        if d == "R":
            c += s
        elif d == "L":
            c -= s
        elif d == "U":
            r -= s
        elif d == "D":
            r += s
        mn_r = min(mn_r, r)
        mn_c = min(mn_c, c)
        mx_r = max(mx_r, r)
        mx_c = max(mx_c, c)
    m = (mx_r - mn_r) * 2
    n = (mx_c - mn_c) * 2

    result = 0

    r, c = mn_r, mn_c
    grid = [["." for j in range(n)] for i in range(m)]
    grid[r][c] = "#"
    for line in lines:
        d, s, _ = line.split(" ")
        s = int(s)
        while s:
            if d == "R":
                c += 1
            elif d == "L":
                c -= 1
            elif d == "U":
                r -= 1
            elif d == "D":
                r += 1
            result += 1
            grid[r][c] = "#"
            s -= 1

    ds = [(0,1), (1,0), (-1,0), (0,-1)]
    dq = [(mn_r+1, mn_c+1)]
    dq = deque(dq)
    while dq:
        r, c = dq.popleft()
        for dr, dc in ds:
            nr, nc = r + dr, c + dc
            if grid[nr][nc] == "#":
                continue
            grid[nr][nc] = "#"
            dq.append((nr, nc))
            result += 1

    #for lll in grid:
        #print("".join(lll))
    print(result)



if __name__ == "__main__":
    main()

