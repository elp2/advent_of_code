from collections import defaultdict

def return_default():
    return 0

REAL=open("18.txt").readlines()
SAMPLE=open("18.sample").readlines()

OPEN="."
TREE="|"
LUMBERYARD="#"

import copy

def safe_grid_get(grid, x, y, missing=None):
    if x < 0 or y < 0:
        return missing
    if y >= len(grid):
        return missing
    if x >= len(grid[y]):
        return missing
    return grid[y][x]


def parse_lines(lines):
    return list(map(lambda l: list(l.strip()), lines))


def next_sq(grid, x, y):
    around = defaultdict(return_default)
    for dy in [-1, 0, 1]:
        for dx in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            a = safe_grid_get(grid, x + dx, y + dy)
            if a is not None:
                around[a] += 1
    here = grid[y][x]
    if here == OPEN:
        if around[TREE] >= 3:
            return TREE
        else:
            return OPEN
    elif here == TREE:
        if around[LUMBERYARD] >= 3:
            return LUMBERYARD
        else:
            return TREE
    else:
        assert here == LUMBERYARD
        if around[LUMBERYARD] >= 1 and around[TREE] >= 1:
            return LUMBERYARD
        else:
            return OPEN


def solve(lines, minutes):
    old_board = parse_lines(lines)

    for minute in range(minutes):
        board = copy.deepcopy(old_board)
        for y in range(len(board)):
            for x in range(len(board[0])):
                board[y][x] = next_sq(old_board, x, y)
        old_board = board

    lands = defaultdict(return_default)
    for y in range(len(board)):
        for x in range(len(board[0])):
            lands[board[y][x]] += 1
    return lands[TREE] * lands[LUMBERYARD]

sample = solve(SAMPLE, 10)
assert sample == 1147
print("*** SAMPLE PASSED ***")

print(solve(REAL, 10))
