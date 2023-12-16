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
    grid = [list(line) for line in lines]

    m, n = len(grid), len(grid[0])
    pd_to_nd = {
            "/": {
                (0, 1): (-1, 0),
                (1, 0): (0, -1),
                (-1, 0): (0, 1),
                (0, -1): (1, 0)
            },
            "\\": {
                (0, 1): (1, 0),
                (0, -1): (-1, 0),
                (1, 0): (0, 1),
                (-1, 0): (0, -1)
            },
            "|": {
                (0, 1): [(1, 0), (-1, 0)],
                (0, -1): [(1, 0), (-1, 0)],
                (1, 0): [(1, 0)],
                (-1, 0): [(-1, 0)]
            },
            "-": {
                (1, 0): [(0, 1), (0, -1)],
                (-1, 0): [(0, 1), (0, -1)],
                (0, 1): [(0, 1)],
                (0, -1): [(0, -1)]
            }

    }

    def bfs(start):
        dq = deque([start])
        visited = set([start])
        while dq:
            r, c, dr, dc = dq.popleft()
            nr, nc = r + dr, c + dc
            if nr < 0 or nc < 0 or nr >= m or nc >= n:
                continue
            if grid[nr][nc] in "/\\":
                dr, dc = pd_to_nd[grid[nr][nc]][(dr, dc)]
                if (nr, nc, dr, dc) not in visited:
                    visited.add((nr, nc, dr, dc))
                    dq.append((nr, nc, dr, dc))
            elif grid[nr][nc] in "-|":
                for dr, dc in pd_to_nd[grid[nr][nc]][(dr, dc)]:
                    if (nr, nc, dr, dc) not in visited:
                        visited.add((nr, nc, dr, dc))
                        dq.append((nr, nc, dr, dc))
            else:
                if (nr, nc, dr, dc) not in visited:
                    visited.add((nr, nc, dr, dc))
                    dq.append((nr, nc, dr, dc))
        result = set()
        for r, c, dr, dc in visited:
            result.add((r, c))
        return len(result)

    result = 0
    for c in range(n):
        result = max(result, bfs((0, c, 1, 0)))
        result = max(result, bfs((m-1, c, -1, 0)))

    for r in range(m):
        result = max(result, bfs((r, 0, 0, 1)))
        result = max(result, bfs((r, n-1, 0, -1)))

    print(result)


    
    ######### Debug ############
    # result = set()
    # for r, c, dr, dc in visited:
    #     result.add((r, c))
    #     if grid[r][c] != ".": continue
    #     if (dr, dc) == (0, 1): 
    #         grid[r][c] = ">"
    #     elif (dr, dc) == (0, -1):
    #         grid[r][c] = "<"
    #     elif (dr, dc) == (1, 0):
    #         grid[r][c] = "v"
    #     else:
    #         grid[r][c] = "^"
    #         
    # for lll in grid:
    #     print("".join(lll))
    # print(len(result))





            






if __name__ == "__main__":
    main()

