from functools import lru_cache
from collections import Counter, defaultdict
import math
from heapq import *

import sys
def get_int(): return int(sys.stdin.readline().strip())
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_list(): return list(map(int, sys.stdin.readline().strip().split()))
def get_string(): return sys.stdin.readline().strip()

def main():
    testcases = get_int()
    for i in range(testcases):
        n, m = get_ints()
        a = get_list()
        freq = Counter()
        pairs = []
        for j in range(m):
            u, v = get_ints()
            u, v = u-1, v-1
            freq[u] += 1
            freq[v] += 1
            pairs.append((u, v))
        if m % 2 != 0:
            print(solve(pairs, freq, a))
        else:
            print(0)



def solve(pairs, freq, a):
    result = math.inf
    for i in range(len(a)):
        if freq[i] % 2 == 1:
            result = min(result, a[i])

    for u, v in pairs:
        if freq[u] % 2 == 0 and freq[v] % 2 == 0:
            result = min(result, a[u] + a[v])
    return result


if __name__ == "__main__":
    try:
        main()
    except BaseException as e:
        print(e)
