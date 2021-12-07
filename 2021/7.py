from collections import defaultdict, deque, Counter
from itertools import combinations, combinations_with_replacement, permutations
import math
# import numpy as np
from operator import add, mul, itemgetter, attrgetter
import re

CHALLENGE_DAY = "7"
REAL = open(CHALLENGE_DAY + ".txt").read()

SAMPLE_EXPECTED = 37
if SAMPLE_EXPECTED:
    SAMPLE = open(CHALLENGE_DAY + ".s.txt").read()


def parse_lines(raw):
    return [int(p) for p in raw.split(",")]
    # Groups.
    # groups = raw.split("\n\n")
    # return list(map(lambda group: group.split("\n"), groups))
    # lines = raw.split("\n")
    # return lines # raw
    # return list(map(lambda l: l.split(" "), lines)) # words.
    # return list(map(int, lines))
    # return list(map(lambda l: l.strip(), lines)) # beware leading / trailing WS

def score(crabs, at):
    ret = 0
    for c in crabs:
        ret += abs(c - at)

    return ret

def solve(raw):
    parsed = parse_lines(raw)
    # Debug here to make sure parsing is good.
    ret = 0
    
    scores = [score(parsed, at) for at in range(min(parsed), max(parsed), 1)]
    print(scores)

    return min(scores)

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
