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
    rules = []
    points = []
    rule_line = True
    for line in lines:
        if line == "":
            rule_line = False
            continue
        if rule_line:
            rules.append(line)
        else:
            points.append(line)
    
    rule_map = dict()
    for rule in rules:
        name, details = rule.split("{")
        details = details[:-1].split(",")
        rule_map[name] = details

    result = 0
    for point in points:
        point = point[1:-1]
        coordinates = point.split(",")
        x, m, a, s = [int(coor[2:]) for coor in coordinates]
        coordinates = {"x": x, "m": m, "a": a, "s": s}
        rule = "in"
        while rule not in "AR":
            for detail in rule_map[rule]:
                if ":" not in detail:
                    rule = detail
                    break
                else:
                    expr, rule = detail.split(":")
                    lhs, rhs = expr[0], int(expr[2:])
                    if expr[1] == "<" and coordinates[lhs] < rhs:
                        break
                    if expr[1] == ">" and coordinates[lhs] > rhs:
                        break
        if rule == "A":
            result += x + m + a + s
    print(result)





if __name__ == "__main__":
    main()

