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
        nonlocal low, high
        low += 1
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
                    pulse = True

            # Debug
            # print(u, pulse, graph[u][2:])


            if pulse:
                high += len(graph[u]) - 2
            else:
                low += len(graph[u]) - 2

            for v in graph[u][2:]:
                if v not in graph: continue
                if graph[v][0] == "broadcaster":
                    dq.append((v, pulse))
                elif graph[v][0] == "%" and not pulse:
                    dq.append((v, False))
                elif graph[v][0] == "&":
                    graph[v][1][u] = pulse
                    dq.append((v, pulse))

    low, high = 0, 0
    for _ in range(1000):
        press_button()
        # print()
    print(low*high, low, high)




if __name__ == "__main__":
    main()

