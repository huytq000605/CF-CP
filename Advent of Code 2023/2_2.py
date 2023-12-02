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
    for i, line in enumerate(lines):
        game_id = i+1
        sets = line.split(":")[1].strip()
        max_color_game = Counter()
        for set in sets.split(";"):
            counter = Counter()
            set = set.strip()
            for cube in set.split(","):
                cube = cube.strip()
                num, color = cube.split(" ")
                counter[color] += int(num)
                max_color_game[color] = max(max_color_game[color], counter[color])

        mul = 1
        for color in ["blue", "green", "red"]:
            mul *= max_color_game[color]
        result += mul
    print(result)


if __name__ == "__main__":
    main()

