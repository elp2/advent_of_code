from collections import defaultdict, deque, Counter
from itertools import combinations, combinations_with_replacement, permutations
import math
from operator import add, mul, itemgetter, attrgetter
import re
from typing import DefaultDict

CHALLENGE_DAY = "5"
REAL = open(CHALLENGE_DAY + ".txt").read()
SAMPLE_EXPECTED = 12
if SAMPLE_EXPECTED:
    SAMPLE = open(CHALLENGE_DAY + ".s.txt").read()
# SAMPLE_EXPECTED =


def parse_lines(raw):
    # Groups.
    # groups = raw.split("\n\n")
    # return list(map(lambda group: group.split("\n"), groups))
    lines = raw.split("\n")
    # 5,5 -> 8,2
    ret = []
    for l in lines:
        a, b = l.split(" -> ")
        ax, ay = a.split(",")
        ax = int(ax)
        ay = int(ay)

        bx, by = b.split(",")
        bx = int(bx)
        by = int(by)
        ret.append(((ax, ay), (bx, by)))
    return ret
    # return lines # raw
    # return list(map(lambda l: l.split(" "), lines)) # words.
    # return list(map(int, lines))
    # return list(map(lambda l: l.strip(), lines)) # beware leading / trailing WS

def solve(raw):
    parsed = parse_lines(raw)
    # Debug here to make sure parsing is good.

    ret = 0
    points = DefaultDict(lambda: 0)
    for (ax, ay), (bx, by) in parsed:
        dx = bx - ax
        dy = by - ay
        # if dx != 0 and dy != 0:
        #     print("skip", (ax, ay), (bx, by))
        #     continue
        # print("cont: ", (ax, ay), (bx, by))
        
        if dx != 0:
            steps = abs(dx)
        else:
            steps = abs(dy)
        for s in range(steps + 1):
            nx = ax + s * (dx / steps)
            ny = ay + s * (dy / steps)
            # print((nx, ny))
            points[(nx, ny)] += 1
    
    return len([v for v in points.values() if v > 1])

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
