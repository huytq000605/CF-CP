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
    pq = []
    s = 0
    for line in lines:
        if line == "":
            s = 0
            continue
        s += int(line)
        heappush(pq, s)
        if len(pq) > 3:
            heappop(pq)
    print(sum(pq))



if __name__ == "__main__":
    main()
