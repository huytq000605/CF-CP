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
        new_seeds = []
        intervals.sort()
        for src_start, src_end, diff in intervals:
            next_seeds = []
            while seeds:
                start, end = seeds.pop()
                before = (start, min(src_start - 1, end))
                inner = (max(src_start, start), min(src_end, end))
                after = (max(start, src_end + 1), end)

                if before[0] <= before[1]:
                    next_seeds.append(before)

                if inner[0] <= inner[1]:
                    new_seeds.append(inner)

                if after[0] <= after[1]:
                    next_seeds.append(after)
            seeds = next_seeds
        return new_seeds + seeds

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

