from collections import defaultdict, deque, Counter
from itertools import combinations, combinations_with_replacement, permutations
from functools import reduce, cmp_to_key
import math
# import numpy as np
from operator import add, mul, itemgetter, attrgetter
import os
import re
from sys import argv

def flatten(t):
    return [item for sublist in t for item in sublist]

# Sorts with cmp. cmp < 0 for a < b, == 0 for a==b, > 0 for a > b.
def elpsort(array, cmp):
    return sorted(array, key=cmp_to_key(cmp))

ON_TEXT = '\u2588'
OFF_TEXT = '\u2592'

LEFT = 0
UP = 1
RIGHT = 2
DOWN = 3
CHAR_TO_DS = {"^": UP, ">": RIGHT, "<": LEFT, "v": DOWN}
DS = [(-1, 0), (0, -1), (1, 0), (0, 1)]
DS8 = DS + [(-1, -1), (1, -1), (-1, 1), (1, 1)]
def arounds(x, y, diagonals):
    ret = []
    for dx, dy in DS8 if diagonals else DS:
        ret.append((x + dx, y + dy))
    return ret

CHALLENGE_DAY = "17"
AOC_DIR = os.path.dirname(argv[0])

print("Day: ", CHALLENGE_DAY)

######################
SAMPLE_EXPECTED = 94
######################
assert SAMPLE_EXPECTED != None

try:
    SAMPLE = open(os.path.join(AOC_DIR, CHALLENGE_DAY + ".s.txt")).read()
except:
    print("Did you create the sample file?")

try:
    REAL = open(os.path.join(AOC_DIR, CHALLENGE_DAY + ".txt")).read()
except:
    print("Did you create the solutions file?")


def parse_lines(raw):
    lines = raw.split("\n")
    return list(map(lambda r: list(map(lambda c: int(c), r)), lines))

MIN_MOVE=4
MUST_TURN=10

def solve(raw):
    losses = parse_lines(raw)

    ret = 0
    best = None

    ending = (len(losses[0]) - 1, len(losses) - 1)

    bests = {}
    def ret1k():
        return 1000000
    enqbest = defaultdict(ret1k)


    def seen_better(x, y, dir, runlen, lost, update=False):
        return False        
        for rl in range(runlen):
            key = (x, y, dir, rl)
            if key in bests:
                other = bests[key]
                if other <= lost:
                    return True
        
        key = (x, y, dir, runlen)
        if key not in bests or bests[key] > lost:
            if update:
                bests[key] = lost
            return False
        return True

    i = 0
    print("TODO DOWN")
    q = deque([
                 (0, 0, DOWN, 0, 0),
                 (0, 0, RIGHT, 0, 0)
            ])
    while len(q):
        i += 1
        if i == 1000000:
            print(x, y, len(q))
            i = 0
        x, y, dir, runlen, lost = q.popleft()
        if (x, y) == (11,4):
            print(x, y, dir, runlen, lost)

        if lost > enqbest[(x, y, dir, runlen)]:
            continue

        if seen_better(x, y, dir, runlen, lost, True):
            continue

        if (x, y) == ending and runlen >= MIN_MOVE:
            if best == None:
                best = lost
            else:
                best = min(lost, best)
            continue

        for nd in [(3 + dir)%4, dir, (dir + 1)%4]:
            if nd == dir and runlen == MUST_TURN:
                continue
            if nd != dir and runlen < MIN_MOVE:
                continue
            nx = x + DS[nd][0]
            ny = y + DS[nd][1]
            if not (0 <= nx < len(losses[0]) and 0 <= ny < len(losses)):
                continue
            nrun = runlen + 1 if nd == dir else 1
            nlost = lost + losses[ny][nx]

            if enqbest[(nx, ny, nd, nrun)] > nlost:
                q.append((nx, ny, nd, nrun, nlost))
                enqbest[(nx, ny, nd, nrun)] = nlost
        
    return best

# 908, 906, 903 all too high

sample = solve("""111111111111
999999999991
999999999991
999999999991
999999999991""")
SAMPLE_EXPECTED2 = 71
if sample != SAMPLE_EXPECTED2:
    print("SAMPLE FAILED: ", sample, " != ", SAMPLE_EXPECTED2)
assert sample == SAMPLE_EXPECTED2
print("\n*** SAMPLE PASSED ***\n")



sample = solve(SAMPLE)
if sample != SAMPLE_EXPECTED:
    print("SAMPLE FAILED: ", sample, " != ", SAMPLE_EXPECTED)
assert sample == SAMPLE_EXPECTED
print("\n*** SAMPLE PASSED ***\n")

solved = solve(REAL)
print("SOLUTION: ", solved)