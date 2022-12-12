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
    grid = [[0 for j in range(n)] for i in range(m)]
    starts = []
    end = (0, 0)
    for r, line in enumerate(lines):
        for c, l in enumerate(line):
            if l == "S" or l == "a":
                starts.append((r, c))
                grid[r][c] = ord("a") - ord("a")
            elif l == "E":
                end = (r, c)
                grid[r][c] = ord("z") - ord("a")
            else:
                grid[r][c] = ord(l) - ord("a")
    def bfs(start):
        q = deque([(start[0], start[1], 0)])
        ds = [(0,1), (1,0), (-1, 0), (0, -1)]
        seen = set([start])
        while q:
            r, c, s = q.popleft()
            if r == end[0] and c == end[1]:
                return s
            for dr, dc in ds:
                nr, nc = r + dr, c + dc
                if nr < 0 or nc < 0 or nr >= m or nc >= n or grid[nr][nc] - grid[r][c] > 1:
                    continue
                if (nr, nc) not in seen:
                    seen.add((nr, nc))
                    q.append((nr, nc, s+1))
        return math.inf
    result = math.inf
    for start in starts:
        result = min(result, bfs(start))
    print(result)
                






if __name__ == "__main__":
    main()
