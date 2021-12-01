from collections import defaultdict, deque, Counter
from itertools import combinations, combinations_with_replacement, permutations
import math
import numpy as np
from operator import add, mul, itemgetter, attrgetter
import re

def flatten(t):
    return [item for sublist in t for item in sublist]

ON_TEXT = '\u2588'
OFF_TEXT = '\u2592'

DAY = "13"

SAMPLE_EXPECTED = None # 11

OPEN = "."
WALL = "#"

def solve(tx, ty, number):
    building = {}

    queue = deque()
    queue.append((1, 1, 0))

    part1 = None
    while queue:
        pl = queue.popleft()
        x, y, depth = pl

        if depth == 51:
            part2 = 0
            for space, _ in building.values():
                if space == OPEN:
                    part2 += 1
                print(space)
            return part1, part2

        if x < 0 or y < 0:
            continue
        if (x, y) in building:
            continue
        if x == tx and y == ty:
            part1 = depth
        val = x*x + 3*x + 2*x*y + y + y*y + number
        ones = bin(val).count("1")
        if ones % 2 == 0:
            here = OPEN
        else:
            here = WALL
        building[(x, y)] = (here, depth)
        if here == WALL:
            continue

        nd = depth + 1
        queue.append((x + 1, y, nd))
        queue.append((x-1, y, nd))
        queue.append((x, y+1, nd))
        queue.append((x, y-1, nd))

    return ret

if SAMPLE_EXPECTED != None:
    sample = solve(7,4, 10)
    if sample != SAMPLE_EXPECTED:
        print("SAMPLE FAILED: ", sample, " != ", SAMPLE_EXPECTED)
    assert sample == SAMPLE_EXPECTED
    print("\n*** SAMPLE PASSED ***\n")
else:
    print("Skipping sample")

part1 = solve(31,39, 1362)
print("Part 1, 2: ", part1)

try:
    import pandas as pd
    df=pd.DataFrame([str(solved)])
    df.to_clipboard(index=False,header=False)
    print("COPIED TO CLIPBOARD")
except ModuleNotFoundError:
    print("Pandas not installed.")
