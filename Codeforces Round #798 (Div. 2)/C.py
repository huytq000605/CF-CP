from functools import lru_cache
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
        tree = [[] for j in range(n)]
        for j in range(n-1):
            u, v = get_ints()
            tree[u-1].append(v-1)
            tree[v-1].append(u-1)
        print(solve(tree, n))


def solve(tree, n):
    count_child_node = [0 for i in range(n)]
    def count(node, parent):
        result = 0
        tree[node] = list(filter(lambda ele: ele != parent, tree[node]))
        for child in tree[node]:
            if child == parent:
                continue
            result += 1
            result += count(child, node)
        count_child_node[node] = result
        return result
    count(0, -1)

    @lru_cache(None)
    def dfs(node):
        children = tree[node]
        if len(children) == 0:
            return 0
        elif len(children) == 1:
            return count_child_node[children[0]]
        elif len(children) == 2:
            return max(count_child_node[children[0]] + dfs(children[1]),
                    count_child_node[children[1]] + dfs(children[0]))
        else:
            return 0

    return dfs(0)

if __name__ == "__main__":
    main()
