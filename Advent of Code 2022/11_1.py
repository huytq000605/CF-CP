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
    monkeys = []
    n = len(lines)
    i = 0
    while i < n:
        line = lines[i]
        if line.startswith("Monkey"):
            i += 1
            items = map(int, lines[i].split(":")[-1].strip().split(","))
            monkeys.append(list(items))
        i += 1
    inspected = [0 for i in range(8)]
    testcases = [(13, 1, 7), (7, 3, 6), (3, 5, 4), (19, 2, 6), (5, 0, 5), (2, 7, 0), (11, 2, 4), (17, 1, 3)]

    def test(item, monkey):
        nonlocal testcases, monkeys
        div, t, f = testcases[monkey]
        if item % div == 0:
            monkeys[t].append(item)
        else:
            monkeys[f].append(item)

    for turn in range(20):
        for monkey in range(8):
            items = monkeys[monkey]
            inspected[monkey] += len(items)
            for item in items:
                if monkey == 0:
                    item *= 11
                elif monkey == 1:
                    item = item + 1
                elif monkey == 2:
                    item = item * item
                elif monkey == 3:
                    item += 2
                elif monkey == 4:
                    item += 6
                elif monkey == 5:
                    item += 7
                elif monkey == 6:
                    item *= 7
                elif monkey == 7:
                    item += 8
                item //= 3
                test(item, monkey)
            monkeys[monkey] = []
    print(inspected)


if __name__ == "__main__":
    main()
