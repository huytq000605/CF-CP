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
def get_int(): return int(input())
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_list(): return list(map(int, sys.stdin.readline().strip().split()))
def get_string(): return sys.stdin.readline().strip()

class BreakOutException(Exception):
    pass

def main():
    lines = sys.stdin.read().splitlines()
    MAX = 4000000
    sensors = []
    def merge_intervals(intervals):
        intervals.sort()
        prev = -math.inf
        result = []
        for s, e in intervals:
            if s > prev:
                result.append([s, e])
            else:
                result[-1][1] = max(result[-1][1], e)
            prev = max(prev, e)
        return result

    for line in lines:
        line = line.split(" ")
        sensor = (int(line[2][2:-1]), int(line[3][2:-1]))
        beacon = (int(line[8][2:-1]), int(line[9][2:]))
        distance = abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])
        sensors.append((sensor[0], sensor[1], distance))

    for y in range(MAX+1):
        intervals = []
        for sx, sy, sd in sensors:
            remaining = sd - abs(sy - y)
            if remaining < 0:
                continue
            intervals.append([max(0, sx - remaining), min(MAX, sx + remaining)])
        merged_intervals = merge_intervals(intervals)
        if len(merged_intervals) != 1:
            print((merged_intervals[0][1] + 1) * MAX + y)
            break

        if merged_intervals[0][0] != 0 and merge_intervals[0][1] != MAX:
            break
            


if __name__ == "__main__":
    main()
