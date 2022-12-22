from collections import defaultdict, deque, Counter
from itertools import combinations, combinations_with_replacement, permutations
from functools import reduce
import math
# import numpy as np
from operator import add, mul, itemgetter, attrgetter
import re

DS = [[0, -1], [1, 0], [0, 1], [-1, 0]]
DIRCHAR=["^", ">", "v", "<"]

FACING_TO_DI = {">": 0, "v": 1, "<": 2, "^": 3}
# DI_TO_FACING = {0: ">", 1: "v", 2: "<", 3: "^"}

CHALLENGE_DAY = "22"
REAL = open(CHALLENGE_DAY + ".txt").read()

SAMPLE_EXPECTED = None
if SAMPLE_EXPECTED:
    SAMPLE = open(CHALLENGE_DAY + ".s.txt").read()

VOID = " "
SPACE = "."
WALL = "#"

REAL_CUBE={
    "A": {
        "B": (">", ">"),
        "C": ("v", "v"),
        "D": ("<", ">"), # adjust for the ys being flipped
        "F": ("^", ">"),
    },
    "B": {
        "A": ("<", "<"),
        "C": ("v", "<"),
        "E": (">", "<"),
        "F": ("^", "^"),
    },
    "C": {
        "A": ("^", "^"),
        "B": (">", "^"),
        "E": ("v", "v"),
        "D": ("<", "v"),
    },
    "D": {
        "C": ("^", ">"),
        "E": (">", ">"),
        "F": ("v", "v"),
        "A": ("<", ">"),
    },
    "E": {
        "C": ("^", "^"),
        "B": (">", "<"),
        "F": ("v", "<"),
        "D": ("<", "<"),
    },
    "F": {
        "D": ("^", "^"),
        "E": (">", "^"),
        "B": ("v", "v"),
        "A": ("<", "v"),
    }
}

LTRPOS = {"^": True, "v": False, ">": True, "<": False}

SIDES = {"A": (50,0), "B": (100, 0), "C": (50, 50), "D": (0, 100), "E": (50, 100), "F": (0, 150)}

def side_for(x, y):
    for name, (sx, sy) in SIDES.items():
        if sx <= x < sx + 50 and sy <= y < sy + 50:
            return name
    return None

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

    def pass_wall(x, y, facing):
        start_side = side_for(x, y)
        cx = x % 50
        cy = y % 50

        for next_cube, (ffrom, fnew) in REAL_CUBE[start_side].items():
            if facing != ffrom:
                continue
            if ffrom == ">":
                epos = cy
            elif ffrom == "v":
                epos = cx
            elif ffrom == "<":
                epos = cy
            elif ffrom == "^":
                epos = cx

            if LTRPOS[fnew] != LTRPOS[ffrom]:
                adj = 50 - epos - 1
            else:
                adj = epos

            if fnew == ">":
                ncx = 0
                ncy = adj
            elif fnew == "^":
                ncx = adj
                ncy = 50 - 1
            elif fnew == "<":
                ncx = 50 - 1
                ncy = adj
            elif fnew == "v":
                ncx = adj
                ncy = 0

            ndi = DIRCHAR.index(fnew)

            ncx += SIDES[next_cube][0]
            ncy += SIDES[next_cube][1]

            assert side_for(ncx, ncy) == next_cube

            print("SIDES Move: ", start_side, ffrom, fnew, next_cube, (x, y), (ncx, ncy))
            return ncx, ncy, ndi

        assert False


    def advance(di, x, y, spaces):
        print("Advancing: ", x, y, " dx/dy", di, "s=", spaces)
        for _ in range(spaces):
            side = side_for(x, y)
            dx, dy = DS[di]
            assert side
            nx, ny, ndi = x, y, di
            nx, ny = (nx + dx + W) % W, (ny + dy + H) % H
            nside = side_for(nx, ny)
            if nside != side:
                nx, ny, ndi = pass_wall(x, y, DIRCHAR[di])
            if m[ny][nx] == WALL:
                return x, y, di
            else:
                x, y, di = nx, ny, ndi
                assert m[y][x] in [".", ">", "<", "^", "v"]
                m[y][x] = DIRCHAR[di]
        return x, y, di

    print_map(m)
    print(start)
    for spaces, turn in ins:
        x, y, di = advance(di, x, y, spaces)
        print_map(m)
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
    
    return row * 1000 + 4 * col + FACING_TO_DI[DIRCHAR[di]]

if SAMPLE_EXPECTED != None:
    sample = solve(SAMPLE)
    if sample != SAMPLE_EXPECTED:
        print("SAMPLE FAILED: ", sample, " != ", SAMPLE_EXPECTED)
    assert sample == SAMPLE_EXPECTED
    print("\n*** SAMPLE PASSED ***\n")
else:
    print("Skipping sample")

solved = solve(REAL)
assert solved > 9396
print("SOLUTION: ", solved)