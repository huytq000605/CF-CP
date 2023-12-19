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

    stack = [{"rule": "in", "x": (1,4000), "m": (1, 4000), "a": (1, 4000), "s":(1, 4000)}]
    finished = []
    while stack:
        point = stack.pop()
        rule = point["rule"]
        if rule in "AR":
            finished.append(point)
            continue
        for detail in rule_map[rule]:
            if ":" not in detail:
                rule = detail
                point["rule"] = rule
                stack.append(point)
                break
            else:
                expr, rule = detail.split(":")
                lhs, rhs = expr[0], int(expr[2:])
                if expr[1] == "<":
                    if point[lhs][1] < rhs:
                        point["rule"] = rule
                        stack.append(point)
                        break
                    elif point[lhs][0] < rhs:
                        copy_point = dict(point)
                        copy_point[lhs] = (point[lhs][0], rhs - 1)
                        copy_point["rule"] = rule
                        point[lhs] = (rhs, point[lhs][1])
                        stack.append(copy_point)
                elif expr[1] == ">":
                    if point[lhs][0] > rhs:
                        point["rule"] = rule
                        stack.append(point)
                        break
                    elif point[lhs][1] > rhs:
                        copy_point = dict(point)
                        copy_point[lhs] = (rhs + 1, point[lhs][1])
                        point[lhs] = (point[lhs][0], rhs)
                        stack.append(copy_point)

            
    # print(finished)
    result = 0
    for point in finished:
        count = 0
        if point["rule"] == "A":
            count = 1
            for c in "xmas":
                if point[c][1] >= point[c][0]:
                    count *= point[c][1] - point[c][0] + 1
                else:
                    exit("invalid, exit...")
                    count = 0
        result += count
    print(result)





if __name__ == "__main__":
    main()

