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
    result = 0
    for line in lines:
        nums = list(map(int, line.split(" ")))
        rounds = [[*nums]]
        while any(num != 0 for num in nums):
            nums = [nums[i+1] - nums[i] for i in range(len(nums)-1)]
            rounds.append([*nums])
        last = 0
        for i in range(len(rounds) - 2, -1, -1):
            last += rounds[i][-1]
        result += last
    
    print(result)



        
        

if __name__ == "__main__":
    main()

