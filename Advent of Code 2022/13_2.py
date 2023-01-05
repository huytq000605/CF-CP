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
    def parseLine(line):
        stack = [[]]
        cur = -1
        for c in line:
            if c == "[":
                stack.append([])
            elif c == "]":
                if cur != -1:
                    stack[-1].append(cur)
                    cur = -1
                last = stack.pop()
                stack[-1].append(last)
            elif c == ",":
                if cur != -1:
                    stack[-1].append(cur)
                    cur = -1
            elif c.isdigit():
                if cur == -1:
                    cur = 0
                cur = cur * 10 + int(c)
        stack = stack.pop().pop()
        return stack

    def cmp(e1, e2):
        if not isinstance(e1, list):
            e1 = [e1]
        if not isinstance(e2, list):
            e2 = [e2]

        n = min(len(e2), len(e1))
        for i in range(n):
            if isinstance(e1[i], list) or isinstance(e2[i], list):
                r = cmp(e1[i], e2[i])
                if r == 1:
                    return 1
                elif r == -1:
                    return -1
                continue

            if e1[i] > e2[i]:
                return -1
            if e1[i] < e2[i]:
                return 1
        if len(e1) > len(e2):
            return -1
        if len(e1) < len(e2):
            return 1
        return 0

                
    packets = [[[2]], [[6]]]
    result = 0
    for i, line in enumerate(lines):
        if line == "":
            f, s = parseLine(lines[i+1]), parseLine(lines[i+2])
            packets.append(f)
            packets.append(s)

    n = len(packets)
    for i in range(n):
        for j in range(i+1, n):
            if cmp(packets[i], packets[j]) >= 0:
                packets[i], packets[j] = packets[j], packets[i]
    packets = reversed(packets)

    for i, packet in enumerate(packets):
        if packet == [[2]] or packet == [[6]]:
            print(i+1)
            






if __name__ == "__main__":
    main()
