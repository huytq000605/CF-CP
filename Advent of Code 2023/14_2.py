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

    m, n = len(lines), len(lines[0])

    grid = [[lines[r][c] for c in range(n)] for r in range(m)]


    def north():
        for r in range(1, m):
            for c in range(n):
                if grid[r][c] != "O": continue
                cur_r = r
                while cur_r > 0 and grid[cur_r - 1][c] == ".":
                    grid[cur_r - 1][c] = "O"
                    grid[cur_r][c] = "."
                    cur_r -= 1

    def south():
        for r in range(m - 2, -1, -1):
            for c in range(n):
                if grid[r][c] != "O": continue
                cur_r = r
                while cur_r < m - 1 and grid[cur_r + 1][c] == ".":
                    grid[cur_r + 1][c] = "O"
                    grid[cur_r][c] = "."
                    cur_r += 1

    def east():
        for c in range(n - 2, -1, -1):
            for r in range(m):
                if grid[r][c] != "O": continue
                cur_c = c
                while cur_c < n - 1 and grid[r][cur_c + 1] == ".":
                    grid[r][cur_c + 1] = "O"
                    grid[r][cur_c] = "."
                    cur_c += 1

    def west():
        for c in range(1, n):
            for r in range(m):
                if grid[r][c] != "O": continue
                cur_c = c
                while cur_c > 0 and grid[r][cur_c - 1] == ".":
                    grid[r][cur_c - 1] = "O"
                    grid[r][cur_c] = "."
                    cur_c -= 1


    seen = dict()

    cycles = 1000000000
    first = 0
    graph_cycle = 0
    for cycle in range(cycles):
        north()
        west()
        south()
        east()
        s = str(grid)
        if s in seen:
            graph_cycle = cycle - seen[s]
            first = seen[s]
            grid = ast.literal_eval(s)
            break
        seen[s] = cycle

    print("first", first, graph_cycle)
    remain = (cycles - first - 1) % graph_cycle
    for _ in range(remain):
        north()
        west()
        south()
        east()

    result = 0
    for r in range(m):
        for c in range(n):
            if grid[r][c] == "O":
                result += m - r
    print(result)


            




if __name__ == "__main__":
    main()

