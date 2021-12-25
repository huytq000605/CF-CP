import sys
import collections
from functools import lru_cache
from typing import *
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

def main():
    lines = sys.stdin.read().splitlines()
    m, n = len(lines), len(lines[0])
    grid = [[None for j in range(n)] for i in range(m)]
    for row, line in enumerate(lines):
        for col, value in enumerate(line):
            grid[row][col] = value


    print(solve(grid))



class BreakOutException(Exception):
	pass


def solve(grid):
    m, n = len(grid), len(grid[0])
    def print_grid():
        nonlocal grid
        for i in range(m):
            print(grid[i])
        print()
    steps = 0
    while True:
        nextGrid = copy.deepcopy(grid)
        move = False
        for row in range(m):
            for col in range(n):
                if grid[row][col] == ">" and grid[row][(col + 1) % n] == ".":
                    move = True
                    nextGrid[row][col] = "."
                    nextGrid[row][(col + 1) % n] = ">"
        grid = nextGrid
        nextGrid = copy.deepcopy(grid)
        for row in range(m):
            for col in range(n):
                if grid[row][col] == "v" and grid[(row + 1) % m][col] == ".":
                    move = True
                    nextGrid[row][col] = "."
                    nextGrid[(row + 1) % m][col] = "v"
        steps += 1
        if not move:
            return steps
        grid = nextGrid

	
if __name__ == "__main__":
	main()
