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

LEFT = (-1, 0)
UP = (0, -1)
RIGHT = (1, 0)
DOWN = (0, 1)
CHAR_TO_DS = {"^": UP, ">": RIGHT, "<": LEFT, "v": DOWN}
DS = [LEFT, UP, RIGHT, DOWN] # +IDX = TURN RIGHT
UPLEFT = (-1, -1)
UPRIGHT = (1, -1)
DOWNRIGHT = (1, 1)
DOWNLEFT = (-1, 1)
DS8 = [LEFT, UPLEFT, UP, UPRIGHT, RIGHT, DOWNRIGHT, DOWN, DOWNLEFT] # +IDX = TURN RIGHT

def arounds(x, y, diagonals):
    ret = []
    for dx, dy in DS8 if diagonals else DS:
        ret.append((x + dx, y + dy))
    return ret

CHALLENGE_DAY = argv[0].split("/")[-1].replace("p2.py", "").replace(".py", "")
AOC_DIR = os.path.dirname(argv[0])

print("Day: ", CHALLENGE_DAY)

######################
SAMPLE_EXPECTED = 123
######################
assert SAMPLE_EXPECTED != None

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
        # split = list(map(int, line.split(" "))) # All Ints

        # Using Parse Library
        # split = parse("{:d} {:s}", line) # Simple - unnamed
        # split = parse("{name:s} {height:d}", line) # Parse with field names
        # assert split # Make sure line was parsed

        split = list(map(int, line.split("|"))) # All Ints
        assert len(split) != 0
        ret.append(split)

    return ret

def parse_prints(group):
    lines = group.split("\n")
    ret = []
    for line in lines:
        line = line.strip()
        assert len(line) != 0

        # Simple parse - parse as all one type
        split = list(map(int, line.split(","))) # All Ints

        # Using Parse Library
        # split = parse("{:d} {:s}", line) # Simple - unnamed
        # split = parse("{name:s} {height:d}", line) # Parse with field names
        # assert split # Make sure line was parsed

        assert len(split) != 0
        ret.append(split)
    return ret

def parse_lines(raw):
    # Groups.
    rulestr, printstr = raw.split("\n\n")
    # Do something with the groups.

    rules = parse_group(rulestr)
    prints = parse_prints(printstr)

    return rules, prints


def valid_pages(pages, rules):
    for i in range(len(pages)):
        pi = pages[i]
        for j in range(i + 1, len(pages)):
            for must_first, must_later in rules:
                if must_first == pages[j]:
                    if must_later == pi:
                        return False
    return True

def reorder_to_valid(pages, rules):
    ret = []
    for p in pages:
        ret = [p] + ret
        i = 0
        while not valid_pages(ret, rules):
            ret[i], ret[i+1] = ret[i+1], ret[i]
            i += 1
    
    return ret


def solve(raw):
    ret = 0

    rules, prints = parse_lines(raw)
    for pagei, pages in enumerate(prints):
        valid = reorder_to_valid(pages, rules)
        if valid != pages:
            print(pages, "becomes", valid)
            middle = valid[len(valid)//2]
            print(pagei, valid, "is middle:", middle)
            ret += middle

    return ret

sample = solve(SAMPLE)
assert sample == SAMPLE_EXPECTED, "Sample Result %s != %s expected" % (sample, SAMPLE_EXPECTED)
print("\n*** SAMPLE PASSED ***\n")

solved = solve(REAL)
print("SOLUTION: ", solved)
