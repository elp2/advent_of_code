from collections import defaultdict, deque, Counter
from itertools import combinations, combinations_with_replacement, permutations
from functools import reduce
import math
# import numpy as np
from operator import add, mul, itemgetter, attrgetter
import re

DS = [[-1, 0], [1, 0], [0, 1], [0, -1]]
DS8 = DS + [[-1, -1], [1, -1], [-1, 1], [1, 1]]
def arounds_inside(x, y, diagonals, w, h):
    ret = []
    for dx, dy in DS8 if diagonals else DS:
        ret.append((x + dx, y + dy))


CHALLENGE_DAY = "9"
REAL = open(CHALLENGE_DAY + ".txt").read()

SAMPLE_EXPECTED = 13
if SAMPLE_EXPECTED:
    SAMPLE = open(CHALLENGE_DAY + ".s.txt").read()


def parse_lines(raw):
    # Groups.
    # groups = raw.split("\n\n")
    # return list(map(lambda group: group.split("\n"), groups))
    lines = raw.split("\n")
    return lines # raw
    # return list(map(lambda l: l.split(" "), lines)) # words.
    # return list(map(int, lines))
    # return list(map(lambda l: l.strip(), lines)) # beware leading / trailing WS

def solve(raw):
    parsed = parse_lines(raw)
    # Debug here to make sure parsing is good.
    ret = 0
    # HT Start overlapping
    tail_visited = set()
    tail_visited.add((0, 0))

    hx = 0
    hy = 0
    tx = 0
    ty = 0

    ROPE_LEN = 2
    rope = []
    for _ in range(ROPE_LEN):
        rope.append((0, 0))
    for l in parsed:
        d, num = l.split(" ")
        num = int(num)
        dx = 0
        dy = 0
        if d == "R":
            dx = 1
        elif d == "L":
            dx = -1
        elif d == "D":
            dy = -1
        elif d == "U":
            dy = 1



        for n in range(num):
            hx, hy = rope[0]
            rope[0] = (hx + dx, hy + dy)

            for ri in range(len(rope) - 1):
                hx, hy = rope[ri]
                tx, ty = rope[ri + 1]

            thx = abs(hx - tx)
            thy = abs(hy - ty)
            if thx > 1 or thy > 1:
                tx = hx - dx
                ty = hy - dy
            rope[ri] = (hx, hy)
            rope[ri + 1] = (tx, ty)            
            if ri == len(rope) - 2:
                tail_visited.add((tx, ty))

    # How many positions does the tail of the rope visit at least once?
    # print(tail_visited)
    return len(tail_visited)

if SAMPLE_EXPECTED != None:
    sample = solve(SAMPLE)
    if sample != SAMPLE_EXPECTED:
        print("SAMPLE FAILED: ", sample, " != ", SAMPLE_EXPECTED)
    assert sample == SAMPLE_EXPECTED
    print("\n*** SAMPLE PASSED ***\n")
else:
    print("Skipping sample")

solved = solve(REAL)
print("SOLUTION: ", solved) # not 1870
