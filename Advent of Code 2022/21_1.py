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
    for line in lines:
        line = line.split()
        monkey = line[0][:-1]
        operation = False
        for op in "+-*/":
            if op in line:
                operation = True
        print(line)
        if operation:
            left = line[1]
            op = line[2]
            right = line[3]
            monkeys[monkey] = [left, op, right]
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

    for monkey in monkeys.keys():
        dfs(monkey)
    print(monkeys["root"])

            


if __name__ == "__main__":
    main()

