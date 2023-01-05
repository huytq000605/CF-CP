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
    line = lines[0]
    idx_pattern = 0
    def get_pattern():
        nonlocal idx_pattern
        pattern = line[idx_pattern]
        idx_pattern += 1
        idx_pattern %= len(line)
        if pattern == "<":
            return (0, -1)
        else:
            return (0, 1)
    
    rocks = [[(0, 0), (0, 1), (0,2), (0,3)], [(0, 1), (1, 0), (1, 1), (1, 2), (2, 1)], [(0, 0), (0, 1), (0,2), (1, 2), (2, 2)],[(0, 0), (1, 0), (2, 0), (3, 0)], [(0, 0), (0, 1), (1, 0), (1, 1)]]
    idx_rock = 0
    def get_rock():
        nonlocal idx_rock
        rock = rocks[idx_rock]
        idx_rock += 1
        idx_rock %= len(rocks)
        return rock
    
    grid = [["." for j in range(7)] for i in range(4 * 2022 + 4 + 1)]

    def next_rock(rock, pattern):
        dr, dc = pattern
        next_rock = []
        for p in rock:
            r, c = p
            nr, nc = r + dr, c + dc
            if nr < 0 or nc < 0 or nc >= 7 or grid[nr][nc] != ".":
                return rock, False
            next_rock.append((nr, nc))
        return next_rock, True

    lowest = 0
    for time in range(2022):
        rock = get_rock()
        start = (lowest + 3, 2)
        rock_pos = []
        for p in rock:
            rock_pos.append((p[0] + start[0], p[1] + start[1]))

        while True:
            pattern = get_pattern()
            rock_pos, _ = next_rock(rock_pos, pattern)
            rock_pos, fall = next_rock(rock_pos, (-1, 0))
            if not fall:
                for r, c in rock_pos:
                    lowest = max(lowest, r+1)
                    grid[r][c] = "#"
                break
    print("result:", lowest)


            




    








if __name__ == "__main__":
    main()

