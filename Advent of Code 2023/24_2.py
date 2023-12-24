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
# pip3 install z3-solver
import z3
def get_int(): return int(input())
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_list(): return list(map(int, sys.stdin.readline().strip().split()))
def get_string(): return sys.stdin.readline().strip()


class BreakOutException(Exception):
    pass

def main():
    input_lines = sys.stdin.read().splitlines()

    lines = []
    for input_line in input_lines:
        p, u = input_line.split(" @ ")
        px, py, pz = map(lambda s: int(s.strip()), p.split(","))
        ux, uy, uz = map(lambda s: int(s.strip()), u.split(","))
        p = (px, py, pz)
        u = (ux, uy, uz)
        lines.append((p, u))

    import z3
    # note - these are actually all ints in the solution, but typing them as reals makes Z3 work faster
    x, y, z, vx, vy, vz = z3.Reals("x y z vx vy vz")
    solver = z3.Solver()
    for k, line in enumerate(lines[:3]):
        tK = z3.Real(f"t{k}")
        p, u = line
        px, py, pz = p
        ux, uy, uz = u
        solver.add(tK >= 0)
        solver.add(x + tK * vx == px + tK * ux)
        solver.add(y + tK * vy == py + tK * uy)
        solver.add(z + tK * vz == pz + tK * uz)
    solver.check()
    model = solver.model()
    result = sum(model[v].as_long() for v in [x, y, z])
    print(result)

        
if __name__ == "__main__":
    main()



