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


CHALLENGE_DAY = "8"
REAL = open(CHALLENGE_DAY + ".txt").read()

SAMPLE_EXPECTED = 21
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

    seens = set()

    def at(x, y):
        return int(parsed[y][x])

    def edge(x, y):
        return x == 0 or x == len(parsed[0]) - 1 or y == 0 or y == len(parsed) - 1

    def on_board(x, y):
        return 0 <= x < len(parsed[0]) and 0 <= y < len(parsed)

    def visible(x, y):
        if x == 1 and y == 0:
            print("?")

        if (x, y) in seens:
            return True

        # if edge(x, y):
        #     seens.add((x, y))
        #     return True
        for (dx, dy) in DS:
            here = at(x, y)
            nx = x + dx
            ny = y + dy
            failed = False
            while on_board(nx, ny):
                nhere = at(nx, ny)
                if nhere >= here:
                    failed = True
                    break
            
                nx = nx + dx
                ny = ny + dy
            if not failed:
                seens.add((x, y))
                return True
        return False

    for y in range(len(parsed)):
        for x in range(len(parsed[0])):
            if visible(x, y):
                seens.add((x, y))

    print(seens)
    for y in range(len(parsed)):
        line = ""
        for x in range(len(parsed[0])):
            if (x, y) in seens:
                line += "*"
            else:
                line += " "
        print(line)
    return len(seens)

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
