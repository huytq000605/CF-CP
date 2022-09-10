from functools import lru_cache
from collections import Counter, defaultdict
import math
from heapq import *

import sys
def get_int(): return int(sys.stdin.readline().strip())
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_list(): return list(map(int, sys.stdin.readline().strip().split()))
def get_string(): return sys.stdin.readline().strip()

def main():
    testcases = get_int()
    for i in range(testcases):
        n, m, k = get_ints()
        a = get_list()
        print(solve(n, m, k, a))



def solve(n, m, k, a):
    def can_print(each, target, arr):
        max_used = list(filter(lambda ele: ele >= 2, map(lambda ele: ele // each, arr)))
        # Gurantee to have enough
        if sum(max_used) >= target:
            if target % 2 == 0:
                return True
            # Example: target = 5, max_used = [2,2,2]
            # We need to have at least 1 odd result from max_used
            else:
                for num in max_used:
                    if num > 2:
                        return True
        return False
            

    if can_print(m, n, a) or can_print(n, m, a):
        return "Yes"
    return "No"


if __name__ == "__main__":
    try:
        main()
    except BaseException as e:
        print(e)
