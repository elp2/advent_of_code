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


CHALLENGE_DAY = "25"
REAL = open(CHALLENGE_DAY + ".txt").read()

SAMPLE_EXPECTED = 58
if SAMPLE_EXPECTED:
    SAMPLE = open(CHALLENGE_DAY + ".s.txt").read()


def parse_lines(raw):
    # Groups.
    # groups = raw.split("\n\n")
    # return list(map(lambda group: group.split("\n"), groups))
    lines = raw.split("\n")

    rights = set()
    downs = set()
    h = len(lines)
    w = len(lines[0])
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == ">":
                rights.add((x, y))
            elif c == "v":
                downs.add((x, y))
    
    return rights, downs, w, h


def solve(raw):
    rights, downs, w, h = parse_lines(raw)

    total = len(rights) + len(downs)

    round = 0
    while True:
        print(round)
        moved = 0

        nrights = set()
        ndowns = set()
        for (x, y) in rights:
            nx = (x + 1) % w
            ny = y
            if (nx, ny) in rights or (nx, ny) in downs:
                nrights.add((x, y))
            else:
                nrights.add((nx, ny))
                moved += 1

        for (x, y) in downs:
            nx = x
            ny = (y + 1) % h
            if (nx, ny) in nrights or (nx, ny) in downs:
                ndowns.add((x, y))
            else:
                ndowns.add((nx, ny))
                moved += 1

        if moved == 0:
            return round + 1

        print(round, moved)
        downs = ndowns
        rights = nrights
        round += 1
        assert len(downs) + len(rights) == total


if SAMPLE_EXPECTED != None:
    sample = solve(SAMPLE)
    if sample != SAMPLE_EXPECTED:
        print("SAMPLE FAILED: ", sample, " != ", SAMPLE_EXPECTED)
    assert sample == SAMPLE_EXPECTED
    print("\n*** SAMPLE PASSED ***\n")
else:
    print("Skipping sample")

solved = solve(REAL)
print("SOLUTION: ", solved)
import pandas as pd
df=pd.DataFrame([str(solved)])
df.to_clipboard(index=False,header=False)
print("COPIED TO CLIPBOARD")
