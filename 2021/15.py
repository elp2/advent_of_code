from collections import defaultdict, deque, Counter
from itertools import combinations, combinations_with_replacement, permutations
import math
# import numpy as np
from operator import add, mul, itemgetter, attrgetter
import re
from typing import DefaultDict

DS = [[-1, 0], [1, 0], [0, 1], [0, -1]]
DS8 = DS + [[-1, -1], [1, -1], [-1, 1], [1, 1]]
def arounds_inside(x, y, diagonals, w, h):
    ret = []
    for dx, dy in DS8 if diagonals else DS:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < w and 0 <= ny < h:
            ret.append((nx, ny))
    return ret


CHALLENGE_DAY = "15"
REAL = open(CHALLENGE_DAY + ".txt").read()

SAMPLE_EXPECTED = 315
if SAMPLE_EXPECTED:
    SAMPLE = open(CHALLENGE_DAY + ".s.txt").read()


def parse_lines(raw):
    # Groups.
    # groups = raw.split("\n\n")
    # return list(map(lambda group: group.split("\n"), groups))
    return [[int(x) for x in line] for line in raw.split("\n")]

def solve(raw):
    parsed = parse_lines(raw)
    # parsed = [[8]]
    w = len(parsed[0])
    h = len(parsed)

    def risk_at(x, y):
        assert x <= 5 * w
        assert y <= 5 * h
        bx = x % w
        by = y % h
        base = parsed[bx][by]
        adj = base + (x - bx) // w + (y - by) // h
        if adj <= 9:
            return adj
        else:
            return adj - 9
    # Debug here to make sure parsing is good.
    ret = 0

    bests = DefaultDict(lambda: (1000000, []))

    visit = {(0, 0): (0, [])}

    dest = (w, h)

    visited = 0
    while len(visit) != 0:
        nvisit = DefaultDict(lambda: (1000000, []))
        for (x, y), (cost, path) in visit.items():
            if x < 0 or y < 0 or y >= 5 * h or x >= 5 * w:
                continue
            if bests[(x, y)][0] < cost:
                continue
            bests[(x, y)] = (cost, path)

            visited += 1
            if visited % 1000 == 0:
                print(x, y, cost, visited)

            for ax, ay in arounds_inside(x, y, False, 5 * w, 5 * h):
                exit_cost = cost + risk_at(x, y)
                if nvisit[(ax, ay)][0] > exit_cost:
                    new_path = path + [(ax, ay)]
                    nvisit[(ax, ay)] = (exit_cost, new_path)
        visit = nvisit

    ret = bests[(5 * w - 1, 5 * h - 1)]
    print(ret)
    check = 0
    for (x, y) in ret[1]:
        check += risk_at(x, y)
    for i in range(1, len(ret[1])):
        px, py = ret[1][i - 1]
        cx, cy = ret[1][i]
        assert abs(px - cx) + abs(py - cy) == 1

    # assert check == ret[0] # 487 for p1
    return check # ret[0]

if SAMPLE_EXPECTED != None:
    sample = solve(SAMPLE)
    if sample != SAMPLE_EXPECTED:
        print("SAMPLE FAILED: ", sample, " != ", SAMPLE_EXPECTED)
    assert sample == SAMPLE_EXPECTED
    print("\n*** SAMPLE PASSED ***\n")
else:
    print("Skipping sample")

solved = solve(REAL) # 488 too high
print("SOLUTION: ", solved)
import pandas as pd
df=pd.DataFrame([str(solved)])
df.to_clipboard(index=False,header=False)
print("COPIED TO CLIPBOARD")
