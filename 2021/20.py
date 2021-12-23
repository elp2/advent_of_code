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


CHALLENGE_DAY = "20"
REAL = open(CHALLENGE_DAY + ".txt").read()

def parse_lines(raw):
    algo, pstr = raw.split("\n\n")

    pixels = set()
    for y, l in enumerate(pstr.split("\n")):
        for x, v in enumerate(l):
            if v == "#":
                pixels.add((x, y))

    assert 512 == len(algo)
    algo = set(i for i in range(len(algo)) if algo[i] == "#")
    return algo, pixels


def solve(raw):
    algo, pixels = parse_lines(raw)

    truew = max(px for px, _ in pixels)
    trueh = max(py for _, py in pixels)

    for round in range(2):
        boundary_expected = 1 if round % 2 == 1 and 0 in algo else 0


        bw1 = min(px for px, _ in pixels) - 1 - round
        bh1 = min(py for _, py in pixels) - 1 - round
        bw2 = max(px for px, _ in pixels) + 1 + round
        bh2 = max(py for _, py in pixels) + 1 + round
        print(sw, sh, w, h)

        def value(pixels, x, y):
            if x <= sw or x >= w or y <= sh or y >= h:
                return boundary_expected
            else:
                return 1 if (x, y) in pixels else 0
            
        for y in range(-3, trueh - 3):
            print("".join(["#" if value(pixels, x, y) else "." for x in range(-3, truew + 3)]))

        next = set()


        def conv_key(x, y):
            if (x, y) == (-1, -1):
                print("1")
            ret = 0
            for dy in [-1, 0, 1]:
                for dx in [-1, 0, 1]:
                    nx = x + dx
                    ny = y + dy
                    ret = ret << 1
                    ret |= value(pixels, x, y)
            return ret
        
        for y in range(sh, h + 1):
            for x in range(sw, w + 1):
                if conv_key(x, y) in algo:
                    next.add((x, y))

        pixels = next
    return (len(pixels), None)


solved, p2 = solve(REAL) # 5962 high # 5294 low
print("SOLUTION: ", solved)
assert 5294 < solved < 5962
assert 5681 != solved
assert 5487 != solved

SAMPLE_EXPECTED = (35, None)
if SAMPLE_EXPECTED:
    SAMPLE = open(CHALLENGE_DAY + ".s.txt").read()

if SAMPLE_EXPECTED != None:
    sample = solve(SAMPLE)
    if sample != SAMPLE_EXPECTED:
        print("SAMPLE FAILED: ", sample, " != ", SAMPLE_EXPECTED)
    assert sample == SAMPLE_EXPECTED
    print("\n*** SAMPLE PASSED ***\n")
else:
    print("Skipping sample")

