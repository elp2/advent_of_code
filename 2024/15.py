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
SAMPLE_EXPECTED = 10092
######################
assert SAMPLE_EXPECTED != None, "Must enter sample value"

def parse_group(group):
    lines = group.split("\n")
    boxes = {}
    robot = None
    ret = []
    for y, line in enumerate(lines):
        line = line.strip()
        assert len(line) != 0

        split = list(line)

        for x, xc in enumerate(split):
            if xc == "@":
                robot = (x, y)
                split[x] = "."
        ret.append(split)

    return robot, ret, len(lines[0]), len(lines)


def parse_lines(raw):
    tank, moves = raw.split("\n\n")
    robot, board, w, h = parse_group(tank)

    mret = ""
    for m in moves:
        mret += m.strip()

    return robot, board, w, h, mret

def solve(raw):
    robot, board, w, h, mret = parse_lines(raw)
    print(robot, board, mret, w, h)

    def onboard(x, y, w=w, h=h):
        return 0 <= nx < w and 0 <= ny < h
    
    x, y = robot
    for m in mret:
        dx, dy = CHAR_TO_DS[m]
        nx, ny = dx + x, dy + y
        n = board[ny][nx]
        if n == "#":
            continue # would go out of bounds or hit edge.
        elif n == ".":
            x, y = nx, ny
        else:
            assert n == "O"
            bx, by = nx, ny
            tomoves = []
            while board[by][bx] == "O":
                tomoves.append((bx, by))
                bx, by = bx + dx, by + dy
            if board[by][bx] == ".":
                # we ended up in empty space, valid.
                for mx, my in tomoves:
                    board[my][mx] = "."
                for mx, my in tomoves:
                    nmx, nmy = mx + dx, my + dy
                    board[nmy][nmx] = "O"
                x, y = nx, ny
            else:
                pass

    ret = 0
    for y, row in enumerate(board):
        for x, xc in enumerate(row):
            if xc == "O":
                ret += 100 * y + x

    return ret

if __name__ == "__main__":
    SAMPLE, REAL = get_raw_inputs(sys.argv)

    sample = solve(SAMPLE)
    assert sample == SAMPLE_EXPECTED, "Sample Result %s != %s expected" % (sample, SAMPLE_EXPECTED)
    print("\n*** SAMPLE PASSED ***\n")

    solved = solve(REAL)
    print("SOLUTION: ", solved)
