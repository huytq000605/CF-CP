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
    m = len(lines)
    n = len(lines[0])
    grid = [[0 for j in range(n)] for i in range(m)]
    for i in range(m):
        for j in range(n):
            grid[i][j] = int(lines[i][j])
    result = 0
    for r in range(m):
        for c in range(n):
            top = 0
            for rr in range(r-1, -1, -1):
                top += 1
                if grid[r][c] <= grid[rr][c]:
                    break

            down = 0
            for rr in range(r+1, m):
                down += 1
                if grid[r][c] <= grid[rr][c]:
                    break

            left = 0
            for cc in range(c-1, -1, -1):
                left += 1
                if grid[r][c] <= grid[r][cc]:
                    break
            
            right = 0
            for cc in range(c+1, n):
                right += 1
                if grid[r][c] <= grid[r][cc]:
                    break

            result = max(top * down * left * right, result)


    print(result)








if __name__ == "__main__":
    main()
