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
def get_int(): return int(input())
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_list(): return list(map(int, sys.stdin.readline().strip().split()))
def get_string(): return sys.stdin.readline().strip()


class BreakOutException(Exception):
    pass


def main():
    lines = sys.stdin.read().splitlines()
    values = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]
    ranks = {
        "high": [1],
        "one": [2],
        "two": [3],
        "three": [4],
        "full": [5],
        "four": [6],
        "five": [7]
    }
    for line in lines:
        cards, bet = line.split(" ")

        counter = Counter()
        count_j = 0
        for card in cards:
            if card == "J":
                count_j += 1
                continue
            counter[card] += 1

        
        mx = 0
        if counter:
            mx = max(counter.values())
        keys = [cards[i] for i in range(5)]
        keys = [-values.index(e) for e in keys]
        keys.append(bet)
        keys = tuple(keys)
        mx = min(5, mx + count_j)
        if mx == 5:
            ranks["five"].append((keys, bet))
        elif mx == 4:
            ranks["four"].append(keys)
        elif mx == 3 and len(counter) == 2:
            ranks["full"].append(keys)
        elif mx == 3 and len(counter) == 3:
            ranks["three"].append(keys)
        elif mx == 2 and len(counter) == 3:
            ranks["two"].append(keys)
        elif mx == 2 and len(counter) == 4:
            ranks["one"].append(keys)
        elif mx == 1:
            ranks["high"].append(keys)

    jth = 1
    result = 0
    for key in ranks.keys():
        ranks[key] = sorted(ranks[key][1:])

    for key in reversed(["five", "four", "full", "three", "two", "one", "high"]):
        for (*_, bet) in ranks[key]:
            result += jth * int(bet)
            jth += 1

    print(result)
    return result
       
        

if __name__ == "__main__":
    main()

