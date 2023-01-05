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
    sprite = 1
    result = 0
    CRT = [["." for j in range(40)] for i in range(6)]
    cycle = 0

    def valid():
        return abs(cycle % 40 - sprite) <= 1


    for line in lines:
        if line.startswith("addx"):
            value = int(line[5:])
            if valid():
                CRT[cycle // 40][cycle % 40] = "#"
            cycle += 1
            if valid():
                CRT[cycle // 40][cycle % 40] = "#"
            cycle += 1
            sprite += value
        else:
            if valid():
                CRT[cycle // 40][cycle % 40] = "#"
            cycle += 1
    for CRTr in CRT:
        print(CRTr)









if __name__ == "__main__":
    main()
