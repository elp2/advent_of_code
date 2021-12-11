from collections import defaultdict, deque, Counter
from itertools import combinations, combinations_with_replacement, permutations
import math
# import numpy as np
from operator import add, mul, itemgetter, attrgetter
import re
from typing import DefaultDict

CHALLENGE_DAY = "11"
REAL = open(CHALLENGE_DAY + ".txt").read()

SAMPLE_EXPECTED = 195
if SAMPLE_EXPECTED:
    SAMPLE = open(CHALLENGE_DAY + ".s.txt").read()


def parse_lines(raw):
    # Groups.
    # groups = raw.split("\n\n")
    # return list(map(lambda group: group.split("\n"), groups))
    lines = raw.split("\n")
    ret = []
    for line in lines:
        ret.append([int(l) for l in line])
    return ret
    # return lines # raw
    # return list(map(lambda l: l.split(" "), lines)) # words.
    # return list(map(int, lines))
    # return list(map(lambda l: l.strip(), lines)) # beware leading / trailing WS

def step(octs):
    flashed = set()
    def flash(x, y, around):
        if (x, y) in flashed:
            return
        # assert (x, y) not in flashed
        flashed.add((x, y))
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == dy and dx == 0:
                    continue
                nx = dx + x
                ny = dy + y
                if 0 <= nx < len(octs[0]) and 0 <= ny < len(octs):
                    if (nx, ny) in flashed:
                        continue
                    around[(nx, ny)] += 1
    

    arounds = DefaultDict(lambda: 0)
    for y in range(len(octs)):
        line = octs[y]
        for x in range(len(line)):
            line[x] += 1
            if line[x] >= 10:
                flash(x, y, arounds)
    
    while len(arounds):
        next = DefaultDict(lambda: 0)
        for (x, y), v in arounds.items():
            octs[y][x] += v
            if octs[y][x] >= 10:
                flash(x, y, next)

        arounds = next

    for (x, y) in flashed:
        octs[y][x] = 0

    a = octs[y][x]
    for line in octs:
        for o in line:
            if a != o:
                return False

    return True

def solve(raw):
    parsed = parse_lines(raw)
    # Debug here to make sure parsing is good.
    ret = 0
    # for line in parsed:
    #     print("".join([str(o) for o in line]))
    while True:
        ret += 1
        if step(parsed):
            return ret

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
