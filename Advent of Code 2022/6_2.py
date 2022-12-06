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
    freq = defaultdict(int)
    for line in lines:
        for i, c in enumerate(line):
            if i > 13:
                freq[line[i-14]] -= 1
                if freq[line[i-14]] == 0:
                    freq.pop(line[i-14])
            freq[c] += 1
            if len(freq) == 14:
                print(i+1)
                return 



if __name__ == "__main__":
    main()
