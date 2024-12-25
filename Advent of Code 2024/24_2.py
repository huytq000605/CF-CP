# copied from Alternative_Chain293
import sys

XOR = 'XOR'
AND = 'AND'
OR = 'OR'

g = {}
rg = {}
minmax = lambda _a, _b: (_a, _b) if _a <= _b else (_b, _a)

for line in sys.stdin.read().split('\n\n')[1].splitlines():
    a, op, b, _, c = line.split()
    a, b = minmax(a, b)
    g[a, b, op] = c
    rg[c] = a, b, op


def swap(_a, _b):
    rg[_a], rg[_b] = rg[_b], rg[_a]
    g[rg[_a]], g[rg[_b]] = g[rg[_b]], g[rg[_a]]


output = set()
c = ''
for i in range(int(max(rg)[1:])):
    x = f'x{i:02}'
    y = f'y{i:02}'
    z = f'z{i:02}'
    zn = f'z{i + 1:02}'
    xxy = g[x, y, XOR]
    xay = g[x, y, AND]
    if not c:
        c = xay
    else:
      	# if there is carryover, the next val will be xxy ^ c
        a, b = minmax(c, xxy)
        k = a, b, XOR
        # there is no k in g, meaning this is wrong
        # we know to reach z, we have to a xor b
        # but reaching z currently is b xor c
        # so we swap a and c
        if k not in g:
            print(rg[z][:2], k[:2])
            a, b = list(set(rg[z][:2]) ^ set(k[:2]))
            output.add(a)
            output.add(b)
            swap(a, b)
        # we know to reach z, we have to a xor b
        # but reaching z currently is c xor d != a xor b
        # so we swap output (a xor b) with z
        elif g[k] != z:
            output.add(g[k])
            output.add(z)
            swap(z, g[k])
        k = rg[z]
        xxy = g[x, y, XOR]
        xay = g[x, y, AND]
        w1, w2 = minmax(c, xxy)
        c = g[w1, w2, AND]
        w1, w2 = minmax(c, xay)
        c = g[w1, w2, OR]

print(','.join(sorted(output)))