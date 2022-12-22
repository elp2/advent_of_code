from collections import defaultdict, deque, Counter
from itertools import combinations, combinations_with_replacement, permutations
from functools import reduce
import math
# import numpy as np
from operator import add, mul, itemgetter, attrgetter
import re

DS = [[0, -1], [1, 0], [0, 1], [-1, 0]]
DIRCHAR=["^", ">", "v", "<"]

CHALLENGE_DAY = "22"
REAL = open(CHALLENGE_DAY + ".txt").read()

SAMPLE_EXPECTED = 6032
if SAMPLE_EXPECTED:
    SAMPLE = open(CHALLENGE_DAY + ".s.txt").read()

VOID = " "
SPACE = "."
WALL = "#"
def parse_lines(raw):
    # Groups.
    ms, instructions = raw.split("\n\n")
    
    ms = ms.split("\n")
    start = None

    W = max(map(len, ms))
    H = len(ms)

    m = [["" for _ in range(W)] for _ in range(H)]
    for y in range(H):
        for x in range(W):
            if x >= len(ms[y]) or ms[y][x] == VOID:
                m[y][x] = VOID
            else:
                m[y][x] = ms[y][x]
                if start == None:
                    start = (x, y)

    ins = []
    here = ""
    for c in instructions:
        if c in ["R", "L"]:
            ins.append((int(here), c))
            here = ""
        else:
            here += c
    if here != "":
        ins.append((int(here), ""))
    
    return W, H, m, start, ins

def solve(raw):
    W, H, m, start, ins = parse_lines(raw)
    print(ins)
    # Debug here to make sure parsing is good.

    x, y = start

    di = 1

    def print_map(m):
        print("-------------------")
        for l in m:
            print("".join(l))
        print("-------------------")

    def advance(dx, dy, x, y, spaces):
        print("Advancing: ", x, y, " dx/dy", dx, dy, "s=", spaces)
        for _ in range(spaces):
            nx, ny = x, y
            while True:
                nx, ny = (nx + dx + W) % W, (ny + dy + H) % H
                if m[ny][nx] != VOID:
                    break
            if m[ny][nx] == WALL:
                return x, y
            else:
                x, y = nx, ny
                assert m[y][x] in [".", ">", "<", "^", "v"]
                m[y][x] = DIRCHAR[di]
        return x, y

    # print_map(m)
    print(start)
    for spaces, turn in ins:
        dx, dy = DS[di]
        x, y = advance(dx, dy, x, y, spaces)
        # print_map(m)
        if turn == "R":
            di = (4 + di + 1) % 4
        elif turn == "L":
            di = (4 + di - 1) % 4
        else:
            pass
        print(x, y, di)

    row = y + 1
    col = x + 1
    # Facing is 0 for right (>), 1 for down (v), 2 for left (<), and 3 for up (^). The final password is the sum of 1000 times the row, 4 times the column, and the facing.
    # DS = [[-1, 0], [1, 0], [0, 1], [0, -1]]
    # DIRCHAR=["^", ">", "v", "<"]
    fmap = {">": 0, "v": 1, "<": 2, "^": 3} 
    return row * 1000 + 4 * col + fmap[DIRCHAR[di]]

if SAMPLE_EXPECTED != None:
    sample = solve(SAMPLE)
    if sample != SAMPLE_EXPECTED:
        print("SAMPLE FAILED: ", sample, " != ", SAMPLE_EXPECTED)
    assert sample == SAMPLE_EXPECTED
    print("\n*** SAMPLE PASSED ***\n")
else:
    print("Skipping sample")

solved = solve(REAL)
assert solved > 81391
assert solved < 95382
print("SOLUTION: ", solved)