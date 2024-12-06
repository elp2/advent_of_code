from collections import defaultdict, deque, Counter
from itertools import combinations, combinations_with_replacement, permutations
from functools import reduce, cmp_to_key
import math
# import numpy as np
from operator import add, mul, itemgetter, attrgetter
from parse import parse
import os
import re
from sys import argv

def flatten(t):
    return [item for sublist in t for item in sublist]

# Sorts with cmp. cmp < 0 for a < b, == 0 for a==b, > 0 for a > b.
def elpsort(array, cmp):
    return sorted(array, key=cmp_to_key(cmp))

ON_TEXT = '\u2588'
OFF_TEXT = '\u2592'

LEFT = (-1, 0)
UP = (0, -1)
RIGHT = (1, 0)
DOWN = (0, 1)
CHAR_TO_DS = {"^": UP, ">": RIGHT, "<": LEFT, "v": DOWN}
DS = [LEFT, UP, RIGHT, DOWN] # +IDX = TURN RIGHT
UPLEFT = (-1, -1)
UPRIGHT = (1, -1)
DOWNRIGHT = (1, 1)
DOWNLEFT = (-1, 1)
DS8 = [LEFT, UPLEFT, UP, UPRIGHT, RIGHT, DOWNRIGHT, DOWN, DOWNLEFT] # +IDX = TURN RIGHT

def arounds(x, y, diagonals):
    ret = []
    for dx, dy in DS8 if diagonals else DS:
        ret.append((x + dx, y + dy))
    return ret

CHALLENGE_DAY = argv[0].split("/")[-1].replace("p22.py", "").replace(".py", "")
AOC_DIR = os.path.dirname(argv[0])

print("Day: ", CHALLENGE_DAY)

######################
SAMPLE_EXPECTED = 6
######################
assert SAMPLE_EXPECTED != None

try:
    sample_file = os.path.join(AOC_DIR, CHALLENGE_DAY + ".s.txt")
    SAMPLE = open(sample_file).read()
except:
    assert None, "Missing Sample File: %s" % (sample_file)

try:
    solutions_file = os.path.join(AOC_DIR, CHALLENGE_DAY + ".txt")
    REAL = open(solutions_file).read()
except:
    assert None, "Missing Solutions File: %s" % (solutions_file)

def parse_group(group):
    lines = group.split("\n")
    ret = []
    y = 0
    for line in lines:
        line = line.strip()
        assert len(line) != 0
        split = list(line)
        for k in CHAR_TO_DS.keys():
            if k in line:
                sx = line.index(k)
                sy = y
                dir = CHAR_TO_DS[k]
        assert len(split) != 0
        ret.append(split)
        y += 1

    
    return (sx, sy, dir), ret


def parse_lines(raw):
    # Groups.
    # groups = raw.split("\n\n")
    # Do something with the groups.

    return parse_group(raw)

def printboard(board):
    for l in board:
        print("".join(l))

def solve2(raw, board):
    (startx, starty, dir), _ = parse_lines(raw)
    x, y = startx, starty
    visited = set()
    def isin(x, y, board):
        w = len(board[0])
        h = len(board)
        return 0 <= x < w and 0 <= y < h

    def at(x, y, board):
        if not isin(x,y,board):
            return "."
        here = board[y][x]
        if here == "X" or here == "." or here == "O":
            return "."
        return here


    sx, sy = x, y
    lines = {LEFT: [], UP: [], DOWN: [], RIGHT: []}

    def intersectings(x, y, l):
        # for line in l:
        (sx, sy), (ex, ey) = l
        # sx, sy = line[0]
        # ex, ey = line[1]

        if sx > ex or sy > ey:
            tx, ty = sx, sy
            sx, sy = ex, ey
            ex, ey = tx, ty

        if sx <= x <= ex and sy <= y <= ey:
            return True
        return False
            

    obstacles_at = set()

    def extend_line(line, dir, board):
        (osx, osy), (ex, ey) = line
        dir = (-1 * dir[0], -1 * dir[1])

        sx, sy = osx, osy
        while True:
            if isin(sx + dir[0], sy + dir[1], board):
                sx = sx + dir[0]
                sy = sy + dir[1]
            else:
                break
        # print((osx, osy), "->", (sx, sy))
        return ((sx, sy), (ex, ey))

    while True:
        # print(x, y, dir)
        if not isin(x, y, board):
            break

        if (x, y, dir) in visited:
            return True
        visited.add((x, y, dir))
        board[y][x] = "X"
        # printboard(board)

        turned = 0
        while True:
            # for l in lines[dir]:
            #     if intersectings(x, y, l):
            #         return True
            nx, ny = x + dir[0], y + dir[1]
            if at(nx, ny, board) == ".":
                x, y = nx, ny
                break
            else:
                if turned < 4:
                    newline = ((sx, sy), (x, y))
                    assert sx == x or sy == y
                    # print("LINE: ", newline)
                    lines[dir].append(extend_line(newline, dir, board))
                    sx, sy = x, y
                assert turned < 4

                dir = DS[(DS.index(dir) + 1) % 4]
                # print("Turned to ", dir, x, y)
                turned += 1
    
    return False
    # assert len(visited) in [41, 5404]
    # print("Visited: ", len(visited))
    # print("obs", obstacles_at)
    # return len(obstacles_at)

def solve(raw):
    (startx, starty, dir), board = parse_lines(raw)
    ret = 0
    for y in range(len(board)):
        print(y, "/", len(board))
        for x in range(len(board[y])):
            if (x, y) == (startx, starty):
                continue
            if board[y][x] == "#":
                continue
            (startx, starty, _), board = parse_lines(raw)
            board[y][x] = "#"

            if solve2(raw, board):
                print("obsat", x, y)
                ret += 1
            board[y][x] = "."
    print(ret)
    return ret



sample = solve(SAMPLE)
assert sample == SAMPLE_EXPECTED, "Sample Result %s != %s expected" % (sample, SAMPLE_EXPECTED)
print("\n*** SAMPLE PASSED ***\n")

solved = solve(REAL)
assert solved > 760 and solved < 2000
assert solved != 1695
print("SOLUTION: ", solved)
