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
    m, n = 2000, 2000
    points = [(1000, 1000) for i in range(10)]
    ds = {"L": (0, -1), "R": (0, 1), "U": (-1, 0), "D": (1, 0)}
    seen = set([(1000, 1000)])
    for line in lines:
        d, steps = line.split()
        steps = int(steps)
        for _ in range(steps):
            dr, dc = ds[d]
            points[0] = (points[0][0] + dr, points[0][1] + dc)
            for i in range(9):
                H, T = points[i], points[i+1]
                distance = max(abs(T[0] - H[0]), abs(T[1] - H[1]))
                if distance >= 2:
                    dr, dc = 0, 0
                    if T[0] < H[0]:
                        dr = 1
                    elif T[0] > H[0]:
                        dr = -1

                    if T[1] < H[1]:
                        dc = 1
                    elif T[1] > H[1]:
                        dc = -1

                    T = (T[0] + dr, T[1] + dc)
                points[i+1] = T
                if i == 8:
                    seen.add(points[-1])
    print(len(seen))






if __name__ == "__main__":
    main()
