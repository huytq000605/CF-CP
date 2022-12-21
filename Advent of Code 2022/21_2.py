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
    monkeys = dict()
    parents = defaultdict(set)
    for line in lines:
        line = line.split()
        monkey = line[0][:-1]
        if monkey == "humn":
            continue
        operation = False
        for op in "+-*/":
            if op in line:
                operation = True
        if operation:
            left = line[1]
            op = line[2]
            right = line[3]
            if monkey == "root":
                eq1 = left
                eq2 = right
            else:
                monkeys[monkey] = [left, op, right]
                parents[left].add(monkey)
                parents[right].add(monkey)
        else:
            monkeys[monkey] = [int(line[1])]

    def dfs(u):
        if len(monkeys[u]) == 1:
            return monkeys[u][0]
        left = dfs(monkeys[u][0])
        right = dfs(monkeys[u][2])
        op = monkeys[u][1]

        if op == "+":
            result = left + right
        elif op == "-":
            result = left - right
        elif op == "*":
            result = left * right
        else:
            result = left // right
        monkeys[u] = [result]
        return result
    
    def dfs2(u):
        more = set()
        for v in parents[u]:
            for parent in dfs2(v):
                more.add(parent)
        parents[u].update(more)
        return parents[u]
    
    humn_parents = dfs2("humn")

    # dfs(eq1) use one of eq1 or eq2, the one doesn't depend on monkey named humn
    dfs(eq2)

    eq = monkeys[eq2][0]
    u = eq1
    # len == 1 if u == humn
    while u in monkeys:
        print(u)
        left, op, right = monkeys[u]
        if left in humn_parents:
            if op == "+":
                eq = eq - dfs(right)
            elif op == "-":
                eq = eq + dfs(right)
            elif op == "/":
                eq = eq * dfs(right)
            else:
                eq = eq // dfs(right)
            u = left
        else:
            if op == "+":
                eq = eq - dfs(left)
            elif op == "-":
                eq = dfs(left) - eq
            elif op == "/":
                eq = dfs(left) // eq
            else:
                eq = eq // dfs(left)
            u = right
    print(eq)


            


if __name__ == "__main__":
    main()

