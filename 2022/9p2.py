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

SAMPLE_EXPECTED = 36
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

def solve(raw, ropelen):
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

    rope = []
    for _ in range(ropelen):
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

        print(l, "-----")

        for n in range(num):
            print(n, l, rope)
            hx, hy = rope[0]
            rope[0] = (hx + dx, hy + dy)

            for ri in range(len(rope) - 1):
                hx, hy = rope[ri]
                tx, ty = rope[ri + 1]

                tnx = tx
                tny = ty
                
                if abs(tx - hx) <= 1 and abs(ty - hy) <= 1:
                    break
                elif tx == hx and abs(ty - hy) > 1:
                    tny = int((hy + ty) / 2)
                elif ty == hy and abs(tx - hx) > 1:
                    tnx = int((hx + tx) / 2)
                else:
                    tdx = hx - tx
                    tdy = hy - ty
                    if abs(tdx) == 2:
                        tnx = int((hx + tx) / 2)
                    elif abs(tdx) == 1:
                        tnx = hx

                    if abs(tdy) == 2:
                        tny = int((hy + ty) / 2)
                    elif abs(tdy) == 1:
                        tny = hy

                rope[ri] = (hx, hy)
                rope[ri + 1] = (tnx, tny)
            tail_visited.add(rope[-1])

            for ri in range(len(rope) - 1):
                a = rope[ri]
                b = rope[ri + 1]
                assert abs(a[0] - b[0]) <= 1
                assert abs(a[1] - b[1]) <= 1
        print("AFTER: ", rope)
      
    # How many positions does the tail of the rope visit at least once?
    # print(tail_visited)
    return len(tail_visited)

s2 = solve(SAMPLE, 2)
print(s2)
assert s2 == 13

sp2 = solve(SAMPLE, 10)
print(sp2, 1)
assert sp2 == 1


SAMPLE2 = open(CHALLENGE_DAY + ".s2.txt").read()
# L 8
# D 3
# R 17
# D 10
# L 25
# U 20
#SAMPLE2 = "".join(SAMPLE2[:2])
sp2 = solve(SAMPLE2, 10)
print(sp2, 36)
assert sp2 == 36


solved = solve(REAL, 10)
print("SOLUTION: ", solved)
