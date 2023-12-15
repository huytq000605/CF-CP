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
import ast
def get_int(): return int(input())
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_list(): return list(map(int, sys.stdin.readline().strip().split()))
def get_string(): return sys.stdin.readline().strip()


class BreakOutException(Exception):
    pass


def main():
    lines = sys.stdin.read().splitlines()
    line = lines[0]
    strs = line.split(",")
    def hash(s):
        v = 0
        for c in s:
            v += ord(c)
            v *= 17
            v %= 256
        return v
    
    boxes = [[] for _ in range(256)]
    for s in strs:
        if "-" in s:
            lens = s[:-1]
            box = hash(lens)
            for i, l in enumerate(boxes[box]):
                if l[0] == lens:
                    boxes[box].pop(i)
                    break
        else:
            lens, v = s.split("=")
            box = hash(lens)
            done = False
            for i, l in enumerate(boxes[box]):
                if l[0] == lens:
                    boxes[box][i] = (lens, v)
                    done = True
                    break
            if not done:
                boxes[box].append((lens, v))

    result = 0
    for box in range(256):
        for i, (_, focal) in enumerate(boxes[box]):
            result += (box+1) * (i+1) * int(focal)

    print(result)

    




if __name__ == "__main__":
    main()

