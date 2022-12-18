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
    cubes = []
    for line in lines:
        x, y, z = map(int, line.split(","))
        cubes.append((x, y, z))
    n = len(cubes)
    result = 6*n

    def connected(c1, c2):
        x1, y1, z1 = c1
        x2, y2, z2 = c2
        if abs(x1 - x2) == 1 and y1 == y2 and z1 == z2:
            return True
        if abs(y1 - y2) == 1 and x1 == x2 and z1 == z2:
            return True
        if abs(z1 - z2) == 1 and x1 == x2 and y1 == y2:
            return True
        return False
    
    for i in range(n):
        for j in range(i+1, n):
            if connected(cubes[i], cubes[j]):
                result -= 2
    print(result)
    return result


if __name__ == "__main__":
    main()

