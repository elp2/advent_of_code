from collections import defaultdict, deque, Counter
from itertools import combinations, combinations_with_replacement, permutations
from functools import reduce
import math
# import numpy as np
from operator import add, mul, itemgetter, attrgetter
import re

DS = [[-1, 0], [1, 0], [0, 1], [0, -1]]
DS8 = DS + [[-1, -1], [1, -1], [-1, 1], [1, 1]]
def arounds_inside(x, y, diagonals, w, h):
    ret = []
    for dx, dy in DS8 if diagonals else DS:
        ret.append((x + dx, y + dy))


CHALLENGE_DAY = "18"
REAL = open(CHALLENGE_DAY + ".txt").read()

SAMPLE_EXPECTED = 58
if SAMPLE_EXPECTED:
    SAMPLE = open(CHALLENGE_DAY + ".s.txt").read()


def parse_lines(raw):
    # Groups.
    # groups = raw.split("\n\n")
    # return list(map(lambda group: group.split("\n"), groups))
    lines = raw.split("\n")
    # return lines # raw
    return list(map(lambda l: l.split(","), lines))
    # return list(map(int, lines))
    # return list(map(lambda l: l.strip(), lines)) # beware leading / trailing WS

def solve(raw):
    cubes = parse_lines(raw)

    threed = set()
    outsides = set()
    for c in cubes:
        threed.add(tuple(map(lambda i: int(i), c)))
    seen = set()
    q = deque()
    q.append((0, 0, 0))

    outsides = 0

    maxx = maxy = maxz = 0
    for x, y, z in threed:
        maxx = max(x + 2, maxx)
        maxy = max(y + 2, maxy)
        maxz = max(z + 2, maxz)
    while len(q):
        x, y, z = q.popleft()
        ds = [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0,0,1), (0,0,-1)]
        
        for dx, dy, dz in ds:
            other = (x + dx, y + dy, z + dz)
            if other in threed:
                outsides += 1
            elif other not in seen and -2 <= other[0] < maxx and -2 <= other[1] < maxy and -2 <= other[2] < maxz:
                q.append(other)
                seen.add(other)

    return outsides

if SAMPLE_EXPECTED != None:
    sample = solve(SAMPLE)
    if sample != SAMPLE_EXPECTED:
        print("SAMPLE FAILED: ", sample, " != ", SAMPLE_EXPECTED)
    assert sample == SAMPLE_EXPECTED
    print("\n*** SAMPLE PASSED ***\n")
else:
    print("Skipping sample")

solved = solve(REAL) # 2567 wrong
print("SOLUTION: ", solved)
