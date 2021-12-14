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


CHALLENGE_DAY = "14"
REAL = open(CHALLENGE_DAY + ".txt").read()

SAMPLE_EXPECTED = 1588
if SAMPLE_EXPECTED:
    SAMPLE = open(CHALLENGE_DAY + ".s.txt").read()


def parse_lines(raw):    
    # Groups.
    mol, rules = raw.split("\n\n")
    rmap = {}
    for rule in rules.split("\n"):
        f, to = rule.split(" -> ")
        rmap[f] = to
    return mol, rmap


    # return list(map(lambda group: group.split("\n"), groups))
    # lines = raw.split("\n")
    # return lines # raw
    # return list(map(lambda l: l.split(" "), lines)) # words.
    # return list(map(int, lines))
    # return list(map(lambda l: l.strip(), lines)) # beware leading / trailing WS


def round(mol, rules):
    nmol = []

    for i in range(len(mol) - 1):
        pair = "".join(mol[i:i+2])
        print(pair)
        assert pair in rules
        nmol.append(pair[0])
        nmol.append(rules[pair])
    nmol.append(pair[1])

    print("".join(nmol))
    return nmol

def solve(raw):
    mol, rules = parse_lines(raw)
    # Debug here to make sure parsing is good.
    ret = 0

    for r in range(10):
        mol = round(mol, rules)

    
    maps = Counter()
    for c in mol:
        maps[c] += 1
    coms = maps.most_common()
    mck, mcnum = coms[0]
    lck, lcnum = coms[-1]

    return mcnum - lcnum

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
