from collections import defaultdict, deque, Counter
from itertools import combinations, combinations_with_replacement, permutations
from functools import reduce
import math
# import numpy as np
from operator import add, mul, itemgetter, attrgetter
import re

DS = [(-1, 0), (1, 0), (0, 1), (0, -1)]
DS8 = DS + [[-1, -1], [1, -1], [-1, 1], [1, 1]]
def arounds_inside(x, y, diagonals):
    ret = []
    for dx, dy in DS8 if diagonals else DS:
        ret.append((x + dx, y + dy))
    return ret


CHALLENGE_DAY = "24"
REAL = open(CHALLENGE_DAY + ".txt").read()

SAMPLE_EXPECTED = 54
if SAMPLE_EXPECTED:
    SAMPLE = open(CHALLENGE_DAY + ".s.txt").read()

B2D = {"^": 3, ">": 1, "<": 0, "v": 2}

def parse_lines(raw):
    lines = raw.split("\n")
    W = len(lines[0])
    H = len(lines)
    enter = (lines[0].index(".") - 1, -1)

    exit = (lines[-1].index(".") - 1, H - 2 - 1)
    blizzards = defaultdict(lambda: [])
    for y, row in enumerate(lines[1:-1]):
        row = row[1:-1]
        for x, c in enumerate(row):
            if c not in "#.":
                blizzards[(x, y)].append(DS[B2D[c]])

    return enter, exit, W - 2, H - 2, blizzards


def advance(W, H, blizzards):
    n = defaultdict(lambda: [])
    for (x, y), bhere in blizzards.items():
        for dx, dy in bhere:
            nx = (x + dx + W) % W
            ny = (y + dy + H) % H
            assert 0 <= nx < W
            assert 0 <= ny < H
            n[(nx, ny)].append((dx, dy))
    return n

def solve(raw):
    parsed = parse_lines(raw)
    # Debug here to make sure parsing is good.
    enter, exit, W, H, blizzards = parsed

    enterance = (enter[0], 0)

    q = deque()
    q.append((enter, 0, 0))

    all_blizzards = []
    for i in range(W * H):
        all_blizzards.append(blizzards)
        blizzards = advance(W, H, blizzards)

    visited_at = defaultdict(lambda: [])
    max_dist = 0

    seens = set()
    while len(q):
        pl = q.popleft()
        (x, y), dist, phase = pl

        k = (x, y, dist, phase)
        if k in seens:
            continue
        seens.add(k)

        if dist > max_dist:
            print(dist)
            max_dist = dist
        visited_at[(x, y)].append(dist)
        if (x, y) == exit:
            if phase == 0:
                q.append(((x, y+1), dist + 1, 1))
            elif phase == 1:
                q.append(((x, y+1), dist + 1, phase))
            elif phase == 2:
                return dist + 1 # TODO why + 1????
        elif (x, y) == enterance:
            if phase == 0:
                q.append((enter, dist + 1, phase))
            elif phase == 1:
                q.append((enter, dist + 1, 2))
            elif phase == 2:
                q.append((enter, dist + 1, phase))

        blizzards = all_blizzards[(dist + 1) % (W * H)]
        if (x, y) not in blizzards:
            # Stay
            q.append(((x, y), dist + 1, phase))

        for ax, ay in arounds_inside(x, y, False):
            if 0 <= ax < W and 0 <= ay < H:
                if (ax, ay) in blizzards:
                    continue
                q.append(((ax, ay), dist + 1, phase))

    assert False

if SAMPLE_EXPECTED != None:
    sample = solve(SAMPLE)
    if sample != SAMPLE_EXPECTED:
        print("SAMPLE FAILED: ", sample, " != ", SAMPLE_EXPECTED)
    assert sample == SAMPLE_EXPECTED
    print("\n*** SAMPLE PASSED ***\n")
else:
    print("Skipping sample")

solved = solve(REAL)

assert solved > 218
print("SOLUTION: ", solved)
