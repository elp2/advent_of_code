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


CHALLENGE_DAY = "14"
REAL = open(CHALLENGE_DAY + ".txt").read()

SAMPLE_EXPECTED = 2188189693529
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
    nmol = DefaultDict(lambda: 0)

    for k, v in mol.items():
        r = rules[k.upper()]
        a = k[0] + r
        b = r.lower() + k[1]
        nmol[a] += v
        nmol[b] += v
        print(k, v, "->", a, b)

    return nmol



def solve(raw):
    mol, rules = parse_lines(raw)
    # Debug here to make sure parsing is good.
    ret = 0

    mdict = DefaultDict(lambda: 0)
    mdict[mol[:2]] = 1
    for i in range(1, len(mol) - 1):
        pair = list(mol[i:i+2])
        pair[0] = pair[0].lower()
        mdict["".join(pair)] += 1
    


    for r in range(40):
        mdict = round(mdict, rules)
    
    maps = Counter()
    for k, v in mdict.items():
        if k[0] == k[0].upper():
            maps[k[0]] += v
        if k[1] == k[1].upper():
            maps[k[1]] += v
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
