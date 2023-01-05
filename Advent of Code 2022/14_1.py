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
    m, n = 1000, 1000
    grid = [["." for j in range(n)] for i in range(m)]
    grid[0][500] = "*"
    HIGHEST_ROW = 0
    for line in lines:
        points = []
        rc = line.split(" -> ")
        for p in rc:
            c, r = map(int, p.split(","))
            points.append((r, c))
            HIGHEST_ROW = max(HIGHEST_ROW, r)

        k = len(points)
        for i in range(k-1):
            r1, c1 = points[i]
            r2, c2 = points[i+1]
            if r1 == r2:
                for c in range(min(c1, c2), max(c1, c2) + 1):
                    grid[r1][c] = "#"
            elif c1 == c2:
                for r in range(min(r1, r2), max(r1, r2) + 1):
                    grid[r][c1] = "#"

    result = 0
    while True:
        r,  c = 0, 500
        while r < HIGHEST_ROW:
            if grid[r+1][c] == ".":
                r += 1
            elif grid[r+1][c-1] == ".":
                r += 1
                c -= 1
            elif grid[r+1][c+1] == ".":
                r += 1
                c += 1
            else:
                grid[r][c] = "o"
                result += 1
                break
        if r >= HIGHEST_ROW:
            break

    print(result)
        
                



    



        





if __name__ == "__main__":
    main()
