from collections import defaultdict, deque, Counter
from itertools import combinations, combinations_with_replacement, permutations
from functools import reduce, cmp_to_key
import math
# import numpy as np
from operator import add, mul, itemgetter, attrgetter
from parse import parse
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

CHALLENGE_DAY = argv[0].split("/")[-1].replace("p2.py", "").replace(".py", "")
AOC_DIR = os.path.dirname(argv[0])

print("Day: ", CHALLENGE_DAY)

######################
SAMPLE_EXPECTED = 4
######################
assert SAMPLE_EXPECTED != None, "Need to set sample expected"

try:
    sample_file = os.path.join(AOC_DIR, CHALLENGE_DAY + ".s.txt")
    SAMPLE = open(sample_file).read()
except:
    assert None, "Missing Sample File: %s" % (sample_file)

try:
    solutions_file = os.path.join(AOC_DIR, CHALLENGE_DAY + ".txt")
    REAL = open(solutions_file).read()
except:
    assert None, "Missing Solutions File: %s" % (solutions_file)

def parse_group(group):
    lines = group.split("\n")
    ret = []
    for line in lines:
        line = line.strip()
        assert len(line) != 0

        # Simple parse - parse as all one type
        split = list(map(int, line.split(" "))) # All Ints

        # Using Parse Library
        # split = parse("{:d} {:s}", line) # Simple - unnamed
        # split = parse("{name:s} {height:d}", line) # Parse with field names
        # assert split # Make sure line was parsed

        assert len(split) != 0
        ret.append(split)

    return ret


def parse_lines(raw):
    # Groups.
    # groups = raw.split("\n\n")
    # Do something with the groups.

    return parse_group(raw)


def solve(raw):
    parsed = parse_lines(raw)
    print(parsed)

    def ok(r):
        diffs = []
        for i in range(len(r) - 1):
            diff = r[i] - r[i + 1]
            if not (1 <= abs(diff) <= 3):
                return False
            diffs.append(diff)
        
        gts = [x > 0 for x in diffs]
        lts = [x < 0 for x in diffs]
        return all(gts) or all(lts)

    ret = 0
    for orig in parsed:
        if ok(orig):
            ret += 1
            continue

        for i in range(len(orig)):
            report = orig[:]
            report.pop(i)
            if ok(report):
                ret += 1
                break

    return ret

sample = solve(SAMPLE)
assert sample == SAMPLE_EXPECTED, "Sample Result %s != %s expected" % (sample, SAMPLE_EXPECTED)
print("\n*** SAMPLE PASSED ***\n")

solved = solve(REAL)
print("SOLUTION: ", solved)
