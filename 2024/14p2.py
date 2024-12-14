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

    t = 0
    while True:
        ats = set()
        for r in range(len(robots)):
            rx, ry, vx, vy = robots[r]
            rx = (rx + vx + w) % w
            ry = (ry + vy + h) % h
            robots[r] = rx, ry, vx, vy
            ats.add((rx, ry))
        t += 1

        shouldexit = False
        prev_count = 0
        rows = []
        for y in range(h):
            row = []
            for x in range(w):
                if (x, y) in ats:
                    row.append(ON_CHAR)
                    prev_count += 1
                else:
                    row.append(OFF_CHAR)
                    prev_count = 0
                if prev_count > 10:
                    shouldexit = True
            
            rows.append(row)
        if shouldexit:
            print("After ", t, "seconds")

            for row in rows:
                print("".join(row))
            shouldexit = False



if __name__ == "__main__":
    SAMPLE, REAL = get_raw_inputs(sys.argv)

    solved = solve(REAL, 101, 103, 100)
    print("SOLUTION: ", solved)
