from collections import defaultdict, deque, Counter
from itertools import combinations, combinations_with_replacement, permutations
import math
# import numpy as np
from operator import add, mul, itemgetter, attrgetter
import re
from typing import DefaultDict

DS = [[-1, 0], [1, 0], [0, 1], [0, -1]]
DS8 = DS + [[-1, -1], [1, -1], [-1, 1], [1, 1]]
def arounds_inside(x, y, diagonals, w, h):
    ret = []
    for dx, dy in DS8 if diagonals else DS:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < w and 0 <= ny < h:
            ret.append((nx, ny))
    return ret


CHALLENGE_DAY = "15"
REAL = open(CHALLENGE_DAY + ".txt").read()

SAMPLE_EXPECTED = 315
if SAMPLE_EXPECTED:
    SAMPLE = open(CHALLENGE_DAY + ".s.txt").read()


def parse_lines(raw):
    # Groups.
    # groups = raw.split("\n\n")
    # return list(map(lambda group: group.split("\n"), groups))
    return [[int(x) for x in line] for line in raw.split("\n")]

def solve(raw):
    parsed = parse_lines(raw)
    # parsed = [[8]]
    w = len(parsed[0])
    h = len(parsed)

    def risk_at(x, y):
        assert x <= 5 * w
        assert y <= 5 * h
        bx = x % w
        by = y % h
        base = parsed[by][bx]
        adj = base + (x - bx) // w + (y - by) // h
        if adj <= 9:
            return adj
        else:
            while adj > 9:
                adj -= 9
            return adj
    # Debug here to make sure parsing is good.
    ret = 0

    bests = DefaultDict(lambda: 1000000000)

    q = {(0, 0): -parsed[0][0]}
    while len(q) != 0:
        print(len(q))
        nq = DefaultDict(lambda: 10000000)
        for (x, y), cost in q.items():
            cost += risk_at(x, y)
            if bests[(x, y)] <= cost:
                continue
            bests[(x, y)] = cost
            for ax, ay in arounds_inside(x, y, False, 5 * w, 5 * h):
                nq[(ax, ay)] = min(cost, nq[(ax, ay)])
        q = nq
    ret = bests[(5 * w - 1, 5 * h - 1)]

    return ret

if SAMPLE_EXPECTED != None:
    sample = solve(SAMPLE)
    if sample != SAMPLE_EXPECTED:
        print("SAMPLE FAILED: ", sample, " != ", SAMPLE_EXPECTED)
    assert sample == SAMPLE_EXPECTED
    print("\n*** SAMPLE PASSED ***\n")
else:
    print("Skipping sample")

solved = solve(REAL) # 488 too high
print("SOLUTION: ", solved)
import pandas as pd
df=pd.DataFrame([str(solved)])
df.to_clipboard(index=False,header=False)
print("COPIED TO CLIPBOARD")
