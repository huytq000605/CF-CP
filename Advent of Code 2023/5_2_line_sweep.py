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
    seed_ranges = list(map(int, lines[0].split(": ")[1].split(" ")))
    seeds = []
    for i in range(0, len(seed_ranges), 2):
        seeds.append((seed_ranges[i], seed_ranges[i] + seed_ranges[i+1] - 1))

    line_idx = 1

    def process_seeds(seeds, intervals):
        line = []
        # sort line in order
        # start of src needs to start before seeds
        # end of src needs to end after seeds
        for src_start, src_end, diff in intervals:
            line.append((src_start, 1, diff))
            line.append((src_end, 4, diff))
        for start, end in seeds:
            line.append((start, 2, 0))
            line.append((end, 3, 0))

        line.sort()
        take = False
        change = 0
        cur = 0
        result = []
        for x, t, v in line:
            if t == 1:
                if take and x-1 >= cur: result.append((cur + change, x + change -1))
                cur = x
                change = v
            elif t == 4:
                if take: result.append((cur + change, x + change))
                cur = x+1
                change = 0
            elif t == 2:
                cur = x
                take = True
            elif t == 3:
                # always take == True
                if take: result.append((cur + change, x + change))
                cur = x + 1
                take = False

        result.sort()
        return result

    intervals = []
    while line_idx < len(lines):
        line = lines[line_idx]
        if line == "":
            if intervals:
                seeds = process_seeds(seeds, intervals)
            intervals = []
            line_idx += 2
            continue
        dst_start, src_start, length = map(int, line.split(" "))
        src_end = src_start + length - 1
        diff = dst_start - src_start
        intervals.append((src_start, src_end, diff))
        line_idx += 1

    seeds = process_seeds(seeds, intervals)
    result = math.inf
    for s, _ in seeds:
        result = min(result, s)
    print(result)
    return result

        

if __name__ == "__main__":
    main()


