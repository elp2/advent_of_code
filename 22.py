from collections import defaultdict, deque, Counter, namedtuple
from itertools import combinations, combinations_with_replacement, permutations
import math
import numpy as np
from operator import add, mul, itemgetter, attrgetter
import re

def flatten(t):
    return [item for sublist in t for item in sublist]

ON_TEXT = '\u2588'
OFF_TEXT = '\u2592'

DAY = "22"
REAL = open(DAY + ".in").read().strip().split("\n")

SAMPLE_EXPECTED = None

Disk = namedtuple("Disk", ["x", "y", "size",  "used",  "avail"])

def get_nodes(lines):
    nodes = []
    useds = Counter()
    avails = Counter()
    for line in lines:
        # Filesystem              Size  Used  Avail  Use%
        # /dev/grid/node-x0-y0     93T   71T    22T   76%
        x, y, size, used, avail, _ = map(int, re.findall(r'\d+', line))
        useds[used] += 1
        avails[avail] += 1
        disk = Disk(x, y, size, used, avail)
        assert disk.size - disk.used == disk.avail
        nodes.append(disk)

    print(useds, "\n", avails)

    return nodes

def viable(a, b):
    if a.used == 0:
        return False
    if a.x == b.x and a.y == b.y:
        print(a)
        return False
    return a.used <= b.avail

def solve(raw):
    nodes = get_nodes(raw)
    viables = []
    dupes = 0
    for (a, b) in combinations(nodes, 2):
        if viable(a, b):
            viables.append((a, b))
        if viable(b, a):
            viables.append((b, a))

    print("part 1:", len(viables),   dupes)
    return ret

if SAMPLE_EXPECTED != None:
    SAMPLE = open(DAY + ".sample").read()
    sample = solve(SAMPLE)
    if sample != SAMPLE_EXPECTED:
        print("SAMPLE FAILED: ", sample, " != ", SAMPLE_EXPECTED)
    assert sample == SAMPLE_EXPECTED
    print("\n*** SAMPLE PASSED ***\n")
else:
    print("Skipping sample")

part1 = solve(REAL)
print("Part 1: ", part1)

part2 = solve(REAL)
print("Part 2: ", part2)

try:
    import pandas as pd
    df=pd.DataFrame([str(solved)])
    df.to_clipboard(index=False,header=False)
    print("COPIED TO CLIPBOARD")
except ModuleNotFoundError:
    print("Pandas not installed.")