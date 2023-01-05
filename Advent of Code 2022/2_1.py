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
    m = {"A": "R", "B": "P", "C": "S", "X": "R", "Y": "P", "Z": "S"}
    points = {"R": 1, "P": 2, "S": 3}
    lines = sys.stdin.read().splitlines()
    result = 0 
    for line in lines:
        opp = m[line[0]]
        me = m[line[2]]
        if opp == me:
            result += 3
        elif opp == "R" and me == "P":
            result += 6
        elif opp == "P" and me == "S":
            result += 6
        elif opp == "S" and me == "R":
            result += 6
        result += points[me]
        
    print(result)



if __name__ == "__main__":
    main()
