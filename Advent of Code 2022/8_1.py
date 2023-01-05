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
    visible = set()
    for r in range(m):
        stack = []
        for c in range(n):
            while stack and grid[r][c] > stack[-1]:
                stack.pop()
            if not stack:
                visible.add((r, c))
            stack.append(grid[r][c])
        
        stack = []
        for c in reversed(range(n)):
            while stack and grid[r][c] > stack[-1]:
                stack.pop()
            if not stack:
                visible.add((r, c))
            stack.append(grid[r][c])

    for c in range(n):
        stack = []
        for r in range(m):
            while stack and grid[r][c] > stack[-1]:
                stack.pop()
            if not stack:
                visible.add((r, c))
            stack.append(grid[r][c])

        stack = []
        for r in reversed(range(m)):
            while stack and grid[r][c] > stack[-1]:
                stack.pop()
            if not stack:
                visible.add((r, c))
            stack.append(grid[r][c])
    print(len(visible))








if __name__ == "__main__":
    main()
