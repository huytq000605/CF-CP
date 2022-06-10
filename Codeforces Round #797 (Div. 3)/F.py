from functools import lru_cache as cache
from collections import Counter, defaultdict
import math
from heapq import *

import sys
def get_int(): return int(input())
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_list(): return list(map(int, sys.stdin.readline().strip().split()))
def get_string(): return sys.stdin.readline().strip()

def main():
    testcases = get_int()
    for i in range(testcases):
        n = get_int()
        s = get_string()
        p = get_list()
        print(solve(n, s, p))

def solve(n, s, p):
    # Maybe better to use union find
    done = set()
    # groups are circles
    groups = []
    for i in range(n):
        group = []
        if i in done:
            continue
        done.add(i)
        group.append(i)
        cur = p[i] - 1
        group.append(cur)
        done.add(cur)
        while cur != i:
            cur = p[cur] - 1
            group.append(cur)
            done.add(cur)
        group.pop() # Last element is i
        groups.append(group)
    
    result = 1
    for group in groups:
        st = ""
        for i in group:
            st += s[i]
        original = st
        st += st
        i = 1
        while st[i:i + len(original)] != original:
            i += 1
        result = lcm(result, i)
    return int(result)
        
def lcm(a, b):
    return a*b / gcd(a, b)

def gcd(a, b):
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    return gcd(b, a % b)


if __name__ == "__main__":
    main()
