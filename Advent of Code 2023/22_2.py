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
import ast
def get_int(): return int(input())
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_list(): return list(map(int, sys.stdin.readline().strip().split()))
def get_string(): return sys.stdin.readline().strip()


class BreakOutException(Exception):
    pass

def main():
    lines = sys.stdin.read().splitlines()
    bricks = []
    n = len(lines)
    for line in lines:
        a, b = line.split("~")
        x1, y1, z1 = list(map(int, a.split(",")))
        x2, y2, z2 = list(map(int, b.split(",")))
        bricks.append(((x1, x2), (y1, y2), (z1, z2)))
    bricks.sort(key = lambda b: b[2])

    heights = defaultdict(int)
    supported = defaultdict(lambda: -1)
    supporters = defaultdict(set)
    for b, ((x1, x2), (y1, y2), (z1, z2)) in enumerate(bricks):
        cur = 0
        if y1 != y2:
            cur = max(heights[(x1, y)] for y in range(y1, y2+1))
            for y in range(y1, y2+1):
                if heights[(x1, y)] == cur:
                    supporters[b].add(supported[(x1, y)])
                heights[(x1, y)] = cur + 1
                supported[(x1, y)] = b
        elif x1 != x2:
            cur = max(heights[(x, y1)] for x in range(x1, x2+1))
            for x in range(x1, x2+1):
                if heights[(x, y1)] == cur:
                    supporters[b].add(supported[(x, y1)])
                heights[(x, y1)] = cur + 1
                supported[(x, y1)] = b
        else:
            cur = heights[(x1, y1)]
            if heights[(x1, y1)] == cur:
                supporters[b].add(supported[(x1, y1)])
            heights[(x1, y1)] += z2 - z1 + 1
            supported[(x1, y1)] = b

    
    supporting = defaultdict(set)
    for b, sps in supporters.items():
        for sp in sps:
            if sp == -1: continue
            supporting[sp].add(b)

    result = 0
    for b in range(n):
        dq = deque(supporting[b])
        breaks = set([b])
        while dq:
            b = dq.popleft()

            broken = True
            for spb in supporters[b]:
                if spb == -1: continue
                if spb not in breaks:
                    broken = False
                    break

            if not broken: continue
            breaks.add(b)

            for sp in supporting[b]:
                dq.append(sp)
        result += len(breaks) - 1

    print(result)





            

if __name__ == "__main__":
    main()


