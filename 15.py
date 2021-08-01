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

DAY = "15"
REAL = """Disc #1 has 17 positions; at time=0, it is at position 5.
Disc #2 has 19 positions; at time=0, it is at position 8.
Disc #3 has 7 positions; at time=0, it is at position 1.
Disc #4 has 13 positions; at time=0, it is at position 7.
Disc #5 has 5 positions; at time=0, it is at position 1.
Disc #6 has 3 positions; at time=0, it is at position 0."""
EXTRA = """Disc #7 has 11 positions; at time=0, it is at position 0."""

SAMPLE_EXPECTED = 5

def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)

def solve(raw):
    lines = raw.split("\n")
    discs = []
    for li in range(len(lines)):
        l = lines[li].strip().split(" ")
        numpos = int(l[3])
        pos = int(l[11].replace(".", ""))
        pos += li + 1
        pos %= numpos
        discs.append((pos, numpos))

    print(discs)

    a = 0
    while True:
        poses = set({(a + p) % np for p, np in discs})
        if len(poses) == 1 and poses == set([0]):
            return a
        if a % 100000 == 0:
            print(a)
        a += 1
    return None

if SAMPLE_EXPECTED != None:
    SAMPLE = """Disc #1 has 5 positions; at time=0, it is at position 4.
Disc #2 has 2 positions; at time=0, it is at position 1."""
    sample = solve(SAMPLE)
    if sample != SAMPLE_EXPECTED:
        print("SAMPLE FAILED: ", sample, " != ", SAMPLE_EXPECTED)
    assert sample == SAMPLE_EXPECTED
    print("\n*** SAMPLE PASSED ***\n")
else:
    print("Skipping sample")

part1 = solve(REAL)
print("Part 1: ", part1) # 114110 high

part2 = solve(REAL + "\n" + EXTRA) # 555005 low
print("Part 2: ", part2)

try:
    import pandas as pd
    df=pd.DataFrame([str(solved)])
    df.to_clipboard(index=False,header=False)
    print("COPIED TO CLIPBOARD")
except ModuleNotFoundError:
    print("Pandas not installed.")