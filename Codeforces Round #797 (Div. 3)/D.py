from functools import lru_cache as cache
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
        n, k = get_ints()
        paper = get_string()
        print(solve(paper, n, k))


def solve(paper, n, k):
    result = math.inf
    current_black = 0
    for i in range(k):
        if paper[i] == "B":
            current_black += 1
    result = min(result, k - current_black)
    for i in range(k, n):
        if paper[i-k] == "B":
            current_black -= 1
        if paper[i] == "B":
            current_black += 1
        result = min(result, k - current_black)
    return result


if __name__ == "__main__":
    main()
