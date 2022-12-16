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
    Y = 2000000
    seen = set()
    sensors = set()
    beacons = set()
    for line in lines:
        line = line.split(" ")
        sensor = (int(line[2][2:-1]), int(line[3][2:-1]))
        beacon = (int(line[8][2:-1]), int(line[9][2:]))
        sensors.add(sensor)
        beacons.add(beacon)
        distance = abs(sensor[1] - beacon[1]) + abs(sensor[0] - beacon[0])
        diff_y = abs(sensor[1] - Y)
        remaining = distance - diff_y
        if remaining <= 0:
            continue
        min_x, max_x = sensor[0] - remaining, sensor[0] + remaining
        seen.update({(i, Y) for i in range(min_x, max_x + 1)})
    result = len(seen)
    for ele in seen:
        if ele in beacons or ele in sensors:
            result -= 1
    print(result)

if __name__ == "__main__":
    main()
