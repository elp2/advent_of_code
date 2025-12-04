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
SAMPLE_EXPECTED = 13
######################
assert SAMPLE_EXPECTED != None, "Must enter sample value"

def parse_group(group):
    lines = group.split("\n")
    ret = []
    for y, line in enumerate(lines):
        line = line.strip()
        assert len(line) != 0

        split = line.split(" ")

        for x, xc in enumerate(split):
            pass

        assert len(split) != 0
        ret.append(split)

    return ret


def parse_lines(raw):
    rg = []
    grid = set()
    lines = raw.split("\n")
    w = len(lines[0].strip())
    h = len(lines)
    for y, l in enumerate(lines):
        rg.append(list(l))
        for x, c in enumerate(l):
            if c == "@":
                grid.add((x, y))
    
    return w, h, grid, rg

DS8 = [LEFT, UPLEFT, UP, UPRIGHT, RIGHT, DOWNRIGHT, DOWN, DOWNLEFT] # +IDX = TURN RIGHT
def solve(raw):
    w, h, grid, rg = parse_lines(raw)

    accessibles = set()
    for y in range(h):
        for x in range(w):
            if (x, y) not in grid:
                continue
            arounds = set()
            for (dx, dy) in DS8:
                nx, ny = x + dx, y + dy
                if (nx, ny) in grid:
                    arounds.add((nx, ny))
            if len(arounds) < 4:
                print(x, y, arounds)
                accessibles.add((x, y))
                # for a in arounds:
                #     accessibles.add(a)
    for (x, y) in accessibles:
        assert rg[y][x] == "@"
        rg[y][x] = "x"
    for r in rg:
        print("".join(r))
    return len(accessibles)

if __name__ == "__main__":
    SAMPLE, REAL = get_raw_inputs(sys.argv)

    sample = solve(SAMPLE)
    assert sample == SAMPLE_EXPECTED, "Sample Result %s != %s expected" % (sample, SAMPLE_EXPECTED)
    print("\n*** SAMPLE PASSED ***\n")

    solved = solve(REAL)
    print("SOLUTION: ", solved)
