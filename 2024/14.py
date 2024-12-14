from collections import defaultdict, deque, Counter
from itertools import combinations, combinations_with_replacement, permutations, product
from functools import reduce, cmp_to_key
from operator import add, mul, itemgetter, attrgetter
import os
from parse import parse
import sys

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, root_dir)
from aoc_elp import *

######################
SAMPLE_EXPECTED = 12
######################
assert SAMPLE_EXPECTED != None, "Must enter sample value"

def parse_group(group):
    lines = group.split("\n")
    ret = []
    for y, line in enumerate(lines):
        line = line.strip()
        assert len(line) != 0
        # p=0,4 v=3,-3
        line = line.replace("=", " ")
        line = line.replace(",", " ")
        split = line.split(" ")
        
        here = []
        for x, xc in enumerate(split):
            try:
                here.append(int(xc))
            except:
                pass

        assert len(here) == 4
        ret.append(here)

    return ret


def parse_lines(raw):
    # Groups.
    # groups = raw.split("\n\n")
    # Do something with the groups.

    return parse_group(raw)


def solve(raw, w, h, seconds):
    robots = parse_lines(raw)
    print(robots)

    for t in range(seconds):
        for r in range(len(robots)):
            rx, ry, vx, vy = robots[r]
            rx = (rx + vx + w) % w
            ry = (ry + vy + h) % h
            robots[r] = rx, ry, vx, vy

    quads = [0, 0, 0, 0]
    w2 = w // 2
    h2 = h // 2
    ignorex = w2
    ignorey = h2

    for r in range(len(robots)):
        qi = 0
        rx, ry, vx, vy = robots[r]
        if rx == ignorex or ry == ignorey:
            continue
        if rx > ignorex:
            qi += 1
        if ry > ignorey:
            qi += 2
        quads[qi] += 1

    print(quads)
    return quads[0] * quads[1] * quads[2] * quads[3]

if __name__ == "__main__":
    SAMPLE, REAL = get_raw_inputs(sys.argv)

    sample = solve(SAMPLE, 11, 7, 100)
    assert sample == SAMPLE_EXPECTED, "Sample Result %s != %s expected" % (sample, SAMPLE_EXPECTED)
    print("\n*** SAMPLE PASSED ***\n")

    solved = solve(REAL, 101, 103, 100)
    print("SOLUTION: ", solved)
