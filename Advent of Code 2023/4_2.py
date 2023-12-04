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
    result = 0
    instances = 1
    minus = defaultdict(int)
    for i, line in enumerate(lines):
        card = line.split(": ")[1]
        winner_strs, nums = card.split(" | ")
        winners = set()

        instances += minus[i]
        result += instances

        for s in winner_strs.split(" "):
            s = s.strip()
            if s == "": continue
            winners.add(int(s))

        winning = 0
        for num in nums.split(" "):
            num = num.strip()
            if num == "": continue
            num = int(num)
            if num in winners:
                winning += 1

        minus[i + winning + 1] -= instances
        instances += instances
    print(result)
    return result

        

if __name__ == "__main__":
    main()

