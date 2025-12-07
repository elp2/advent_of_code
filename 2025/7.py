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
SAMPLE_EXPECTED = 21
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
    start, splitters, w, h = parse_lines(raw)

    ret = 0
    q = deque([])
    q.append(start)

    split_at = set()
    while len(q):
        hx, hy = q.popleft()
        if (hx, hy) in splitters:
            if (hx, hy) not in split_at:            
                split_at.add((hx, hy))
                print(hx, hy)
                q.append((hx - 1, hy))
                q.append((hx + 1, hy))
        else:
            if hy < h and 0 <= hx < w:
                q.append((hx, hy + 1))

    return len(split_at)

if __name__ == "__main__":
    SAMPLE, REAL = get_raw_inputs(sys.argv)

    sample = solve(SAMPLE)
    assert sample == SAMPLE_EXPECTED, "Sample Result %s != %s expected" % (sample, SAMPLE_EXPECTED)
    print("\n*** SAMPLE PASSED ***\n")

    solved = solve(REAL)
    print("SOLUTION: ", solved)
