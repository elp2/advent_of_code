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

DAY = "20"
REAL = open(DAY + ".in").read()

SAMPLE_EXPECTED = None

def parse(raw):
    ranges = [list(map(int, line.split("-"))) for line in raw.split("\n") if line]
    return sorted(ranges, key=itemgetter(0))    

def solve(raw):
    sr = parse(raw)
    ranges = []
    h = None
    for r in sr:
        if not ranges:
            ranges.append(r)
            continue

        last = ranges[-1]
        if last[1] + 1 >= r[0]:
            last = [min(last[0], r[0]), max(last[1], r[1])]
            ranges[-1] = last
        else:
            ranges.append(r)
        

    part1 = ranges[0][1] + 1
    part2 = 0
    for i in range(len(ranges) - 1):
        part2 += ranges[i + 1][0] - ranges[i][1] - 1
    part2 += 2**32 - ranges[-1][1] - 1

    return part1, part2


if SAMPLE_EXPECTED != None:

    SAMPLE = open(DAY + ".sample").read()
    sample = solve(SAMPLE)
    if sample != SAMPLE_EXPECTED:
        print("SAMPLE FAILED: ", sample, " != ", SAMPLE_EXPECTED)
    assert sample == SAMPLE_EXPECTED
    print("\n*** SAMPLE PASSED ***\n")
else:
    print("Skipping sample")

parts = solve(REAL)
print("Parts: ", parts)

try:
    import pandas as pd
    df=pd.DataFrame([str(solved)])
    df.to_clipboard(index=False,header=False)
    print("COPIED TO CLIPBOARD")
except ModuleNotFoundError:
    print("Pandas not installed.")