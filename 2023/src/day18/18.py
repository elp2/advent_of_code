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


CHAR_TO_DS = {"^": 3, ">": 1, "<": 0, "v": 2, "U": 3, "R": 1, "L": 0, "D": 2}
DS = [(-1, 0), (1, 0), (0, 1), (0, -1)]
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
SAMPLE_EXPECTED = 62
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


def get_lines(raw, part1=True):
    
    lines = raw.split("\n")
    positions = [(0,0)]
    line_dist = 0

    trenches = []

    for l in lines:
        dir = None
        llen = None
        a, b, c = l.split(" ")
        if part1:
            dir, llen = DS[CHAR_TO_DS[a]], int(b)
        else:
            llen = int(c[2:7], 16)
            dchar = c[7]
            dir = DS[CHAR_TO_DS[{"0": "R", "1": "D", "2": "L", "3": "U"}[dchar]]] # 0 means R, 1 means D, 2 means L, and 3 means U.
        pos = (positions[-1][0] + dir[0] * llen, positions[-1][1] + dir[1] * llen)
        line_dist += abs(dir[0] * llen) + abs(dir[1] * llen) - 1

        ppos = positions[-1]
        if ppos[0] < pos[0] or ppos[1] < pos[1]:
            trenches.append((ppos, pos))
        else:
            trenches.append((pos, ppos))

        positions.append(pos)
    assert positions[-1] == (0, 0)
    return positions, line_dist, trenches

def shoelace(positions):
    plusses = negatives = 0
    for i in range(len(positions) - 1):
        plusses += positions[i][0] * positions[i+1][1]
        negatives += positions[i][1] * positions[i + 1][0]
    return abs(plusses - negatives) // 2

def corner_area(positions, trenches):
    # Corners can either contribute 3/4 of a sq or 1/4 in the shifted 0.5 thing.
    # n = num corners
    # num_corners = threes + ones
    # threes * 3 + ones = corner_area (which must be evenly divisible)
    # ones = num_corners - threes
    # threes * 3 + num_corners - threes = corner_area
    # threes * 2 + num_corners = corner_area

    def trenches_intersected(x, y):
        intersected = 0
        for ((ax, ay), (bx, by)) in trenches:
            if ay == by:
                continue
            if ax < x and ay <= y <= by:
                intersected += 1
        return intersected

    outsides = 0
    for (x, y) in positions[:-1]:
        for (dx, dy) in [(-1, -1), (1, 1), (1, -1), (-1, 1)]:
            hx = 0.25 * dx + x
            hy = 0.25 * dy + y
            if trenches_intersected(hx, hy) % 2 == 0:
                outsides += 1

    print("outsides??", outsides % 4)
    assert outsides % 4 == 0
    return outsides // 4



def solve(raw, part1):
    positions, line_dist, trenches = get_lines(raw, part1)

    # Area = 

    ret = shoelace(positions)
    # Then if we shift the whole thing down 0.5 to the right/down, we have to figure out the fractionals
    # this is 1/2 of the non corner pieces of the lines
    ret += line_dist // 2
    ret += corner_area(positions, trenches)

    return ret


sample = solve("""R 3 (#70c710)
D 3 (#0dc571)
L 3 (#5713f0)
U 3 (#d2c081)""", True)
if sample != 16:
    print("SAMPLE FAILED: ", sample, " != ", 16)
assert sample == 16
print("\n*** SAMPLE PASSED ***\n")

# sample = solve("""R 3 (#70c710)
# D 3 (#0dc571)
# R 3 (#5713f0)
# D 3 (#d2c081)
# L 6 (#d2c081)
# U 6 (#d2c081)""", True)
# if sample != 16:
#     print("SAMPLE FAILED: ", sample, " != ", 16)
# assert sample == 16
# print("\n*** SAMPLE PASSED ***\n")


sample = solve(SAMPLE, True)
if sample != SAMPLE_EXPECTED:
    print("SAMPLE FAILED: ", sample, " != ", SAMPLE_EXPECTED)
assert sample == SAMPLE_EXPECTED
print("\n*** SAMPLE PASSED ***\n")

solved = solve(REAL, True)
print("SOLUTION: ", solved)

SAMPLE_EXPECTED=952408144115
sample = solve(SAMPLE, False)
if sample != SAMPLE_EXPECTED:
    print("SAMPLE FAILED: ", sample, " != ", SAMPLE_EXPECTED)
assert sample == SAMPLE_EXPECTED
print("\n*** SAMPLE PASSED ***\n")

solved = solve(REAL, False)
print("SOLUTION: ", solved)
