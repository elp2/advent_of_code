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
SAMPLE_EXPECTED = 40
######################
assert SAMPLE_EXPECTED != None, "Must enter sample value"

def parse_group(group):
    lines = group.split("\n")
    ret = []
    splitters = set()
    for y, line in enumerate(lines):
        line = line.strip()
        assert len(line) != 0
        for x, xc in enumerate(line):
            if xc == "S":
                start = (x, y)
            if xc == "^":
                splitters.add((x, y))

    return start, splitters, len(line), len(lines)


def parse_lines(raw):
    # Groups.
    # groups = raw.split("\n\n")
    # Do something with the groups.

    return parse_group(raw)


def solve(raw):
    (sx, sy), splitters, w, h = parse_lines(raw)

    ret = 0
    q = defaultdict(lambda: 0)
    q[(sx, sy)] = 1

    while True:
        next = defaultdict(lambda: 0)
        for (hx, hy), score in q.items():
            if hy == h:
                ret += score
            elif (hx, hy) in splitters:
                next[(hx - 1, hy + 1)] += score
                next[(hx + 1, hy + 1)] += score
            else:
                next[(hx, hy + 1)] += score

        if hy == h:
            return ret
        q = next


if __name__ == "__main__":
    SAMPLE, REAL = get_raw_inputs(sys.argv)

    sample = solve(SAMPLE)
    assert sample == SAMPLE_EXPECTED, "Sample Result %s != %s expected" % (sample, SAMPLE_EXPECTED)
    print("\n*** SAMPLE PASSED ***\n")

    solved = solve(REAL)
    print("SOLUTION: ", solved)
