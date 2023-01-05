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
    X = 1
    cycle = 0
    result = 0
    for line in lines:
        if line.startswith("addx"):
            value = int(line[5:])
            cycle += 1
            if cycle == 20 or (cycle > 20 and (cycle - 20) % 40 == 0):
                print(cycle, X)
                result += X * cycle
            cycle += 1
            if cycle == 20 or (cycle > 20 and (cycle - 20) % 40 == 0):
                print(cycle, X)
                result += X * cycle
            X += value
        else:
            cycle += 1
            if cycle == 20 or (cycle > 20 and (cycle - 20) % 40 == 0):
                print(cycle, X)
                result += X * cycle
    print(result)









if __name__ == "__main__":
    main()
