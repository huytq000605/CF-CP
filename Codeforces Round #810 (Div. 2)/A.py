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
        n = get_int()
        print(solve(n))



def solve(n):
    result = [i+2 for i in range(n)]
    result[-1] = 1
    return " ".join(map(str, result))

if __name__ == "__main__":
    main()
