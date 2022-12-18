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


sys.setrecursionlimit(10000)

class BreakOutException(Exception):
    pass

def main():
    lines = sys.stdin.read().splitlines()
    cubes = []
    for line in lines:
        x, y, z = map(int, line.split(","))
        cubes.append((x, y, z))
    n = len(cubes)
    grid = [[[-1 for _ in range(20)] for _ in range(20)] for _ in range(20)]
    for x, y, z in cubes:
        grid[x][y][z] = 1
    ds = ((0, 0, -1), (0, 0, 1), (0, -1, 0), (0, 1, 0), (-1, 0, 0), (1, 0, 0))

    def dfs(x, y, z):
        if grid[x][y][z] != -1:
            return
        print(x, y, z)
        grid[x][y][z] = 0
        for dx, dy, dz in ds:
            nx, ny, nz = x + dx, y + dy, z + dz
            if nx < 0 or ny < 0 or nz < 0 or nx >= 20 or ny >= 20 or nz >= 20:
                continue
            if grid[nx][ny][nz] != -1:
                continue
            dfs(nx, ny, nz)

    for i in range(20):
        dfs(0, 0, i)
        dfs(19, 19, i)
        dfs(0, i, 0)
        dfs(19, i, 19)
        dfs(i, 0, 0)
        dfs(19, 0, 0)

    def exterior(cube):
        ox, oy, oz = cube
        res = 0
        for dx, dy, dz in ds:
            x, y, z = ox, oy, oz
            meet_water = False
            while True:
                x, y, z = x + dx, y + dy, z + dz
                if x < 0 or y < 0 or z < 0 or x >= 20 or y >= 20 or z >= 20 or grid[x][y][z] == 0:
                    meet_water = True
                    break
                if grid[x][y][z] == 1:
                    break
            if meet_water:
                res += 1
        print(cube, res)
        return res


    
    result = 0
    for cube in cubes:
        result += exterior(cube)
    print(result)
    return result


if __name__ == "__main__":
    main()

