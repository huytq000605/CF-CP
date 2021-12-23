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
    n = len(lines)
    cmd = []
    for line in lines:
        line = line.split()
        cmd.append(list(int(d) for d in re.findall(r'-?\d+', line[1])))
        if line[0] == "on":
            cmd[-1].append(1)
        else:
            cmd[-1].append(0)
    print(solve(cmd))



class BreakOutException(Exception):
	pass


def solve(cmd):
    X,Y,Z = set(), set(), set()
    for i , (x1, x2, y1, y2, z1, z2, on) in enumerate(cmd):
        cmd[i][1] += 1
        cmd[i][3] += 1
        cmd[i][5] += 1
        X.add(x1)
        X.add(x2+1)
        Y.add(y1)
        Y.add(y2+1)
        Z.add(z1)
        Z.add(z2+1)


    grid = [[[0 for k in range(len(Z))] for j in range(len(Y))] for i in range(len(X))]
    X,Y,Z = [sorted(list(A)) for A in [X,Y,Z]]


    def get_index(A, value):
        start = 0
        end = len(A) - 1
        while start < end:
            mid = start + (end - start) // 2
            if A[mid] >= value:
                end = mid
            else:
                start = mid + 1
        return start


    for c in cmd:
        x1,x2,y1,y2,z1,z2 = [get_index(A, value) for A, value in zip([X,X,Y,Y,Z,Z], c[:6])]

        for i in range(x1, x2):
            for j in range(y1, y2):
                for k in range(z1, z2):
                    grid[i][j][k] = c[6]


    result = 0
    
    for i in range(len(X)-1):
        for j in range(len(Y)-1):
            for k in range(len(Z)-1):
                if grid[i][j][k] == 1:
                    result += (X[i+1] - X[i]) * (Y[j+1] - Y[j]) * (Z[k+1] - Z[k])

    return result

	
if __name__ == "__main__":
	main()
