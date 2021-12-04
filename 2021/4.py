from collections import defaultdict, deque, Counter
from itertools import combinations, combinations_with_replacement, permutations
import math
# import numpy as np
from operator import add, mul, itemgetter, attrgetter
import re

CHALLENGE_DAY = "4"
REAL = open(CHALLENGE_DAY + ".txt").read()
SAMPLE_EXPECTED = 4512
if SAMPLE_EXPECTED:
    SAMPLE = open(CHALLENGE_DAY + ".s.txt").read()
# SAMPLE_EXPECTED = 


def parse_lines(raw):
    lines = raw.split("\n")
    picks = lines[0]
    boards = []
    i = 1
    while i < len(lines):
        line = lines[i]
        assert len(lines[i]) == 0
        board = []
        for j in range(1, 6):
            line = lines[i + j]
            sf = filter(len, line.split(" "))
            board.append(list(map(lambda bs: int(bs), sf)))
        i += j + 1
        boards.append(board)
    return picks, boards        

def solve_score(board):
    solved = False
    for row in board:
        if row == [None, None, None, None, None]:
            solved = True
    for x in range(len(board[0])):
        col = []
        for y in range(len(board[0])):
            col.append(board[y][x])
        if col == [None, None, None, None, None]:
            solved = True
    # diags = [[(0,0), (1,1), (2, 2), (3, 3), (4, 4)], [(4,0), (3,1), (2,2), (1, 3), (0, 4)]]
    # for dia in diags:
    #     d = []
    #     for x, y in dia:
    #         d.append(board[y][x])
    #     if d == [None, None, None, None, None]:
    #         solved = True

    if not solved:
        return False
    
    ret = 0
    for row in board:
        for sq in row:
            if sq != None:
                ret += sq

    return ret

def solve(raw):
    picks, boards = parse_lines(raw)
    # Debug here to make sure parsing is good.
    ret = 0
    for p in picks.split(","):
        p = int(p)
        print(p)
        for b in boards:
            for row in b:
                for x in range(len(row)):
                    if row[x] == p:
                        row[x] = None
            ss = solve_score(b)
            if ss != False:
                return ss * p

    assert False

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
