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
from copy import copy, deepcopy
def get_int(): return int(input())
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_list(): return list(map(int, sys.stdin.readline().strip().split()))
def get_string(): return sys.stdin.readline().strip()


class BreakOutException(Exception):
    pass


def main():
    lines = sys.stdin.read().splitlines()
    matrix = []

    def process(matrix):
        for lll in matrix:
            print(lll)
        print()

        m, n = len(matrix), len(matrix[0])

        # mirror is horizontal
        for mirror in range(m-1):
            r1, r2 = mirror, mirror + 1
            diff = 0
            while r1 >= 0 and r2 < m and diff <= 1:
                for c in range(n):
                    if matrix[r1][c] != matrix[r2][c]:
                        diff += 1
                r1 -= 1
                r2 += 1
            if diff == 1:
                return ((mirror+1) * 100, "horizontal")
        
        for mirror in range(n-1):
            c1, c2 = mirror, mirror + 1
            diff = 0
            while c1 >= 0 and c2 < n and diff <= 1:
                for r in range(m):
                    if matrix[r][c1] != matrix[r][c2]:
                        diff += 1
                c1 -= 1
                c2 += 1
            if diff == 1:
                return (mirror+1, "vertical")

        return None

        


    result = 0
    for line in lines:
        if line == "":
            res, d = process(matrix)
            result += res
            matrix = []
            continue
        matrix.append(line)

    res, d = process(matrix)
    result += res
    print(result)


if __name__ == "__main__":
    main()

