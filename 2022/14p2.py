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


CHALLENGE_DAY = "14"
REAL = open(CHALLENGE_DAY + ".txt").read()

SAMPLE_EXPECTED = 93
if SAMPLE_EXPECTED:
    SAMPLE = open(CHALLENGE_DAY + ".s.txt").read()


AIR = "."
ROCK = "#"
SOURCE = "+"
SAND = "o"
SOURCE_POS = (500, 0)
def parse_lines(raw):
    world = defaultdict(lambda: "")
    maxy = 0
    for l in raw.split("\n"):
        vertices = []
        for v in l.split(" -> "):
            x, y = map(int, v.split(","))
            vertices.append((x, y))
        for i in range(0, len(vertices) - 1):
            fx, fy = vertices[i]
            tx, ty = vertices[i + 1]
            if fx == tx:
                dx = 0
            else:
                if fx > tx:
                    dx = -1
                else:
                    dx = 1
            if fy == ty:
                dy = 0
            else:
                if fy > ty:
                    dy = -1
                else:
                    dy = 1
            sx = fx
            sy = fy
            while True:
                world[(sx, sy)] = ROCK
                maxy = max(sy + 2, maxy)
                
                if sx == tx and sy == ty:
                    break
                else:
                    sx += dx
                    sy += dy
        
    return world, maxy

        
def solve(raw):
    world, maxy = parse_lines(raw)
    # Debug here to make sure parsing is good.
    settled = 0

    def rock_at(x, y):
        return y == maxy or (x, y) in world

    while True:
        sx, sy = SOURCE_POS
        
# A unit of sand always falls down one step if possible. 
        while True:
            if not rock_at(sx, sy + 1):
                sy += 1
                # if sy == maxy:
                #     return settled
                continue
            # If the tile immediately below is blocked (by rock or sand)
            #   the unit of sand attempts to instead move diagonally one step down and to the left. 
            elif not rock_at(sx - 1, sy + 1):
                sx -= 1
                sy += 1
                continue
            elif not rock_at(sx + 1, sy + 1) :
                sx += 1
                sy += 1
                continue
            else:
                assert not rock_at(sx, sy)
                settled += 1
                if (sx, sy) == SOURCE_POS:
                    return settled
                world[(sx, sy)] = SAND
                # print("settled ", sx, sy)
                break

    return settled

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
import pandas as pd
df=pd.DataFrame([str(solved)])
df.to_clipboard(index=False,header=False)
print("COPIED TO CLIPBOARD")
