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


CHALLENGE_DAY = "22"
REAL = open(CHALLENGE_DAY + ".txt").read()

SAMPLE_EXPECTED = 39
if SAMPLE_EXPECTED:
    SAMPLE = open(CHALLENGE_DAY + ".s.txt").read()


def parse_lines(raw):
    ret = []
    for l in raw.split("\n"):
        state, ranges = l.split(" ")
        x1, x2, y1, y2, z1, z2 = [int(a) for a in re.findall(r"-?\d+", l)]
        ret.append((state, ( x1, x2, y1, y2, z1, z2)))

    return ret

def solve(raw):
    parsed = parse_lines(raw)
    # Debug here to make sure parsing is good.
    ret = 0

    squares = set()
    for (state, ( x1, x2, y1, y2, z1, z2)) in parsed:
        for x in range(max(-50, x1), min(50 + 1, x2 + 1)):
            for y in range(max(-50, y1), min(50 + 1, y2 + 1)):
                for z in range(max(-50, z1), min(50 + 1, z2 + 1)):
                    if state == "on":
                        squares.add((x, y, z))
                    else:
                        if (x, y, z) in squares:
                            squares.remove((x, y, z))

    


        # if x1 > 50 or y1 > 50 or z1 > 50 or x2 <-50 or y2 <-50 or z2 < -50:
        #     print("skipping ", x1, x2, y1, y2, z1, z2)
        

    return len(squares)

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
