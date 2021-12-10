from collections import defaultdict, deque, Counter
from itertools import combinations, combinations_with_replacement, permutations
import math
# import numpy as np
from operator import add, mul, itemgetter, attrgetter
import re
from typing import Deque

CHALLENGE_DAY = "9"
REAL = open(CHALLENGE_DAY + ".txt").read()

SAMPLE_EXPECTED = 1134
if SAMPLE_EXPECTED:
    SAMPLE = open(CHALLENGE_DAY + ".s.txt").read()


def parse_lines(raw):
    lines = raw.split("\n")
    ret = []
    for line in lines:
        ret.append([int(x) for x in list(line)])
    return ret

def solve(raw):
    parsed = parse_lines(raw)
    # Debug here to make sure parsing is good.

    def valid(x, y):
        inside = 0 <= x < len(parsed[0]) and 0 <= y < len(parsed)
        if not inside:
            return False
        
        return parsed[y][x] != None

    ret = 0
    lows = []
    for y in range(len(parsed)):
        for x in range(len(parsed[y])):
            here = parsed[y][x]
            ds = [[-1, 0], [1, 0], [0, 1], [0, -1]]
            around = []
            for dx, dy in ds:
                nx = x + dx
                ny = y + dy
                if valid(nx, ny):
                    around.append(parsed[ny][nx])
            
            gts = [a > here for a in around]
            if all(gts):
                lows.append((x, y))

    basins = []
    for x, y in lows:
        check = Deque()
        check.append((x, y))

        bs = 0
        while len(check) != 0:
            x, y = check.popleft()
            if parsed[y][x] == 9:
                continue

            parsed[y][x] = None

            bs += 1
            ds = [[-1, 0], [1, 0], [0, 1], [0, -1]]
            around = []
            for dx, dy in ds:
                nx = x + dx
                ny = y + dy
                if valid(nx, ny) and (nx, ny) not in check:
                    check.append((nx, ny))

        basins.append(bs)

    print(basins)
    sorty = sorted(basins)
    ret = 1
    for m in sorty[-3:]:
        ret *= m
    return ret

if SAMPLE_EXPECTED != None:
    sample = solve(SAMPLE)
    if sample != SAMPLE_EXPECTED:
        print("SAMPLE FAILED: ", sample, " != ", SAMPLE_EXPECTED)
    assert sample == SAMPLE_EXPECTED
    print("\n*** SAMPLE PASSED ***\n")
else:
    print("Skipping sample")

solved = solve(REAL)
print("SOLUTION: ", solved)
import pandas as pd
df=pd.DataFrame([str(solved)])
df.to_clipboard(index=False,header=False)
print("COPIED TO CLIPBOARD")
