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
        n, m, k = get_ints()
        a = get_string()
        b = get_string()
        print(solve(a, b, k))


def solve(a, b, k):
    ac = [0 for i in range(26)]
    for l in a:
        ac[ord(l) - ord('a')] += 1
    bc = [0 for i in range(26)]
    for l in b:
        bc[ord(l) - ord('a')] += 1
    c = ""
    i, j = 0, 0
    while ac[i] == 0:
        i += 1
    while bc[j] == 0:
        j += 1
    take_from_a = i < j
    cur = 0
    def increase_idx(arr, i):
        nonlocal take_from_a, cur
        if take_from_a:
            if arr != ac:
                cur = 0
                take_from_a = False
        else:
            if arr != bc:
                cur = 0
                take_from_a = True
        while i < 26 and arr[i] == 0:
            i += 1
        return i

    while i < 26 and j < 26:
        if cur >= k:
            if take_from_a:
                c += chr(j + ord('a'))
                bc[j] -= 1
                j = increase_idx(bc, j)
            else:
                c += chr(i + ord('a'))
                ac[i] -= 1
                i = increase_idx(ac, i)
        else:
            if i < j:
                c += chr(i + ord('a'))
                ac[i] -= 1
                i = increase_idx(ac, i)
            else:
                c += chr(j + ord('a'))
                bc[j] -= 1
                j = increase_idx(bc, j)
        cur += 1
    return c


if __name__ == "__main__":
    main()
