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
        ret.append((x + dx, y + dy))


CHALLENGE_DAY = "12"
REAL = open(CHALLENGE_DAY + ".txt").read()

SAMPLE_EXPECTED = 3509
if SAMPLE_EXPECTED:
    SAMPLE = open(CHALLENGE_DAY + ".s.txt").read()


def parse_lines(raw):
    lines = raw.split("\n")
    ret = DefaultDict(lambda: [])
    for l in lines:
        f, to = l.split("-")
        if to != "start":
            ret[f].append(to)
        if f != "start":
            ret[to].append(f)
    return ret

def solve(raw):
    parsed = parse_lines(raw)
    ret = 0

    visit = deque()
    visit.append((["start"], set(), None))

    paths = []
    while len(visit):
        p, seens, extra = visit.popleft()
        here = p[-1]
        if here == "end":
            paths.append(p)
            continue
        if here.lower() == here and here not in ["start", "end"]:
            if here not in seens:
                seens.add(here)
            elif extra == None:
                extra = here
            else:
                assert False
        
        for adj in parsed[here]:
            if adj in seens and extra != None:
                continue
            else:
                pnew = p.copy()
                pnew.append(adj)
                snew = seens.copy()
                visit.append((pnew, snew, extra))

    print(paths[:100])
    return len(paths)

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
