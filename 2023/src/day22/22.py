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
SAMPLE_EXPECTED = 7
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
    ret = []
    for l in lines:
        a, b = l.split("~")
        p1 = tuple([int(q) for q in a.split(",")])
        p2 = tuple([int(q) for q in b.split(",")])
        for v in [0,1,2]:
            assert p1[v] <= p2[v]
        ret.append((p1, p2))
    return ret


def solve(raw):
    cubes = parse_lines(raw)

    def xyoverlap(c1, c2):
        (c1x1, c1y1, c1z1), (c1x2, c1y2, c1z2) = c1
        (c2x1, c2y1, c2z1), (c2x2, c2y2, c2z2) = c2
        xoverlap = c1x1 <= c2x1 <= c1x2 or c1x1 <= c2x2 <= c1x2 or c2x1 <= c1x1 <= c2x2 or c2x1 <= c1x2 <= c2x2
        yoverlap = c1y1 <= c2y1 <= c1y2 or c1y1 <= c2y2 <= c1y2 or c2y1 <= c1y1 <= c2y2 or c2y1 <= c1y2 <= c2y2
        return xoverlap and yoverlap

    fallen = defaultdict(lambda: [])
    tofall = defaultdict(lambda: [])
    for c in cubes:
        z = c[0][2]
        tofall[z].append(c)

    fallen_bottoms = defaultdict(lambda: [])
    
    supports = defaultdict(lambda: [])
    supportedby = defaultdict(lambda: [])

    for bottomz in sorted(tofall.keys()):
        for cube in tofall[bottomz]:
            (x1, y1, z1), (x2, y2, z2) = cube
            
            fellonto = []
            for z in range(z1 - 1, 0, -1):
                fellonto = []
                for supportcube in fallen[z]:
                    if xyoverlap(supportcube, cube):
                        fellonto.append(supportcube)
                if len(fellonto):
                    break
            if not len(fellonto):
                supportz = 0
            else:
                supportz = fellonto[0][1][2]
            falldistance = z1 - supportz - 1
            # fd supportz + 1 = z1 - 
            fellcube = ((x1, y1, z1 - falldistance), (x2, y2, z2 - falldistance))
            # print(cube, "->", fellcube)
            fallen_bottoms[fellcube[0][2]].append(fellcube)
            fallen[fellcube[1][2]].append(fellcube)
            supportedby[fellcube] = supportedby[fellcube]
            supports[fellcube] = supports[fellcube]
            for f in fellonto:
                supportedby[fellcube].append(f)
                supports[f].append(fellcube)

    sum_disintigrated = 0

    def cubes_supported_only_by(cube):
        removed = set([cube])
        for z in sorted(fallen_bottoms.keys()):
            if z <= cube[1][2]:
                continue
            for maybe_supported in fallen_bottoms[z]:
                num_supporting = 0
                for sup in supportedby[maybe_supported]:
                    if sup not in removed:
                        num_supporting += 1
                if num_supporting == 0:
                    removed.add(maybe_supported)
            
        
        return removed

    for c in supports.keys():
        here = cubes_supported_only_by(c) - set([c])
        print("------\n", c, " -> (", len(here), ")", here)
        sum_disintigrated += len(here) 
    
    return sum_disintigrated # 59502 too low

sample = solve(SAMPLE)
if sample != SAMPLE_EXPECTED:
    print("SAMPLE FAILED: ", sample, " != ", SAMPLE_EXPECTED)
assert sample == SAMPLE_EXPECTED
print("\n*** SAMPLE PASSED ***\n")

solved = solve(REAL)
print("SOLUTION: ", solved)