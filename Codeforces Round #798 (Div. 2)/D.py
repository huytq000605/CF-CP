from functools import lru_cache
from collections import Counter, defaultdict
import math
from heapq import *

import sys
def get_int(): return int(input())
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_list(): return list(map(int, sys.stdin.readline().strip().split()))
def get_string(): return sys.stdin.readline().strip()

def main():
    testcases = get_int()
    for i in range(testcases):
        n, m = get_ints()
        matrix = [0 for i in range(n)]
        for j in range(n):
            matrix[j] = get_string()
        print(solve(matrix, n, m))



def solve(matrix, n, m):
    # a, b is the cell we choose
    # xi, yi are the black cells
    # distance = max(abs(a-xi) + abs(b-yi)) 
    # choose the cell where distance is minimum
    # We have 4 situtations:
    # a > xi and b > yi => distance = a-xi + b-yi = (a+b) - (xi + yi) => max(distance) when (xi+yi) min
    # a < xi and b > yi => distance = xi-a + b-yi = (b-a) + (xi - yi) => max(distance) when (xi-yi) max
    # a > xi and b < yi => distance = a-xi + yi-b = (a-b) - (xi - yi) => max(distance) when (xi-yi) min
    # a < xi and b < yi => distance = xi-a + yi-b = (-a-b) + (xi + yi) => max(distance) when (xi+yi) max

    sum_max = (-math.inf, 0, 0)
    sum_min = (math.inf, 0, 0)
    diff_min = (math.inf, 0, 0)
    diff_max = (-math.inf, 0, 0)

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == "B":
                if i + j > sum_max[0]:
                    sum_max = (i + j, i, j)
                if i + j < sum_min[0]:
                    sum_min = (i + j, i, j)
                if i - j > diff_max[0]:
                    diff_max = (i - j, i, j)
                if i - j < diff_min[0]:
                    diff_min = (i - j, i, j)
    min_distance = math.inf
    result = (-1, -1)

    for i in range(n):
        for j in range(m):
            distance = 0
            for _, row, col in [sum_max, sum_min, diff_min, diff_max]:
                distance = max(distance, abs(row - i) + abs(col - j))
            if distance < min_distance:
                min_distance = distance
                result = (i+1, j+1)
    return " ".join(map(str, result))

            


if __name__ == "__main__":
    main()
