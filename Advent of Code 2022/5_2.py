import sys
import collections
from functools import lru_cache
from typing import *
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
    stacks = [[] for _ in range(9)]
    for i, line in enumerate(lines):
        if i == 8 or i == 9:
            continue
        if i < 10:
            nth = 0
            for j in range(1, 35, 4):
                if line[j] != " ":
                    stacks[nth] = [line[j], *stacks[nth]]
                nth += 1
            continue
        line = line.split(" ")
        num = int(line[1])
        fr = int(line[3]) - 1
        to = int(line[-1]) - 1
        tmp = []
        for _ in range(num):
            tmp.append(stacks[fr].pop())
        while tmp:
            stacks[to].append(tmp.pop())
    result = ""
    for s in stacks:
        result += s[-1]
    print(result)



if __name__ == "__main__":
    main()
