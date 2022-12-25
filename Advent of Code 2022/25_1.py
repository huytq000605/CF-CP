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


def main():
    lines = sys.stdin.read().splitlines()
    values = {"1": 1, "2": 2, "0": 0, "-": -1, "=": -2}
    dec = 0
    for line in lines:
        n = len(line)
        line = line[::-1]
        num = 0
        for i, v in enumerate(line):
            num += values[v] * (5 ** i)
        dec += num

    s = ""
    while dec:
        dec, mod = divmod(dec, 5)
        if mod < 3:
            s += str(mod)
        elif mod == 3:
            dec += 1
            s += "="
        elif mod == 4:
            dec += 1
            s += "-"
    s = s[::-1]
    print(s)



# Converting from SNAFU to base-10 is easy: 
# a number is a string of "digits" (v[n], ..., v[2], v[1], v[0]), the value of it is v[n] * 5n + ... + v[2] * 52 + v[1] * 5 + v[0], so calculate that while iterating over the string from the end.
# Converting from base-10 to SNAFU is a little bit trickier. 
# Start by converting from base-10 to base-5: the number is n = a[n] * 5n + ... + a[2] * 52 + a[1] * 5 + a[0], so a[0] = n mod 5, and floor(n / 5) = a[n] * 5n-1 + ... + a[2] * 5 + a[1], that is n shifted to the right in base-5. So at each iteration add a[0] to an array, shift n to the right, and repeat until n is 0, the result is reversed array.
# Now modify the algorithm to handle the case when a[0] = 3 or 4 mod 5. 
# The SNAFU digit value is v[0] = -(5 - a[0]) = -5 + a[0], hence a[0] = v[0] + 5. So n = a[n] * 5n + ... + a[2] * 52 + a[1] * 5 + (v[0] + 5) = a[n] * 5n + ... + a[2] * 52 + (a[1] + 1) * 5 + v[0]. So in case of v[0] < 0 we just have to add 5 to n before shifting, or 1 to n after shifting.


    




if __name__ == "__main__":
    main()

