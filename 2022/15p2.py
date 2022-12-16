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

SAMPLE_EXPECTED = 56000011
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

    for s in sensor_exclusion.keys():
        print("Testing ", s)
        outside_dist = sensor_exclusion[s] + 1

        sx = s[0]
        sy = s[1]

        edges = [(sx, sy - outside_dist), (sx + outside_dist, sy), (sx, sy + outside_dist), (sx - outside_dist, sy)]
        ds = [(1, 1), (-1, 1), (-1, -1), (1, -1)]
        min_md = 0

        for i in range(4):
            tx, ty = edges[i]
            assert manhattan((tx, ty), s) == outside_dist
            dx, dy = ds[i]
            next_edge = edges[(i+1+4) % 4]
            while (tx, ty) != next_edge: # TODO optimize - if we're jumping big diffs, can't expect to hit the edge exactly.
                if min_md > 100:
                    hdx = dx * min_md // 10
                    hdy = dy * min_md // 10
                else:
                    hdx = dx
                    hdy = dy
                # print((tx, ty), next_edge)
                # if tx == 14 and ty == 11:
                #     print("!")
                if not 0 <= tx <= solve_row or not 0 <= ty <= solve_row:
                    tx += hdx
                    ty += hdy
                    continue
                
                min_md = 10000000
                outside_sensors = True
                for os in sensor_exclusion.keys():
                    ost_md = sensor_exclusion[os]
                    om = manhattan((tx, ty), (os))
                    min_md = min(min_md, om)
                    if om <= ost_md:
                        outside_sensors = False
                        break

                if outside_sensors:
                    if (tx, ty) in beacons_on:
                        print((tx, ty), " is actually a beacon!")
                    else:
                        print("Hidden beacon! ", tx, ty)
                        return 4000000 * tx + ty
                tx += hdx
                ty += hdy
    assert False


if SAMPLE_EXPECTED != None:
    sample = solve(SAMPLE, 20)
    if sample != SAMPLE_EXPECTED:
        print("SAMPLE FAILED: ", sample, " != ", SAMPLE_EXPECTED)
    assert sample == SAMPLE_EXPECTED
    print("\n*** SAMPLE PASSED ***\n")
else:
    print("Skipping sample")

solved = solve(REAL, 4000000)
print("SOLUTION: ", solved)
