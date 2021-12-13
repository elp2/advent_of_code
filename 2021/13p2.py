from collections import defaultdict, deque, Counter
from itertools import combinations, combinations_with_replacement, permutations
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


CHALLENGE_DAY = "13"
REAL = open(CHALLENGE_DAY + ".txt").read()

SAMPLE_EXPECTED = 16
if SAMPLE_EXPECTED:
    SAMPLE = open(CHALLENGE_DAY + ".s.txt").read()


def parse_lines(raw):

    # Groups.
    dots, folds = raw.split("\n\n")
    dr = set()
    for d in dots.split("\n"):
        x, y = [int(x) for x in d.split(",")]
        dr.add((x, y))
    
    fr = []
    for f in folds.split("\n"):
        l = f.split(" ")
        a = l[2]
        dim, num = [z for z in a.split("=")]
        num = int(num)
        fr.append((dim, num))
    
    return dr, fr
    # return list(map(lambda group: group.split("\n"), groups))
    # lines = raw.split("\n")
    # return lines # raw
    # return list(map(lambda l: l.split(" "), lines)) # words.
    # return list(map(int, lines))
    # return list(map(lambda l: l.strip(), lines)) # beware leading / trailing WS

def solve(raw):
    dots, folds = parse_lines(raw)
    # Debug here to make sure parsing is good.
    ret = 0

    for fdim, fnum in folds:
        print(fdim, fnum)
        dnew = set()
        for dx, dy in dots:
            if fdim == "x":
                assert dx != fnum
                diff = dx - fnum
                if dx >= fnum:
                    after = (fnum - diff, dy)
                else:
                    after = (dx, dy)
            elif fdim == "y":
                assert dy != fnum
                diff = dy - fnum
                if dy >= fnum:
                    after = (dx, fnum - diff)
                else:
                    after = (dx, dy)
            print((dx, dy), "->", after)
            dnew.add(after)

        dots = dnew

    mx, my = 0, 0
    for d in dots:
        dx, dy = d
        mx = max(mx, dx)
        my = max(my, dy)

    for y in range(my+ 1):
        line = []
        for x in range(mx + 1):
            line.append("*" if (x, y) in dots else " ")
        print("".join(line))
    
    return len(dots)

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
