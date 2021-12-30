from collections import defaultdict, deque, Counter
from itertools import combinations, combinations_with_replacement, permutations
from functools import reduce
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


REAL = [10, 7]

SAMPLE_EXPECTED = 444356092776315
if SAMPLE_EXPECTED:
    SAMPLE = [4, 8]

def solve(start_spots, target=21):
    cache = {}
    def simulate(player, spots, scores, target):
        if scores[0] >= target:
            return (1, 0)
        elif scores[1] >= target:
            return (0, 1)

        if (player, spots, scores) in cache:
            return cache[(player, spots, scores)]
        snew = [0, 0]
        for d, times in combos().items():
            newspot = (spots[player] + d - 1) % 10 + 1
            newscores = list(scores)
            newscores[player] += newspot
            newspots = list(spots)
            newspots[player] = newspot
            p1, p2 = simulate((player + 1) % 2, tuple(newspots), tuple(newscores), target)
            snew[0] += times * p1
            snew[1] += times * p2
        newscores = tuple(snew)
        cache[(player, spots, scores)] = newscores
    
        return newscores
    
    scores = simulate(0, tuple(start_spots), (0, 0), target)
    print(scores)            
    return max(scores)

def combos():
    ret = DefaultDict(lambda: 0)
    for d1 in [1, 2, 3]:
        for d2 in [1, 2, 3]:
            for d3 in [1, 2, 3]:
                ret[d1+d2+d3] += 1
    return ret
print(combos())

print(solve((1, 2), 1))

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
