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

def main():
    lines = sys.stdin.read().splitlines()
    arr = [["#" for j in range(13)] for i in range(5)]
    for row, line in enumerate(lines):
        for col, value in enumerate(line):
            arr[row][col] = value


    print(solve(arr))



class BreakOutException(Exception):
	pass

def print_arr(arr):
    for row in range(len(arr)):
        print(''.join(arr[row]))
    print()


def solve(arr):
    result = 0
    arr[1][11] = "B"
    arr[1][10] = "B"
    arr[2][9] = "."
    arr[3][9] = "."
    result += 10 * 3
    result += 10 * 3
    print_arr(arr)


    arr[3][9] = "D"
    arr[2][7] = "."
    arr[2][3] = "."
    arr[2][9] = "D"
    result += 1000 * 5
    result += 1000 * 8
    print_arr(arr)


    arr[1][8] = "A"
    arr[3][7] = "."
    result += 3
    print_arr(arr)

    arr[3][7] = "C"
    arr[2][7] = "C"
    arr[2][5] = "."
    arr[3][3] = "."
    result += 100 * 5
    result += 100 * 7
    print_arr(arr)

    arr[3][3] = "A"
    arr[3][5] = "."
    arr[2][3] = "A"
    arr[1][8] = "."
    result += 6
    result += 6
    print_arr(arr)

    arr[3][5] = "B"
    arr[2][5] = "B"
    arr[1][11] = "."
    arr[1][10] = "."
    result += 10 * 7
    result += 10 * 7
    print_arr(arr)

    return result

	
if __name__ == "__main__":
	main()
