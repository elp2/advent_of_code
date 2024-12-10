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
SAMPLE_EXPECTED = 81
######################
assert SAMPLE_EXPECTED != None, "Must enter sample value"

def parse_group(group):
    lines = group.split("\n")
    ret = []
    zeroes = deque()
    
    for y, line in enumerate(lines):
        line = line.strip()
        assert len(line) != 0

        split = list(map(int, list(line)))
        for x, xc in enumerate(split):
            if xc == 0:
                zeroes.append((x, y))

        assert len(split) != 0
        ret.append(split)

    return ret, zeroes


def parse_lines(raw):
    # Groups.
    # groups = raw.split("\n\n")
    # Do something with the groups.

    return parse_group(raw)


def solve(raw):
    board, zeroes = parse_lines(raw)
    print(board, zeroes)

    ret = 0

    def at(x, y, board):
        w, h = len(board[0]), len(board)
        if 0 <= x < w and 0 <= y < h:
            return board[y][x]
        return None

    while len(zeroes) > 0:
        sx, sy = zeroes.popleft()
        q = deque([(sx, sy)])
        for t in range(1, 10):
            tnext = deque()
            while len(q) > 0:
                x, y = q.popleft()
                for (ax, ay) in arounds(x, y, False):
                    if at(ax, ay, board) == t:
                        tnext.append((ax, ay))
            q = tnext
        print("from ", sx, sy, len(q))
        ret += len(q)

    return ret

if __name__ == "__main__":
    SAMPLE, REAL = get_raw_inputs(sys.argv)

    sample = solve(SAMPLE)
    assert sample == SAMPLE_EXPECTED, "Sample Result %s != %s expected" % (sample, SAMPLE_EXPECTED)
    print("\n*** SAMPLE PASSED ***\n")

    solved = solve(REAL)
    print("SOLUTION: ", solved)
