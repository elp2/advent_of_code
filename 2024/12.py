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
SAMPLE_EXPECTED = 140
######################
assert SAMPLE_EXPECTED != None, "Must enter sample value"

def parse_group(group):
    lines = group.split("\n")
    ret = []
    for y, line in enumerate(lines):
        line = line.strip()
        assert len(line) != 0

        split = list(line)

        for x, xc in enumerate(split):
            pass

        assert len(split) != 0
        ret.append(split)

    return ret


def parse_lines(raw):
    # Groups.
    # groups = raw.split("\n\n")
    # Do something with the groups.

    return parse_group(raw)

def next_unseen(seen, board):
    target = None
    for y in range(len(board)):
        for x in range(len(board[y])):
            if (x, y) in seen:
                continue
            target = board[y][x]
            sx, sy = x, y
            return target, x, y
    return None, -1, -1

def get_region(seen, board):
    target, x, y = next_unseen(seen, board)
    if target == None:
        return set(), None

    region = set()
    q = deque([(x, y)])
    region.add((x, y))

    while len(q) > 0:
        x, y = q.popleft()
        for ax, ay in arounds(x, y, False):
            if not 0 <= ax < len(board[0]) or not 0 <= ay < len(board):
                continue
            if board[ay][ax] != target:
                continue
            if (ax, ay) in seen or (ax, ay) in region:
                continue
            region.add((ax, ay))
            q.append((ax, ay))
    return region, target
    

def get_perimeter(region, board):
    perimiter = set()
    for (x, y) in region:
        for ax, ay in arounds(x, y, False):
            # if not 0 <= ax < len(board[0]) or not 0 <= ay < len(board):
            #     continue
            if (ax, ay) not in region:
                perimiter.add((ax, ay, (x, y)))
    return perimiter


def print_perim(perim, board):
    for (px, py) in perim:
        board[py][px] = ON_CHAR
    for l in board:
        print("".join(l))

def solve(raw):
    parsed = parse_lines(raw)
    print(parsed)

    seen = set()
    ret = 0
    while True:
        region, target = get_region(seen, parsed)
        if target == None:
            return ret
        perim = get_perimeter(region, parsed)
        cost = len(region) * len(perim)
        print(perim)
        print(target, len(region), len(perim), "=", cost)
        ret += cost
        for (x, y) in region:
            seen.add((x, y))

if __name__ == "__main__":
    SAMPLE, REAL = get_raw_inputs(sys.argv)

    sample = solve(SAMPLE)
    assert sample == SAMPLE_EXPECTED, "Sample Result %s != %s expected" % (sample, SAMPLE_EXPECTED)
    print("\n*** SAMPLE PASSED ***\n")

    solved = solve(REAL)
    print("SOLUTION: ", solved)
