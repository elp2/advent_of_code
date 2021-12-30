from collections import defaultdict, deque, Counter
from itertools import combinations, combinations_with_replacement, permutations
from functools import reduce
import math
# import numpy as np
from operator import add, delitem, mul, itemgetter, attrgetter
import re

DS = [[-1, 0], [1, 0], [0, 1], [0, -1]]
DS8 = DS + [[-1, -1], [1, -1], [-1, 1], [1, 1]]
def arounds_inside(x, y, diagonals, w, h):
    ret = []
    for dx, dy in DS8 if diagonals else DS:
        ret.append((x + dx, y + dy))


CHALLENGE_DAY = "12"
REAL = [10, 7]

SAMPLE_EXPECTED = 739785
if SAMPLE_EXPECTED:
    SAMPLE = [4, 8]


die = 1
rolls = 0

def solve(raw):
    spots = raw
    # Debug here to make sure parsing is good.
    scores = [0, 0]

    global die
    global rolls
    die = 1
    rolls = 0


    def roll():
        global die
        global rolls
        ret = die
        die += 1
        rolls += 1

        if die > 100:
            die = 1
        return ret

    def play(pi, scores):
        move = roll() + roll() + roll()
        next = ((spots[pi] - 1) + move) % 10 + 1
        spots[pi] = next
        scores[pi] += next

    while True:
        for pi in [0, 1]:
            play(pi, scores)
            # print(pi, scores)
            if scores[pi] >= 1000:
                return rolls * scores[(pi + 1) % 2]

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
assert 874698 < solved
print(solved)