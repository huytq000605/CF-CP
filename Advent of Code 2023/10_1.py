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
    matrix = sys.stdin.read().splitlines()
    ds = {
        # cur - prev = (prev_dr, prev_dc)
        # mapping from # (prev_dr, prev_dc) to (dr, dc) 
        "|": {
            (-1, 0): (-1, 0),
            (1, 0): (1, 0)
        },
        "-": {
            (0, 1): (0, 1),
            (0, -1): (0, -1)
        },
        "L": {
            (0, -1): (-1, 0),
            (1, 0): (0, 1)
        },
        "J": {
            (1, 0): (0, -1),
            (0, 1): (-1, 0)
        },
        "7": {
            (0, 1): (1, 0),
            (-1, 0): (0, -1)
        },
        "F": {
            (-1, 0): (0, 1),
            (0, -1): (1, 0)
        }
    }

    m, n = len(matrix), len(matrix[0])
    starts = (-1, -1)
    for r in range(m):
        for c in range(n):
            if matrix[r][c] == "S":
                starts = (r, c)
                break
    dq = deque()
    visited = set([starts])

    for prev_dr, prev_dc in [(0,1), (1,0), (0, -1), (-1, 0)]:
        r, c = starts[0] + prev_dr, starts[1] + prev_dc
        if matrix[r][c] in ds and (prev_dr, prev_dc) in ds[matrix[r][c]]:
            dq.append((prev_dr, prev_dc, r, c, 1))
            visited.add((r, c))

    result = 0
    while dq:
        pdr, pdc, r, c, s = dq.popleft()
        result = max(result, s)
        dr, dc = ds[matrix[r][c]][(pdr, pdc)]
        nr, nc = r + dr, c + dc
        if (nr, nc) not in visited:
            visited.add((nr, nc))
            dq.append((dr, dc, nr, nc, s + 1))
    
    print(result)

if __name__ == "__main__":
    main()

