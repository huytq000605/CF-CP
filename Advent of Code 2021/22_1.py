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

def main():
    lines = sys.stdin.read().splitlines()
    n = len(lines)
    cmd = []
    for line in lines:
        line = line.split(" ")
        cmd.append(list(int(d) for d in re.findall(r'-?\d+', line[1])))
        if line[0] == "on":
            cmd[-1].append(1)
        else:
            cmd[-1].append(0)
    print(solve(cmd))



class BreakOutException(Exception):
	pass

def solve(cmd):
    grid = [[[0 for k in range(102)] for j in range(102)] for i in range(102)]
    result = 0
    for c in cmd:
        try:
            for value in c:
                if value > 50 or value < -50:
                    raise BreakOutException
        except BreakOutException:
            continue

        for i in range(len(c) - 1):
            c[i] += 50

        
        for x in range(c[0], c[1] + 1):
            for y in range(c[2], c[3] + 1):
                for z in range(c[4], c[5] + 1):
                    grid[x][y][z] = c[6]
    
    for x in range(101):
        for y in range(101):
            for z in range(101):
                if grid[x][y][z] == 1:
                    result += 1
    return result


	
if __name__ == "__main__":
	main()
