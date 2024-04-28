from collections import defaultdict, deque, Counter
from itertools import combinations, combinations_with_replacement, permutations
from functools import reduce, cmp_to_key
import math
# import numpy as np
from operator import add, mul, itemgetter, attrgetter
import os
import re
from sys import argv
import sympy


def flatten(t):
    return [item for sublist in t for item in sublist]

# Sorts with cmp. cmp < 0 for a < b, == 0 for a==b, > 0 for a > b.
def elpsort(array, cmp):
    return sorted(array, key=cmp_to_key(cmp))

ON_TEXT = '\u2588'
OFF_TEXT = '\u2592'

LEFT = 0
UP = 1
RIGHT = 2
DOWN = 3
CHAR_TO_DS = {"^": UP, ">": RIGHT, "<": LEFT, "v": DOWN}
DS = [(-1, 0), (0, -1), (1, 0), (0, 1)]
DS8 = DS + [(-1, -1), (1, -1), (-1, 1), (1, 1)]

def arounds(x, y, diagonals):
    ret = []
    for dx, dy in DS8 if diagonals else DS:
        ret.append((x + dx, y + dy))
    return ret

CHALLENGE_DAY = argv[0].split("/")[-1].replace(".py", "").replace("p2.py", "")
AOC_DIR = os.path.dirname(argv[0])

print("Day: ", CHALLENGE_DAY)


try:
    REAL = open(os.path.join(AOC_DIR, CHALLENGE_DAY + ".txt")).read()
except:
    print("Did you create the solutions file?")


def parse_lines(raw):
    lines = raw.split("\n")
    for y in range(len(lines)):
        if "S" in lines[y]:
            return (lines[y].index("S"), y, lines)
    return None

def print_garden(odds, evens, minx, miny, maxx, maxy, garden):
    w = len(garden[0])
    h = len(garden)
    def gat(x, y):
        x = x % w
        y = y % h
        return garden[y][x]

    for y in range(miny, maxy + 1):
        line = []
        for x in range(minx, maxx + 1):
            if (x, y) in odds or (x, y) in evens:
                assert gat(x, y) in "S."
                line.append(".")
            else:
                g = gat(x, y)
                if g == ".":
                    line.append(" ")
                else:
                    line.append(g)

        print("".join(line))

def slow_recurse(sx, sy, garden):
    q = deque()
    minx, miny = 100, 100
    maxx, maxy = 0, 0
    
    w = len(garden[0])
    h = len(garden)
    def gat(x, y):
        x = x % w
        y = y % h
        if not 0 <= x < w or not 0 <= y < h or garden[y][x] == "#":
            return None
        return garden[y][x]

    odds = {}
    evens = {}
    q.append((sx, sy, 0))

    equations = []
    a, b, c = sympy.symbols("a, b, c")

    steps_seen = set()
    while len(q) > 0:
        x, y, steps = q.popleft()
        if steps > 1000:
            return
        if steps not in steps_seen:
            truestep = steps - 1

            def print_mod65():
                if truestep % 131 != 65:
                    return
                odd = truestep % 2 == 1
                mingx = minx // 131
                mingy = miny // 131
                maxgx = maxx // 131
                maxgy = maxy // 131
                totalcount = 0
                for gy in range(mingy - 1, maxgy + 2):
                    row = []
                    for gx in range(mingx - 1, maxgx + 2):
                        gridcount = 0
                        for wy in range(131 * gy, 131 * (gy + 1)):
                            for wx in range(131 * gx, 131 * (gx + 1)):
                                if odd:
                                    gridcount += 1 if (wx, wy) in odds else 0
                                else:
                                    gridcount += 1 if (wx, wy) in evens else 0
                        row.append("%5d" % gridcount)
                        totalcount += gridcount
                    print(" ".join(row))
                checkcount = len(odds)if odd else len(evens)
                assert checkcount == totalcount

                print("-----^^^", totalcount, truestep // 131, odd)

                                

            if truestep % 2 == 0:
                vishere = len(evens)
            else:
                vishere = len(odds)
            print_mod65()


            steps_seen.add(steps)
            # print_garden(odds, evens, minx, miny, maxx, maxy, garden)

        if steps % 2 == 0:
            if (x, y) in evens:
                continue
            else:
                evens[(x, y)] = steps
                if (x, y) in odds:
                    print("SHARED!", x, y)
                    return
        if steps % 2 == 1:
            if (x, y) in odds:
                continue
            else:
                odds[(x, y)] = steps
                if (x, y) in evens:
                    print("SHARED!", x, y)
                    return

        minx = min(x, minx)
        miny = min(y, miny)
        maxx = max(x, maxx)
        maxy = max(y, maxy)


        for ax, ay in arounds(x, y, False):
            if gat(ax, ay) != None:
                q.append((ax, ay, steps + 1))




def solve(raw):
    x, y, garden = parse_lines(raw)
    w = len(garden[0])
    h = len(garden)

    slow_recurse(x, y, garden)

    ret = 0

    return ret




solved = solve(REAL)
print("SOLUTION: ", solved)