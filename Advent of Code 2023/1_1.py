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
    s = 0
    for line in lines:
        first = None
        last = None
        for c in line:
            if not c.isdigit(): continue
            if first is None:
                first = int(c)
            last = int(c)

        s += first * 10 + last

    print(s)








if __name__ == "__main__":
    main()

