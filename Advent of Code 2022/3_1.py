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
        n = len(line)
        s = set(line[:n//2])
        for c in line[n//2:]:
            if c in s:
                bonus = 0
                if c.isupper():
                    bonus = 26
                    c = c.lower()
                result += ord(c) - ord('a') + 1 + bonus
                break

    print(result)



if __name__ == "__main__":
    main()
