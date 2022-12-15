from collections import defaultdict, deque, Counter
from itertools import combinations, combinations_with_replacement, permutations
from functools import reduce
import math
import numpy as np
from operator import add, mul, itemgetter, attrgetter
import re

DS = [[-1, 0], [1, 0], [0, 1], [0, -1]]
DS8 = DS + [[-1, -1], [1, -1], [-1, 1], [1, 1]]
def arounds_inside(x, y, diagonals, w, h):
    ret = []
    for dx, dy in DS8 if diagonals else DS:
        ret.append((x + dx, y + dy))


CHALLENGE_DAY = "15"
REAL = open(CHALLENGE_DAY + ".txt").read()

SAMPLE_EXPECTED = 26
if SAMPLE_EXPECTED:
    SAMPLE = open(CHALLENGE_DAY + ".s.txt").read()


def parse_lines(raw, solve_row):
    sensor_exclusion = {}
    lines = raw.split("\n")
    # Sensor at x=2, y=18: closest beacon is at x=-2, y=15
    minx = None
    maxx = None
    beacons_on = set()
    for l in lines:
        l = l.replace(",", "")
        l = l.replace(":", "")
        def eqs(st):
            return int(st.split("=")[1].replace(",", ""))
        
        s = l.split(" ")
        sx = eqs(s[2])
        sy = eqs(s[3])
        bx = eqs(s[8])
        by = eqs(s[9])
        if by == solve_row:
            beacons_on.add((bx, by))

        md = abs(sx - bx) + abs(sy - by)
        minx = sx - md if minx == None else min(sx - md, minx)
        maxx = sx + md if maxx == None else max(sx + md, maxx)

        sensor_exclusion[(sx, sy)] = md

    return sensor_exclusion, minx, maxx, beacons_on

def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def solve(raw, solve_row):
    sensor_exclusion, minx, maxx, beacons_on = parse_lines(raw, solve_row)
    num_cannot_contain = 0
    
    for x in range(minx-100, maxx + 100):
        if x % 10000 == 0:
            print(x, num_cannot_contain)
        impossible = False
        for s in sensor_exclusion.keys():
            if manhattan(s, (x, solve_row)) <= sensor_exclusion[s]:
                impossible = True
                break
        if impossible:
            num_cannot_contain += 1


    return num_cannot_contain - len(beacons_on)

if SAMPLE_EXPECTED != None:
    sample = solve(SAMPLE, 10)
    if sample != SAMPLE_EXPECTED:
        print("SAMPLE FAILED: ", sample, " != ", SAMPLE_EXPECTED)
    assert sample == SAMPLE_EXPECTED
    print("\n*** SAMPLE PASSED ***\n")
else:
    print("Skipping sample")

solved = solve(REAL, 2000000)
print("SOLUTION: ", solved)
