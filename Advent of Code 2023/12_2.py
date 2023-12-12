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

    def calculate(line, groups):
        @cache
        def dfs(i, j, cur):
            if i >= len(line):
                if cur > 0:
                    if j < len(groups) and groups[j] == cur:
                        j += 1
                    else:
                        return 0
                if j < len(groups):
                    return 0
                return 1
            
            if j < len(groups) and cur > groups[j]:
                return 0
            
            if line[i] == ".":
                if cur:
                    if j < len(groups) and groups[j] == cur:
                        j += 1
                        cur = 0
                    else:
                        return 0
                return dfs(i+1, j, cur)
            elif line[i] == "#":
                return dfs(i+1, j, cur + 1)
            else:
                result = dfs(i+1, j, cur + 1)
                if not cur:
                    result += dfs(i+1, j, cur)
                elif j < len(groups) and groups[j] == cur:
                    result += dfs(i+1, j+1, 0)
                return result
        return dfs(0, 0, 0)



    result = 0
    for line in lines:
        line, groups = line.split(" ")

        new_line, new_groups = "", ""
        for _ in range(5):
            new_line += "?"
            new_line += line

            new_groups += ","
            new_groups += groups

        line, groups = new_line[1:], new_groups[1:]
        groups = list(map(int, groups.split(",")))
        print(line, groups)

        result += calculate(line, groups)
    print(result)
    return result


if __name__ == "__main__":
    main()

