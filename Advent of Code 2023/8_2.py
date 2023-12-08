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
    instructions = lines[0]

    starts = []
    d = defaultdict()
    for line in lines[2:]:
        u, vs = line.split(" = ")
        v1, v2 = vs[1:-1].split(", ")
        d[u] = [v1, v2]
        if u[-1] == 'A':
            starts.append(u)

    results = []
    for start in starts:
        i = 0
        s = 0
        stack = [start]
        while stack:
            u = stack.pop()
            if u[-1] == 'Z':
                results.append(s)
                break
            v1, v2 = d[u]
            if instructions[i] == "L":
                stack.append(v1)
            else:
                stack.append(v2)
            i += 1
            i %= len(instructions)
            s += 1
    lcm = results[0]
    mul = 1
    for num in results:
        lcm = math.lcm(lcm, num)
    print(lcm)
    return -1
        

if __name__ == "__main__":
    main()

