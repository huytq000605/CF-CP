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

    d = defaultdict()
    for line in lines[2:]:
        u, vs = line.split(" = ")
        v1, v2 = vs[1:-1].split(", ")
        d[u] = [v1, v2]

    i = 0
    dq = deque([('AAA', 0)])
    while True:
        u, s = dq.popleft()
        if u == 'ZZZ':
            print(s)
            return s
        v1, v2 = d[u]
        if instructions[i] == "L":
            dq.append((v1, s+1))
        else:
            dq.append((v2, s+1))
        i += 1
        i %= len(instructions)
    print("???")
    return -1
        

if __name__ == "__main__":
    main()

