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

    mn_r, mn_c, mx_r, mx_c = math.inf, math.inf, -math.inf, -math.inf

    result = 0
    x1, y1 = 0, 0
    outer = 0
    # Shoelace algorithm
    for line in lines:
        _, _, hexi = line.split(" ")
        hexi = hexi[2:-1]
        s = int("0x" + hexi[:5], 16)
        # print(s)
        dx, dy = 0, 0
        if hexi[-1] == "0":
            dx = s
        elif hexi[-1] == "1":
            dy = s
        elif hexi[-1] == "2":
            dx = -s
        elif hexi[-1] == "3":
            dy = -s
        outer += abs(dx) + abs(dy)
        x2, y2 = x1 + dx, y1 + dy
        result += (y1 + y2) * (x1 - x2)
        x1, y1 = x2, y2
    result += y1*(-x1)
    result += outer
    result //= 2
    result += 1
    print(outer)



        #print("".join(lll))
    print(result)



if __name__ == "__main__":
    main()

