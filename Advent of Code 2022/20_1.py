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

class LL:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None



def main():
    lines = sys.stdin.read().splitlines()
    head = LL(0)
    prev = head
    n = 0
    order = []
    zero = None
    for line in lines:
        val = int(line)
        node = LL(val)
        if val == 0:
            zero = node
        node.prev = prev
        prev.next = node
        prev = node
        n += 1
        order.append(node)
    head = head.next
    prev.next = head
    head.prev = prev

    for node in order:
        val = node.val
        if val == 0:
            continue
        nxt = node.next
        prev = node.prev
        prev.next = nxt
        nxt.prev = prev
        if val < 0:
            while val < 0:
                prev = prev.prev
                val += 1
            nxt = prev.next
            node.prev = prev
            node.next = nxt
            nxt.prev = node
            prev.next = node
        
        if val > 0:
            while val > 0:
                nxt = nxt.next
                val -= 1
            prev = nxt.prev
            node.prev = prev
            node.next = nxt
            prev.next = node
            nxt.prev = node

    result = 0
    cur = zero
    for i in range(3001):
        if i > 0 and i % 1000 == 0:
            result += cur.val
        cur = cur.next
    print(result)









if __name__ == "__main__":
    main()

