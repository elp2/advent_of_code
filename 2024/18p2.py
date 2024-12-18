from collections import defaultdict, deque, Counter
from itertools import combinations, combinations_with_replacement, permutations, product
from functools import reduce, cmp_to_key
from operator import add, mul, itemgetter, attrgetter
import os
from re import findall
from parse import parse
import sys

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, root_dir)
from aoc_elp import *

######################
SAMPLE_EXPECTED = "6,1"
######################
assert SAMPLE_EXPECTED != None, "Must enter sample value"

def parse_group(group, dims, pixels):
    print(pixels)
    b = ["".join(["." for x in range(dims)]) for y in range(dims)]
    b = "\n".join(b)
    board = Board(b)
    lines = group.split("\n")
    for i, l in enumerate(lines):
        if i < pixels:
            x, y = map(int, findall(r'\d+', l))
            board[Pos(x, y)] = "#"
    return board


def parse_lines(raw, dims, pixels):
    # Groups.
    # groups = raw.split("\n\n")
    # Do something with the groups.

    return parse_group(raw, dims, pixels)


def solve(raw, dims, pixels_start):
    lines = raw.split("\n")
    pixels = pixels_start

    while True:
        sap = solveint(raw, dims, pixels)
        if sap == 0:
            print(pixels, lines[pixels -1])
            return lines[pixels - 1]
        print(pixels)
        pixels += 1
    


def solveint(raw, dims, pixels):
    board = parse_lines(raw, dims, pixels)

    start = Pos(0, 0)
    end = Pos(dims - 1, dims - 1)
    q = deque()
    q.append((start, 0))
    best_to = defaultdict(lambda: float('inf'))
    while q:
        p, dist = q.popleft()
        if p == end:
            return dist
        if best_to[p] <= dist:
            continue
        best_to[p] = dist
        for v in [Vel(1, 0), Vel(0, 1), Vel(0, -1), Vel(-1, 0)]:
            next = p.add(v)
            if board.valid(next.x, next.y) and board[next] != "#":
                q.append((next, dist + 1))

    ret = 0

    return ret

if __name__ == "__main__":
    SAMPLE, REAL = get_raw_inputs(sys.argv)

    sample = solve(SAMPLE, 7, 12)
    assert sample == SAMPLE_EXPECTED, "Sample Result %s != %s expected" % (sample, SAMPLE_EXPECTED)
    print("\n*** SAMPLE PASSED ***\n")

    solved = solve(REAL, 71, 1024)
    print("SOLUTION: ", solved)
