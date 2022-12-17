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
    
    times = 100000
    max_row = 4 * times + 4 + 1
    grid = [["." for j in range(7)] for i in range(max_row)]

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

    def get_state():
        nonlocal highest_rock, grid, idx_pattern, idx_rock
        lowest = 0
        cols = [1 for i in range(7)]
        row = highest_rock
        while row >= 0 and any(cols[col] == 1 for col in range(7)):
            for col in range(7):
                if not cols[col]:
                    continue
                if grid[row][col] == "#":
                    cols[col] = 0
            row -= 1
        hash_str = f"{idx_pattern}_{idx_rock}_"
        for r in range(row, highest_rock):
            for c in range(7):
                hash_str += grid[r][c]
        return hash_str
        

    highest_rock = 0
    seen = dict({get_state(): -1})
    heights = dict()
    # COUNT EACH CYCLE
    # COUNT BEFORE CYCLE
    # COUNT REMAINING AFTER CYCLE
    cycle = 0
    height_when_found_cycle = -1
    count = 0
    remaining = -1
    before_cycle = -1
    cycle_time = -1
    times = 10**12


    for time in range(times):
        rock = get_rock()
        start = (highest_rock + 3, 2)
        rock_pos = []
        for p in rock:
            rock_pos.append((p[0] + start[0], p[1] + start[1]))

        while True:
            pattern = get_pattern()
            rock_pos, _ = next_rock(rock_pos, pattern)
            rock_pos, fall = next_rock(rock_pos, (-1, 0))
            if not fall:
                for r, c in rock_pos:
                    highest_rock = max(highest_rock, r+1)
                    grid[r][c] = "#"
                break
        state = get_state()
        count += 1
        if cycle == 0 and state in seen:
            cycle = time - seen[state]
            count = 1
            print("FOUND CYCLE =", cycle)
            each_cycle = highest_rock - heights[seen[state]]
            before_cycle = heights[seen[state]]
            remaining = (times - seen[state]) % cycle
            height_when_found_cycle = highest_rock
            cycle_time = (times - seen[state]) // cycle
            print(each_cycle, before_cycle)


        if count == remaining:
            print(before_cycle + each_cycle * cycle_time + highest_rock - height_when_found_cycle)
            return
            

        heights[time] = highest_rock
        seen[state] = time

            
    print("result:", highest_rock)

if __name__ == "__main__":
    main()

