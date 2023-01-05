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
    n = len(lines)
    for i in range(0, n, 3):
        s1, s2, s3 = set(lines[i]), set(lines[i+1]), set(lines[i+2])
        c = list(set.intersection(s1, s2, s3))[0]
        if c.isupper():
            result += 26
            c = c.lower()
        result += ord(c) - ord('a') + 1
        

    print(result)



if __name__ == "__main__":
    main()
