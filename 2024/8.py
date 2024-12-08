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
SAMPLE_EXPECTED = 14
######################
assert SAMPLE_EXPECTED != None, "Must enter sample value"

def parse_group(group):
    lines = group.split("\n")
    ret = []
    ats = defaultdict(lambda: [])
    for y, line in enumerate(lines):
        line = line.strip()
        assert len(line) != 0

        split = list(line)

        assert len(split) != 0
        ret.append(split)
        for x, xc in enumerate(split):
            if xc != ".":
                ats[xc].append((x, y))

    return ret, ats


def parse_lines(raw):
    # Groups.
    # groups = raw.split("\n\n")
    # Do something with the groups.

    return parse_group(raw)


def solve(raw):
    board, ats = parse_lines(raw)
    print(board)

    ret = 0
    antinodes = set()
    for freq, locations in ats.items():
        for a, b in combinations(locations, 2):
            ax, ay = a
            bx, by = b
            dx = ax - bx
            dy = ay - by
            arounds = [(ax + dx, ay + dy), (ax - dx, ay - dy), (bx + dx, by + dy), (bx - dx, by - dy)]
            for arr in arounds:
                if arr != a and arr != b:
                    nx, ny = arr
                    if 0 <= nx < len(board[0]) and 0 <= ny < len(board):
                        antinodes.add(arr)
    print(antinodes)
    return len(antinodes)

if __name__ == "__main__":
    SAMPLE, REAL = get_raw_inputs(sys.argv)

    sample = solve(SAMPLE)
    assert sample == SAMPLE_EXPECTED, "Sample Result %s != %s expected" % (sample, SAMPLE_EXPECTED)
    print("\n*** SAMPLE PASSED ***\n")

    solved = solve(REAL)
    print("SOLUTION: ", solved)
