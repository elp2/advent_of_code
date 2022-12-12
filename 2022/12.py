from collections import defaultdict, deque, Counter
from dataclasses import dataclass
from itertools import combinations, combinations_with_replacement, permutations
from functools import reduce
import math
# import numpy as np
from operator import add, mul, itemgetter, attrgetter
import re
from typing import List

DS = [[-1, 0], [1, 0], [0, 1], [0, -1]]
DS8 = DS + [[-1, -1], [1, -1], [-1, 1], [1, 1]]
def arounds_inside(x, y, diagonals, w, h):
    ret = []
    for dx, dy in DS8 if diagonals else DS:
        ret.append((x + dx, y + dy))


CHALLENGE_DAY = "12"
REAL = open(CHALLENGE_DAY + ".txt").read()

SAMPLE_EXPECTED = 31
if SAMPLE_EXPECTED:
    SAMPLE = open(CHALLENGE_DAY + ".s.txt").read()

def parse_lines(raw):
    ret = []
    start = (0, 0)
    dest = (0, 0)
    y = 0

    for l in raw.split("\n"):
        row  = []
        x = 0
        for c in l.strip():
            if c == "S":
                start = (x, y)
                row.append(ord("a"))
            elif c == "E":
                dest = (x, y)
                row.append(ord("z"))
            else:
                row.append(ord(c))
            x += 1
        y += 1
        ret.append(row)

    return ret, start, dest


def solve(raw):
    board, start, dest = parse_lines(raw)
    bests = {}

    def valid(x, y):
        return 0 <= x < len(board[0]) and 0 <= y < len(board)

    q = deque([(start, 0)])
    while len(q):
        (x, y), steps = q.popleft()
        if (x, y) in bests and bests[(x, y)] <= steps:
            continue
        else:
            bests[(x, y)] = steps
        for dx, dy in DS:
            nx = x + dx
            ny = y + dy
            if valid(nx, ny) and board[y][x] + 1 >= board[ny][nx]:
                q.append(((nx, ny), steps + 1))
    
    return bests[dest]

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
