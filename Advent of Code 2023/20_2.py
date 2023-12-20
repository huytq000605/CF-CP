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

    graph = defaultdict(list)
    for line in lines:
        u, v = line.split(" -> ")
        if u == "broadcaster":
            graph[u].append("broadcaster")
            graph[u].append(None)
        else:
            module = u[0]
            u = u[1:]
            graph[u].append(module)
            if module == "%":
                graph[u].append(False)
            elif module == "&":
                graph[u].append(dict())

        vs = v.split(", ")
        for v in vs:
            graph[u].append(v)

    for line in lines:
        u, v = line.split(" -> ")
        vs = v.split(", ")
        if u != "broadcaster":
            u = u[1:]
        for v in vs:
            if v not in graph: continue
            if graph[v][0] == "&":
                graph[v][1][u] = False

        


    def press_button():
        nonlocal counter, time
        dq = [("broadcaster", False)]
        dq = deque(dq)
        while dq:
            u, pulse  = dq.popleft()

            if graph[u][0] == "%":
                if pulse:
                    continue
                graph[u][1] = not graph[u][1]
                pulse = graph[u][1]

            if graph[u][0] == "&":
                if all(graph[u][1].values()):
                    pulse = False
                else:
                    if not counter[u] and u in ["rk", "cd", "zf", "qx"]:
                        counter[u] = time
                    pulse = True

            # Debug
            # print(u, pulse, graph[u][2:])

            for v in graph[u][2:]:
                if v == "rx":
                    continue
                if graph[v][0] == "&":
                    graph[v][1][u] = pulse
                dq.append((v, pulse))

    # gh leads to rx
    # rk, cd, zf, qx lead to gh
    counter = Counter()
    time = 0
    while len(counter) < 4:
        time += 1
        press_button()

    print(counter)
    print(math.lcm(*counter.values()))
    


if __name__ == "__main__":
    main()

