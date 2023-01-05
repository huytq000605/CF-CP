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
    n = len(lines)
    elves = set()
    for r in range(n):
        for c in range(n):
            if lines[r][c] == "#":
                elves.add((r, c))
    ds = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    di = 0

    def consider_move(r, c):
        nonlocal elves
        for dr in range(-1, 2):
            for dc in range(-1, 2):
                if dr == dc == 0: continue
                if (r + dr, c + dc) in elves:
                    return True
        return False
    
    def move(r, c):
        nonlocal elves, di
        i = di
        for _ in range(4):
            dr, dc = ds[i]
            if i == 0 or i == 1:
                if all([(r + dr, c + dcc) not in elves for dcc in range(-1, 2)]):
                    return (r + dr, c + dc)
            else:
                if all([(r + drr, c + dc) not in elves for drr in range(-1, 2)]):
                    return (r + dr, c + dc)
            i += 1
            i %= 4
        return (r, c)


    time = 0
    while True:
        time += 1
        next_elves = dict()
        freq = defaultdict(int)
        for r, c in elves:
            if not consider_move(r, c):
                next_elves[(r, c)] = (r, c)
                freq[(r, c)] += 1
                continue
            nr, nc = move(r, c)
            freq[(nr, nc)] += 1
            next_elves[(r, c)] = (nr, nc)
        for (r, c) in elves:
            nr, nc = next_elves[(r, c)]
            if freq[(nr, nc)] > 1:
                next_elves[(r, c)] = (r, c)
        new_elves = set(next_elves.values())
        if elves == new_elves:
            print(time)
            return
        elves = new_elves

        di += 1
        di %= 4

    lr, lc, hr, hc = math.inf, math.inf, -math.inf, -math.inf




if __name__ == "__main__":
    main()

