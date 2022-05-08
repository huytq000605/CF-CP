from functools import lru_cache as cache
from collections import Counter
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
        s = get_string()
        print(solve(s))


def solve(s):
    if s[-1] != "B":
        return "NO"
    A = 0
    B = 0
    for l in s:
        if l == "A":
            A += 1
        else:
            B += 1
            if B > A:
                return "NO"
    return "YES"

if __name__ == "__main__":
    main()