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


CHALLENGE_DAY = "5"
REAL = open(CHALLENGE_DAY + ".txt").read()

SAMPLE_EXPECTED = "MCD"
if SAMPLE_EXPECTED:
    SAMPLE = open(CHALLENGE_DAY + ".s.txt").read()


#     [D]    
# [N] [C]    
# [Z] [M] [P]
#  1   2   3 

#     [M]             [Z]     [V]    
#     [Z]     [P]     [L]     [Z] [J]
# [S] [D]     [W]     [W]     [H] [Q]
# [P] [V] [N] [D]     [P]     [C] [V]
# [H] [B] [J] [V] [B] [M]     [N] [P]
# [V] [F] [L] [Z] [C] [S] [P] [S] [G]
# [F] [J] [M] [G] [R] [R] [H] [R] [L]
# [G] [G] [G] [N] [V] [V] [T] [Q] [F]
#  1   2   3   4   5   6   7   8   9 

# move 6 from 9 to 3

def parse_lines(raw):
    # Groups.
    groups = raw.split("\n\n")
    stacks, moves = groups
    stacks = stacks.split("\n")
    ncols = int(stacks[-1].strip().split(" ")[-1])
    cols = []# [] for i in range(ncols)]
    i = 0
    x = 1
    while x < len(stacks[0]):
        c = []
        y = len(stacks) - 2
        while y >= 0:
            if stacks[y][x] != " ":
                c.append(stacks[y][x])
            y -= 1
        cols.append(c)
        i += 1
        x += 4
    
    moves = moves.split("\n")
    return cols, moves
    # return list(map(lambda group: group.split("\n"), groups))
    # lines = raw.split("\n")
    # return lines # raw
    # return list(map(lambda l: l.split(" "), lines)) # words.
    # return list(map(int, lines))
    # return list(map(lambda l: l.strip(), lines)) # beware leading / trailing WS

def solve(raw):
    cols, moves = parse_lines(raw)
    # Debug here to make sure parsing is good.
    ret = 0

    for m in moves:
        print(m)
        print(cols)
        # move 6 from 9 to 3
        _, nmove, _, f, _, to = m.strip().split(" ")
        nmove = int(nmove)
        f = int(f) - 1
        to = int(to) - 1


        stack = []
        while nmove:
            container = cols[f].pop()
            stack.append(container)
            nmove -=1
        stack.reverse()
        for s in stack:
            cols[to].append(s)
    
    ret = ""
    for c in cols:
        ret = ret + c.pop()

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
