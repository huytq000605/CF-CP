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
    times = [40, 81, 77, 72]
    distances = [219, 1012, 1365, 1080]

    ways = 1
    for i in range(len(times)):
        time, d = times[i], distances[i]
        w = 0
        for hold in range(time):
            time_left = time - hold
            speed = hold
            if speed * time_left > d:
                w += 1
        ways *= w
    print(ways)
    return
        
        

if __name__ == "__main__":
    main()

