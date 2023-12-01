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
    digits = ["one", "two", "three", "four", "five", "six", "seven" ,"eight", "nine"]
    for line in lines:
        first = None
        last = None
        cur = ""
        i = 0
        while i < len(line):
            if line[i].isdigit():
                if first is None:
                    first = int(line[i])
                last = int(line[i])
            else:
                for j, digit in enumerate(digits):
                    if line[i:i+len(digit)] == digit:
                        i += len(digit) - 2
                        if first is None:
                            first = j + 1
                        last = j + 1
                        break
            i += 1

        s += first * 10 + last

    print(s)








if __name__ == "__main__":
    main()

