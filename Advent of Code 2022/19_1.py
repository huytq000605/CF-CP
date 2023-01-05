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
    blueprints = []
    for line in lines:
        line = line.split(" ")
        for i in [6, 12, 18, 21, 27, 30]:
            line[i] = int(line[i])
        i, ore, clay, obsidiant, geode = int(line[1][:-1]), line[6], line[12], (line[18], line[21]), (line[27], line[30])
        blueprints.append([i, ore, clay, obsidiant, geode])

    result = 0
    MAX_MIN = 24
    for blueprint in blueprints:
        idx, ore_cost, clay_cost, obs_cost, geo_cost = blueprint
        @cache(None)
        def dfs(m, ore, clay, obs, geo, ore_r, clay_r, obs_r, geo_r):
            if m == MAX_MIN:
                return geo
            nonlocal ore_cost, clay_cost, obs_cost, geo_cost
            result = 0
            n_ore, n_clay, n_obs, n_geo = ore + ore_r,clay+ clay_r, obs + obs_r, geo + geo_r
            if ore >= clay_cost:
                result = max(result, dfs(m+1, n_ore - clay_cost, n_clay, n_obs, n_geo ,ore_r, clay_r+1, obs_r, geo_r))
            if ore >= ore_cost:
                result = max(result, dfs(m+1, n_ore - ore_cost, n_clay, n_obs, n_geo, ore_r + 1, clay_r, obs_r, geo_r))
            if ore >= obs_cost[0] and clay >= obs_cost[1]:
                result = max(result, dfs(m+1, n_ore - obs_cost[0], n_clay - obs_cost[1], n_obs, n_geo, ore_r, clay_r, obs_r + 1, geo_r))
            if ore >= geo_cost[0] and obs >= geo_cost[1]:
                result = max(result, dfs(m+1, n_ore - geo_cost[0], n_clay, n_obs - geo_cost[1], n_geo, ore_r, clay_r, obs_r, geo_r + 1))
            result = max(result, dfs(m+1, n_ore, n_clay, n_obs, n_geo, ore_r, clay_r, obs_r, geo_r))
            return result
        res = dfs(0, 0, 0, 0, 0, 1, 0, 0, 0)
        print(blueprint, res)
        result += idx * dfs(0, 0, 0, 0, 0, 1, 0, 0, 0)
    print(result)
        




if __name__ == "__main__":
    main()

