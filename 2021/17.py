from collections import defaultdict, deque, Counter
from itertools import combinations, combinations_with_replacement, permutations
from functools import reduce
import math
# import numpy as np
from operator import add, mul, itemgetter, attrgetter
import re

DS = [[-1, 0], [1, 0], [0, 1], [0, -1]]
DS8 = DS + [[-1, -1], [1, -1], [-1, 1], [1, 1]]
def arounds_inside(x, y, diagonals, w, h):
    ret = []
    for dx, dy in DS8 if diagonals else DS:
        ret.append((x + dx, y + dy))


CHALLENGE_DAY = "17"
REAL = open(CHALLENGE_DAY + ".txt").read()

SAMPLE_EXPECTED = 112
if SAMPLE_EXPECTED:
    SAMPLE = open(CHALLENGE_DAY + ".s.txt").read()


SUMS={0: 0}
for x in range(1, 1000):
    SUMS[x] = SUMS[x-1] + x



def parse_lines(raw):
    a, b, c, d = [int(x) for x in raw.split(" ")]
    minx, maxx = sorted([a, b])
    miny, maxy = sorted([c, d])
    
    return [minx, maxx, miny, maxy]

MISS_RIGHT = 0
MISS_BELOW = 1
INTERSECT = 2

def fire(vx, vy, minx, maxx, miny, maxy, test=False):
    vyo = vy
    x = 0
    y = 0
    ry = 0
    t = 0

    while True:
        if x > maxx:
            return MISS_RIGHT, ry
        elif y < miny:
            return MISS_BELOW, ry
        elif minx <= x <= maxx and miny <= y <= maxy:
            # print("INT at ", x, y, vx, vy)
            return INTERSECT, ry
        else:
            x += vx
            y += vy
            ry = max(ry, y)
            vx = max(0, vx - 1)
            vy -= 1
            t += 1
            if test:
                assert yatt(vyo, t) == y


def solve1(raw):
    [minx, maxx, miny, maxy] = parse_lines(raw)

    minvx = 10000000
    maxvx = 0
    for vx in range(maxx):
        reached = vx + vx * vx - SUMS[vx]
        print(vx, reached)
        if minx <= reached <= maxx:
            minvx = min(vx, minvx)
            maxvx = max(vx, maxvx)

    print(minvx, maxvx)
    print()

    rymax = 0
    for vx in range(minvx - 20, maxvx + 20):
        print(vx)
        for vy in range(0, 1000, 1):
            result, ry = fire(vx, vy, minx, maxx, miny, maxy)
            if result == INTERSECT:
                print("INT: ", ry, " at", vx, vy)
                rymax = max(ry, rymax)

    return rymax


def yatt(vy, t):
    return t * vy - SUMS[t - 1]

def solve(raw):
    [minx, maxx, miny, maxy] = parse_lines(raw)

    minvx = 10000000
    maxvx = 0
    valid_vxt = set()

    fire(6, 9, minx, maxx, miny, maxy, True)
    fire(28, -6, minx, maxx, miny, maxy, True)
    fire(7, 0, minx, maxx, miny, maxy, True)
    fire(8,0, minx, maxx, miny, maxy, True)


    for vxo in range(1, maxx + 1):
        print(vxo)
        vx = vxo
        x = 0
        t = 0
        while x <= maxx:
            x += vx
            vx -= 1
            t += 1
            if minx <= x <= maxx:
                valid_vxt.add((vxo, t))
                if vx == 0:
                    valid_vxt.add((vxo, str(t) + "+"))
            if vx == 0:
                break
    
    print(len(valid_vxt))

    vels = set()
    for vy in range(miny, abs(miny)):
        for vx, t in valid_vxt:
            # print(vx, vy)
            # for t in range(1, 174):
            #     if miny <= yatt(vy, t) <= maxy:
            #         vels.add((vx, vy))              

            if type(t) == str:
                tfrom = int(t.replace("+", ""))
                # special case where it's falling
                for t in range(tfrom, 500):
                    if miny <= yatt(vy, t) <= maxy:
                        vels.add((vx, vy))
                        break
            else:
                if miny <= yatt(vy, t) <= maxy:
                    vels.add((vx, vy))
    
    checks = """23,-10  25,-9   27,-5   29,-6   22,-6   21,-7   9,0     27,-7   24,-5
25,-7   26,-6   25,-5   6,8     11,-2   20,-5   29,-10  6,3     28,-7
8,0     30,-6   29,-8   20,-10  6,7     6,4     6,1     14,-4   21,-6
26,-10  7,-1    7,7     8,-1    21,-9   6,2     20,-7   30,-10  14,-3
20,-8   13,-2   7,3     28,-8   29,-9   15,-3   22,-5   26,-8   25,-8
25,-6   15,-4   9,-2    15,-2   12,-2   28,-9   12,-3   24,-6   23,-7
25,-10  7,8     11,-3   26,-7   7,1     23,-9   6,0     22,-10  27,-6
8,1     22,-8   13,-4   7,6     28,-6   11,-4   12,-4   26,-9   7,4
24,-10  23,-8   30,-8   7,0     9,-1    10,-1   26,-5   22,-9   6,5
7,5     23,-6   28,-10  10,-2   11,-1   20,-9   14,-2   29,-7   13,-3
23,-5   24,-8   27,-9   30,-7   28,-5   21,-10  7,9     6,6     21,-5
27,-10  7,2     30,-9   21,-8   22,-7   24,-9   20,-6   6,9     29,-5
8,-2    27,-8   30,-5   24,-7"""

    # missing = set()
    # seen = set()
    # for l in checks.split("\n"):
    #     for pair in l.split(" "):
    #         if len(pair):
    #             a, b = pair.split(",")
    #             if (int(a), int(b)) in vels:
    #                 vels.remove((int(a), int(b)))
    #                 seen.add(pair)
    #             else:
    #                 missing.add(pair)
          
                  


    return len(vels)


if SAMPLE_EXPECTED != None:
    sample = solve(SAMPLE)
    if sample != SAMPLE_EXPECTED:
        print("SAMPLE FAILED: ", sample, " != ", SAMPLE_EXPECTED)
    assert sample == SAMPLE_EXPECTED
    print("\n*** SAMPLE PASSED ***\n")
else:
    print("Skipping sample")

solved = solve(REAL) # 780 too low # 3118 low
print("SOLUTION: ", solved)
import pandas as pd
df=pd.DataFrame([str(solved)])
df.to_clipboard(index=False,header=False)
print("COPIED TO CLIPBOARD")
