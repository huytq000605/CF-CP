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
    lines = sys.stdin.read().splitlines()

    m, n = len(lines), len(lines[0])

    grid = [[lines[r][c] for c in range(n)] for r in range(m)]


    for r in range(1, m):
        for c in range(n):
            if grid[r][c] != "O": continue
            cur_r = r
            while cur_r > 0 and grid[cur_r - 1][c] == ".":
                grid[cur_r - 1][c] = "O"
                grid[cur_r][c] = "."
                cur_r -= 1

    for lll in grid:
        print("".join(lll))

    result = 0
    for r in range(m):
        for c in range(n):
            if grid[r][c] == "O":
                result += m - r
    print(result)


            




if __name__ == "__main__":
    main()

