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


CHALLENGE_DAY = "10" #PZBGZEJB
REAL = open(CHALLENGE_DAY + ".txt").read()

SAMPLE_EXPECTED = 13140
if SAMPLE_EXPECTED:
    SAMPLE = open(CHALLENGE_DAY + ".s.txt").read()


# addx V takes two cycles to complete. After two cycles, the X register is increased by the value V. (V can be negative.)
# noop takes one cycle to complete. It has no other effect.

def parse_lines(raw):
    # Groups.
    # groups = raw.split("\n\n")
    # return list(map(lambda group: group.split("\n"), groups))
    lines = raw.split("\n")
    return lines # raw
    # return list(map(lambda l: l.split(" "), lines)) # words.
    # return list(map(int, lines))
    # return list(map(lambda l: l.strip(), lines)) # beware leading / trailing WS

CYCLES = [ 20, 60, 100, 140, 180, 220 ]

def solve(raw):
    parsed = parse_lines(raw)
    # Debug here to make sure parsing is good.
    ret = []

    x = 1
    cycle = 0
    screen = ""
    def screen_char(x, cycle):
        ret = ""
        if abs(x - cycle % 40) <= 1:
            ret = "#"
        else:
            ret = " "
            print(x)
        if cycle > 0 and cycle % 40 == 0:
            ret += "\n"
        return ret

    for l in parsed:
        if l == "noop":
            screen += screen_char(x, cycle)
            cycle += 1
        else:
            op, num = l.split(" ")
            num = int(num)
            assert op == "addx"
            screen += screen_char(x, cycle)
            cycle += 1
            screen += screen_char(x, cycle)
            cycle += 1
            x += num
    print(screen)
    return None

solve(SAMPLE)
solved = solve(REAL)
print("SOLUTION: ", solved) # not 1870
