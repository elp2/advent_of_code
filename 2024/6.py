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

CHALLENGE_DAY = argv[0].split("/")[-1].replace("p2.py", "").replace(".py", "")
AOC_DIR = os.path.dirname(argv[0])

print("Day: ", CHALLENGE_DAY)

######################
SAMPLE_EXPECTED = 41
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

def solve(raw):
    (x, y, dir), board = parse_lines(raw)
    
    visited = set()
    def isin(x, y, board):
        w = len(board[0])
        h = len(board)
        return 0 <= x < w and 0 <= y < h

    def at(x, y, board):
        if not isin(x,y,board):
            return "."
        here = board[y][x]
        if here == "X" or here == ".":
            return "."
        return here



    while True:
        print(x, y, dir)
        if not isin(x, y, board):
            return len(visited)
        visited.add((x, y))
        board[y][x] = "X"

        while True:
            nx, ny = x + dir[0], y + dir[1]
            if at(nx, ny, board) == ".":
                x, y = nx, ny
                break
            else:
                dir = DS[(DS.index(dir) + 1) % 4]
                print("Turned to ", dir)
                printboard(board)

    return len(visited)

sample = solve(SAMPLE)
assert sample == SAMPLE_EXPECTED, "Sample Result %s != %s expected" % (sample, SAMPLE_EXPECTED)
print("\n*** SAMPLE PASSED ***\n")

solved = solve(REAL)
print("SOLUTION: ", solved)
