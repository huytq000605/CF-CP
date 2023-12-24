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
    input_lines = sys.stdin.read().splitlines()

    lines = []
    x_ranges = []
    y_ranges = []
    for input_line in input_lines:
        p, u = input_line.split(" @ ")
        px, py, pz = map(lambda s: int(s.strip()), p.split(","))
        ux, uy, uz = map(lambda s: int(s.strip()), u.split(","))
        p = (px, py, pz)
        u = (ux, uy, uz)
        
        # 2d
        nx, ny = uy, -ux
        c = -nx * px - ny * py
        # ax + by + c = 0
        lines.append((nx, ny, c, p, u))

    n = len(lines)
    test_range = [200000000000000, 400000000000000]
    # test_range = [7, 27]
    result = 0
    for i in range(n):
        a1, b1, c1, p1, u1 = lines[i]
        for j in range(i+1, n):
            a2, b2, c2, p2, u2 = lines[j]

            if a1 / a2 == b1 / b2:
                if c1 / c2 == a1 / a2:
                    print(a1, b1, c1, "~", a2, b2, c2)
                    result += 1
                continue

            # a1x + b1y + c1 = 0
            # a2x + b2y + c2 = 0

            # a1*b2*x + b1*b2*y + b2*c1 = 0
            # b1*a2*x + b1*b2*y + b1*c2 = 0
            # (a1 * b2 - b1 * a2) * x = b1 * c2 - b2 * c1

            # a1*a2*x + b1*a2*y + c1*a2 = 0
            # a2*a1*x + b2*a1*y + c2*a1 = 0
            x = (b1 * c2 - b2 * c1) / (a1 * b2 - b1 * a2)
            y = (c2 * a1 - c1 * a2) / (b1 * a2 - b2 * a1)

            # p1[0] + u1[0] * k = x
            # k = (x- p1[0])/u1[0]
            if test_range[0] <= x <= test_range[1] and\
                test_range[0] <= y <= test_range[1] and\
                (x - p1[0]) // u1[0] >= 0 and (y - p1[1]) // u1[1] >= 0 and\
                (x - p2[0]) // u2[0] >= 0 and (y - p2[1]) // u2[1] >= 0:
                    result += 1
    print(result)






if __name__ == "__main__":
    main()



