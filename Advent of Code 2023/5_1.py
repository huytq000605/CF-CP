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
    seeds = set(map(int, lines[0].split(": ")[1].split(" ")))
    line_idx = 1
    next_seeds = set(seeds)
    while line_idx < len(lines):
        line = lines[line_idx]
        if line == "":
            seeds = seeds.union(next_seeds)
            next_seeds.clear()
            line_idx += 2
            continue
        dest, source, length = map(int, line.split(" "))
        used = set()
        for seed in seeds:
            if source <= seed < source + length:
                diff = seed - source
                next_seeds.add(dest + diff)
                used.add(seed)

        for seed in used:
            seeds.remove(seed)
                
        line_idx += 1
    seeds = seeds.union(next_seeds)
    print(min(seeds), seeds)
    return min(next_seeds)

        

if __name__ == "__main__":
    main()

