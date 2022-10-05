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
    for tc in range(testcases):
        n, l = get_ints()
        nums = get_list()
        print(solve(nums, n, l))



def solve(nums, n, l):
    result = 0
    for digit in range(l):
        set_bit = 0
        for num in nums:
            if (num >> digit) & 1:
                set_bit += 1
        if set_bit > (n- set_bit):
            result |= (1<<digit)
    return result



if __name__ == "__main__":
    main()
