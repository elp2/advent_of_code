from collections import defaultdict, deque, Counter
from itertools import combinations, combinations_with_replacement, permutations, product
from functools import reduce, cmp_to_key
from operator import add, mul, itemgetter, attrgetter
import os
from parse import parse
import re
import sys

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, root_dir)
from aoc_elp import *

######################
SAMPLE_EXPECTED = 480
######################
assert SAMPLE_EXPECTED != None, "Must enter sample value"

def parse_group(group):
    lines = group.split("\n")
    ret = []
    # parse("{name:s} {height:d}", line) # Parse with field names
    ax = ay = bx = by = px = py = None
    ax, ay = map(int, re.findall(r"\d+", lines[0]))
    bx, by = map(int, re.findall(r"\d+", lines[1]))
    px, py = map(int, re.findall(r"\d+", lines[2]))
    # parse("Button A: X+{ax:d}, Y+{ay:d}", lines[0])
    # parse("Button B: X+{bx:d}, Y+{by:d}", lines[1])
    # parse("Prize: X={px:d}, Y={py:d}", lines[2])
    return ((ax, ay), (bx, by), (px, py))


def parse_lines(raw):
    # Groups.
    groups = raw.split("\n\n")
    ret = []
    for g in groups:
        ret.append(parse_group(g))
    return ret

def group_cost(g):
    ((ax, ay), (bx, by), (px, py)) = g

    poss = []
    for a in range(101):
        xrem = px - a * ax
        yrem = py - a * ay
        if xrem % bx == 0 and yrem % by == 0:
            b = int(xrem / bx)
            ex, ey = int(a * ax + b * bx), int(a * ay + b * by)
            if (ex, ey) != (px, py):
                continue
            if b > 100 or a > 100 or b < 0 or a < 0:
                continue
            else:
                poss.append(int(a * 3 + b))

    for b in range(101):
        xrem = px - b * bx
        yrem = py - b * by
        if xrem % ax == 0 and yrem % ay == 0:
            a = int(xrem / ax)

            ex, ey = int(a * ax + b * bx), int(a * ay + b * by)
            if (ex, ey) != (px, py):
                continue

            if b > 100 or a > 100 or b < 0 or a < 0:
                continue
            else:
                poss.append(int(a * 3 + b))



    # alen = max(max(px // ax + 1, py // ay + 1), 105)
    # for a in range(px):
    #     xrem = px - a * ax
    #     yrem = py - a * ay
    #     if xrem % bx == 0 and yrem % by == 0:
    #         b = xrem / bx
    #         if b > 100 or a > 100:
    #             continue
    #         else:
    #             poss.append(int(a * 3 + b))
    if len(poss) == 0:
        return 0
    else:
        return min(poss)


def solve(raw):
    groups = parse_lines(raw)
    print(groups)

    ret = 0
    for g in groups:
        gc = group_cost(g)
        print(g, gc)
        ret += gc
    return ret

if __name__ == "__main__":
    SAMPLE, REAL = get_raw_inputs(sys.argv)

    sample = solve(SAMPLE)
    assert sample == SAMPLE_EXPECTED, "Sample Result %s != %s expected" % (sample, SAMPLE_EXPECTED)
    print("\n*** SAMPLE PASSED ***\n")

    solved = solve(REAL)
    assert solved < 69495
    assert solved != 27638
    assert solved != 30164
    assert solved != 29702
    assert solved != 25281
    print("SOLUTION: ", solved)
