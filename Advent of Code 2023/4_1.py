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
    for line in lines:
        card = line.split(": ")[1]
        winner_strs, nums = card.split(" | ")
        winners = set()
        for s in winner_strs.split(" "):
            s = s.strip()
            if s == "": continue
            winners.add(int(s))
        points = 0
        for num in nums.split(" "):
            num = num.strip()
            if num == "": continue
            num = int(num)
            if num in winners:
                points = max(points + 1, points * 2)
        result += points
    print(result)
    return result

        

if __name__ == "__main__":
    main()

