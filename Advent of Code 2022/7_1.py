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
    fs = dict()
    cur = fs
    idx = 0
    while idx < len(lines):
        line = lines[idx]
        if line.startswith("$ cd"):
            d = line.split(" ")[-1]
            if d == "/":
                cur = fs
            elif d == "..":
                cur = cur["parent"]
            else:
                cur = cur[d]
        elif line.startswith("$ ls"):
                idx += 1
                while idx < len(lines) and not lines[idx].startswith("$"):
                    t, name = lines[idx].split(" ")
                    if t == "dir":
                        cur[name] = dict()
                        cur[name]["parent"] = cur
                    else:
                        if "ffff" not in cur:
                            cur["ffff"] = 0
                        cur["ffff"] += int(t)
                    idx += 1
                continue
        idx += 1
    
    result = 0
    def dfs(cur):
        nonlocal result
        size = 0
        for k, v in cur.items():
            if k == "parent":
                continue
            if k == "ffff":
                size += v
                continue
            size += dfs(cur[k])
        if size <= 100000:
            result += size
        return size
            

    dfs(fs)
    print(result)






if __name__ == "__main__":
    main()
