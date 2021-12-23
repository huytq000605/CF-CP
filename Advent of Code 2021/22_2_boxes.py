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
        line = line.split(" ")
        cmd.append(list(int(d) for d in re.findall(r'-?\d+', line[1])))
        if line[0] == "on":
            cmd[-1].append(1)
        else:
            cmd[-1].append(0)
    print(solve(cmd))



class BreakOutException(Exception):
	pass

def is_empty(pos):
    if pos[0] == 0 and pos[1] == 0:
        return True
    if pos[2] == 0 and pos[3] == 0:
        return True
    if pos[4] == 0 and pos[5] == 0:
        return True
    return False

def crop(other, self):
    x1, x2, y1, y2, z1, z2 = self
    a1, a2, b1, b2, c1, c2 = other

    min_x, max_x = max(x1, a1), min(x2, a2)
    min_y, max_y = max(y1, b1), min(y2, b2)
    min_z, max_z = max(z1, c1), min(z2, c2)

    if min_x > max_x or min_y > max_y or min_z > max_z:
        return (0,0,0,0,0,0)

    return (min_x, max_x, min_y, max_y, min_z, max_z)



class Box:
    def __init__(self, pos):
        self.pos = pos
        self.boxes = []
        self.empty = False

    def subtract(self, other):
        if self.empty:
            return

        cropped = crop(other, self.pos)

        if cropped == self.pos:
            self.empty = True
            return

        if is_empty(cropped) or self.empty:
            return

        box = Box(cropped)
        next_boxes = []

        for inner in self.boxes:
            inner.subtract(cropped)
            if inner.volume() > 0:
                next_boxes.append(inner)

        next_boxes.append(box)
        self.boxes = next_boxes

    def volume(self):
        if self.empty:
            return 0
        total = 1
        total *= (self.pos[1] - self.pos[0] + 1) * (self.pos[3] - self.pos[2] + 1) * (self.pos[5] - self.pos[4] + 1)
        return total - sum(box.volume() for box in self.boxes)



def solve(cmd):
    print(cmd)
    boxes = []
    for c in cmd:
        on = c[6] == 1

        for box in boxes:
            box.subtract(c[:6])

        if on:
            box = Box(c[:6])
            boxes.append(box)

    return sum(box.volume() for box in boxes)
            

	
if __name__ == "__main__":
	main()
