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
    result = 0
    for line in lines:
        i1, i2 = line.split(",")
        s1, e1 = list(map(int, i1.split("-")))
        s2, e2 = list(map(int, i2.split("-")))
        if min(e1, e2) >= max(s1, s2):
            result += 1
        

    print(result)



if __name__ == "__main__":
    main()
