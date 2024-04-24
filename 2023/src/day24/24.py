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
SAMPLE_EXPECTED = 2
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
    ret = []
    lines = raw.split("\n")
    for l in lines:
        pos, vel = l.split(" @ ")
        x, y, z = [int(a) for a in pos.split(", ")]
        dx, dy, dz = [int(a) for a in vel.split(", ")]
        ret.append(((x,y,z), (dx, dy, dz)))
    return ret

NEGATIVE="-"
NO_SOLUTION="PARALLEL"
def find_intersection(x1, y1, dx1, dy1, x2, y2, dx2, dy2):
    # Matrix form of the equation Ax = b
    # A = [-dx1, dx2]
    #     [-dy1, dy2]
    # x = [t, s]
    # b = [x2 - x1, y2 - y1]
    A = [[dx1, -dx2], [dy1, -dy2]]  # Adjust sign for second line's direction
    b = [x2 - x1, y2 - y1]
    
    # Use numpy for solving the linear system of equations
    import numpy as np
    try:
        solution = np.linalg.solve(A, b)
        t, s = solution
        if t < 0 or s < 0:
            return NEGATIVE
        # Intersection point
        intersection_x = x1 + t * dx1
        intersection_y = y1 + t * dy1
        return intersection_x, intersection_y
    except np.linalg.LinAlgError:
        return NO_SOLUTION

# print("FI", find_intersection(0, 5, 1, -1, 0,0, 1, 1))

print("FIX", find_intersection(20, 25, -2, -2, 20, 19, 1, -5))
# ((20, 25, 34), (-2, -2, -4)) ((20, 19, 15), (1, -5, -3))

def solve(raw, ranges):
    min_range, max_range = ranges
    parsed = parse_lines(raw)
    print(parsed)

    ret = 0

    for i in range(len(parsed)):
        (x1, y1, z1), (dx1, dy1, dz1) = parsed[i]
        for j in range(i + 1, len(parsed)):
            if i == j:
                continue
            (x2, y2, z2), (dx2, dy2, dz2) = parsed[j]
            ints = find_intersection(x1, y1, dx1, dy1, x2, y2, dx2, dy2)
            print(parsed[i], parsed[j], " @ ", ints)
            if ints in [NO_SOLUTION, NEGATIVE]:
                continue
            intx, inty = ints
            if min_range <= intx < max_range and min_range <= inty < max_range:
                print("INSIDE:")
                print(parsed[i], parsed[j], " @ ", ints)
                ret += 1

    return ret # 13737 too high

sample = solve(SAMPLE, (7, 27))
if sample != SAMPLE_EXPECTED:
    print("SAMPLE FAILED: ", sample, " != ", SAMPLE_EXPECTED)
assert sample == SAMPLE_EXPECTED
print("\n*** SAMPLE PASSED ***\n")

solved = solve(REAL, (200000000000000, 400000000000000))
print("SOLUTION: ", solved) # Part1 11098