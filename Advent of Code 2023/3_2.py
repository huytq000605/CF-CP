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
    ds = [(0,1), (1,0), (0,-1), (-1,0), (1, 1), (-1, -1), (-1, 1), (1, -1)]
    matrix = []
    for line in lines:
        matrix.append(line)

    m, n = len(matrix), len(matrix[0])
    symbols = defaultdict(list)

    def check_num(r, start_c, end_c):
        nonlocal symbols
        adj_symbols = set()
        for c in range(start_c, end_c):
            for dr, dc in ds:
                ar, ac = r + dr, c + dc
                if ar < 0 or ar >= m or ac < 0 or ac >= n:
                    continue
                if not matrix[ar][ac].isdigit() and matrix[ar][ac] != ".":
                    adj_symbols.add((ar, ac))

        for symbol in adj_symbols:
            symbols[symbol].append(num)


    for r in range(m):
        start_c = 0
        num = 0
        is_num = False
        for c in range(n):
            if matrix[r][c].isdigit():
                num = num * 10 + int(matrix[r][c])
                if not is_num:
                    start_c = c
                is_num = True
            else:
                if is_num: check_num(r, start_c, c)
                # reset
                is_num = False
                num = 0

            if c == n-1:
                if is_num: check_num(r, start_c, c)

    result = 0
    for symbol, nums in symbols.items():
        if len(nums) == 2:
            result += nums[0] * nums[1]

    print(result)

    return result

        

if __name__ == "__main__":
    main()

