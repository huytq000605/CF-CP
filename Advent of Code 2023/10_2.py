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
    matrix = [list(m) for m in matrix]
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
            dq.append((prev_dr, prev_dc, r, c))
            visited.add((r, c))
    
    # Find the value of S
    for point_type in ds:
        dr1, dc1, _, _ = dq[0]
        dr2, dc2, _, _ = dq[-1]
        if (dr1, dc1) in ds[point_type].values() and (dr2, dc2) in ds[point_type].values():
            matrix[starts[0]][starts[1]] = point_type

    while dq:
        pdr, pdc, r, c = dq.popleft()
        dr, dc = ds[matrix[r][c]][(pdr, pdc)]
        nr, nc = r + dr, c + dc
        if (nr, nc) not in visited:
            visited.add((nr, nc))
            dq.append((dr, dc, nr, nc))

    big_matrix = [["." for _ in range(n*3)] for _ in range(m*3)]
    for (r, c) in visited:
        br, bc = r*3, c*3
        big_matrix[br][bc] = matrix[r][c]
        if matrix[r][c] == "-":
            big_matrix[br][bc+1] = "-"
            big_matrix[br][bc-1] = "-"
        elif matrix[r][c] == "|":
            big_matrix[br+1][bc] = "|"
            big_matrix[br-1][bc] = "|"
        elif matrix[r][c] == "L":
            big_matrix[br-1][bc] = "|"
            big_matrix[br][bc+1] = "-"
        elif matrix[r][c] == "J":
            big_matrix[br-1][bc] = "|"
            big_matrix[br][bc-1] = "-"
        elif matrix[r][c] == "7":
            big_matrix[br+1][bc] = "|"
            big_matrix[br][bc-1] = "-"
        elif matrix[r][c] == "F":
            big_matrix[br+1][bc] = "|"
            big_matrix[br][bc+1] = "-"

    #for lll in big_matrix:
        #print(''.join(lll))


    ds = [(0,1), (1,0), (-1,0), (0,-1)]

    dq = deque()
    for r in range(3*m):
        dq.append((r, -1))
        dq.append((r, 3*n))
    for c in range(3*n):
        dq.append((-1, c))
        dq.append((3*m, c))

    out = set()
    while dq:
        r, c = dq.popleft()
        for dr, dc in ds:
            nr, nc = r + dr, c + dc
            if nr < 0 or nr >= 3 * m or nc < 0 or nc >= 3 * n:
                continue
            if big_matrix[nr][nc] != "." or (nr, nc) in out:
                continue
            out.add((nr, nc))
            dq.append((nr, nc))

    result = 0
    for r in range(m):
        for c in range(n):
            if (r, c) not in visited and (r*3, c*3) not in out:
                result += 1
    print(result)



if __name__ == "__main__":
    main()

