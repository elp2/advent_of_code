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

CHALLENGE_DAY = argv[0].split("/")[-1].replace(".py", "").replace("p2.py", "")
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
    return lines


def solve(raw):
    world = parse_lines(raw)
    print(world)

    def wat(x, y):
        if 0 > y or y >= len(world):
            return None
        if 0 <= x < len(world[0]):
            return world[y][x]
        return None

    sx = 1
    sy = 0
    ex = len(world[0]) - 2
    ey = len(world) - 1

    q = deque()
    q.append((sx, sy, set()))
    longest = 0
    while len(q):
        x, y, path = q.popleft()
        if x == ex and y == ey:
            print("Longest: ", len(path))
            longest = max(len(path), longest)
            continue
        options = []
        for dchar in "^<v>":
            dx, dy = DS[CHAR_TO_DS[dchar]]
            nx, ny = x + dx, y + dy
            nchar = wat(nx, ny)
            if None == nchar or (nx, ny) in path or nchar == "#":
                continue
            if nchar in "^v<>" and dchar != nchar:
                continue

            path_copy = path.copy()
            path_copy.add((nx, ny))

            if dchar == nchar:
                # advance again on slopes
                nx, ny = nx + dx, ny + dy
                path_copy.add((nx, ny))
            
            options.append((nx, ny, path_copy))
        for o in options:
            q.append(o)

    return longest

sample = solve(SAMPLE)
if sample != SAMPLE_EXPECTED:
    print("SAMPLE FAILED: ", sample, " != ", SAMPLE_EXPECTED)
assert sample == SAMPLE_EXPECTED
print("\n*** SAMPLE PASSED ***\n")

solved = solve(REAL)
print("SOLUTION: ", solved)