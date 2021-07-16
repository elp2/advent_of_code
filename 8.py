from collections import defaultdict, deque
from itertools import combinations, combinations_with_replacement, permutations
import math
import numpy as np
from operator import add, mul, itemgetter, attrgetter
import re
def flatten(t):
    return [item for sublist in t for item in sublist]

def part1(lines):
    WIDTH, HEIGHT = 50, 6
    board = np.zeros((HEIGHT, WIDTH), dtype=bool)

    def boardlit():
        return np.sum(board)

    for line in lines:
        print(line)
        before = boardlit()
        rectm = re.match(r"rect (\d+)x(\d+)", line)
        rowm = re.match(r"rotate row y=(\d+) by (\d+)", line)
        colm = re.match(r"rotate column x=(\d+) by (\d+)", line)
        if rectm:
            board[:int(rectm[2]), :int(rectm[1])] = True
        elif rowm:
            y, by = int(rowm[1]), int(rowm[2])
            board[y] = np.roll(board[y], by)
        elif colm:
            assert boardlit() == before
            x, by = int(colm[1]), int(colm[2])
            board[:, x] = np.roll(board[:, x], by)
            assert boardlit() == before
        else:
            assert False
    return board

print("part 1:", np.sum(part1(open("8.in").readlines())))
