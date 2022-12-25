from collections import defaultdict, deque, Counter
from itertools import combinations, combinations_with_replacement, permutations
from functools import reduce, cmp_to_key
import math
# import numpy as np
from operator import add, mul, itemgetter, attrgetter
import re
from sys import argv

def flatten(t):
    return [item for sublist in t for item in sublist]

# Sorts with cmp. cmp < 0 for a < b, == 0 for a==b, > 0 for a > b.
def elpsort(array, cmp):
    return sorted(array, key=cmp_to_key(cmp))

ON_TEXT = '\u2588'
OFF_TEXT = '\u2592'

CHAR_TO_DS = {"^": 3, ">": 1, "<": 0, "v": 2}
DS = [(-1, 0), (1, 0), (0, 1), (0, -1)]
DS8 = DS + [(-1, -1), (1, -1), (-1, 1), (1, 1)]
def arounds(x, y, diagonals):
    ret = []
    for dx, dy in DS8 if diagonals else DS:
        ret.append((x + dx, y + dy))
    return ret

CHALLENGE_DAY = argv[0].split("/")[-1].replace(".py", "").replace("p2.py", "")
print("Day: ", CHALLENGE_DAY)
REAL = open(CHALLENGE_DAY + ".txt").read()

SAMPLE_EXPECTED = TODO
if SAMPLE_EXPECTED:
    SAMPLE = open(CHALLENGE_DAY + ".s.txt").read()


def parse_lines(raw):
    # Groups.
    # groups = raw.split("\n\n")
    # return list(map(lambda group: group.split("\n"), groups))
    # lines = raw.split("\n")
    # return lines # raw
    # return list(map(lambda l: l.split(" "), lines)) # words.
    # return list(map(int, lines))
    # return list(map(lambda l: l.strip(), lines)) # beware leading / trailing WS
    1
def solve(raw):
    parsed = parse_lines(raw)
    # Debug here to make sure parsing is good.
    ret = 0

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