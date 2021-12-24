import sys
import collections
from functools import lru_cache
from typing import *
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

def main():
    lines = sys.stdin.read().splitlines()
    ins = []
    for line in lines:
        ins.append(line.split())

    # print(ins)

    print(solve(ins))



class BreakOutException(Exception):
	pass


def solve(ins):
    w = x = y = z = 0
    digits = []
    for i in ins:
        if i[0] == 'inp':
            digits.append([])
        else:
            digits[-1].append(i)

    result = ""

    def add(a,b):
        return int(a) + int(b)
    
    def mul(a,b):
        return int(a) * int(b)

    def div(a,b):
        a, b = int(a), int(b)
        if a * b < 0:
            return int(math.ceil(a / b))
        else:
            return a // b
    
    def mod(a,b):
        a, b = int(a), int(b)
        return int(math.fmod(a, b))
    
    @lru_cache(None)
    def dfs(ith, x, y, z):
        print(ith)
        if ith == 14:
            if z == 0:
                return ''
            else:
                return 'F'

        for w in range(9, 0, -1):
            values = {'x': x, 'y': y, 'z': z, 'w': w}
            for op, a, b in digits[ith]:
                if op == "add":
                    if b.isnumeric() or len(b) >= 2:
                        values[a] = add(values[a], b)
                    else:
                        values[a] = add(values[a], values[b])
                elif op == "mul":
                    if b.isnumeric() or len(b) >= 2:
                        values[a] = mul(values[a], b)
                    else:
                        values[a] = mul(values[a], values[b])
                elif op == "div":
                    if b.isnumeric() or len(b) >= 2:
                        values[a] = div(values[a], b)
                    else:
                        values[a] = div(values[a], values[b])
                elif op == "mod":
                    if b.isnumeric() or len(b) >= 2:
                        values[a] = mod(values[a], b)
                    else:
                        values[a] = mod(values[a], values[b])
                elif op == "eql":
                    if b.isnumeric() or len(b) >= 2:
                        if values[a] == int(b):
                            values[a] = 1
                        else:
                            values[a] = 0
                    else:
                        if values[a] == values[b]:
                            values[a] = 1
                        else:
                            values[a] = 0
            result = dfs(ith + 1, values['x'], values['y'], values['z'])
            if result != "F":
                return str(w) + result

        return "F"
    return dfs(0, 0, 0, 0)







	
if __name__ == "__main__":
	main()
