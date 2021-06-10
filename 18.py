from collections import defaultdict, deque
import re

CHALLENGE_DAY = "18"
REAL = open(CHALLENGE_DAY + ".txt").read()
SAMPLE = open(CHALLENGE_DAY + ".sample.txt").read()
SAMPLE_EXPECTED = 4

def parse_lines(raw):
    # Groups.
    # groups = raw.split("\n\n")
    # return list(map(lambda group: group.split("\n"), groups))
    
    ret = set()
    lines = raw.split("\n")
    height = len(lines)
    width = len(lines[0])
    for y, l in enumerate(lines):
        for x, c in enumerate(l):
            if c == "#":
                ret.add((x, y))
    
    return ret, width, height


def around(board, x, y):
    ret = 0
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == dy and dx == 0:
                continue
            if (x + dx, y + dy) in board:
                ret += 1
    return ret

def solve(raw, steps, is_p2=False):
    board, w, h = parse_lines(raw)
    print(w, h)
    # Debug here to make sure parsing is good.
    ret = 0
    while steps:
        np = set()
        if is_p2:
            np.add((0, 0))
            np.add((0, h-1))
            np.add((w-1, 0))
            np.add((w-1, h-1))
        for x in range(w):
            for y in range(h):
                arounds = around(board, x, y)
                if (x, y) in board:
                    if arounds == 2 or arounds == 3:
                        np.add((x, y))
                else:
                    if arounds == 3:
                        np.add((x, y))
        board = np
        if is_p2:
            board.add((0, 0))
            board.add((0, h-1))
            board.add((w-1, 0))
            board.add((w-1, h-1))

        steps -= 1


    return len(board)

sample = solve(SAMPLE, 4)
if sample != SAMPLE_EXPECTED:
    print("SAMPLE FAILED: ", sample, " != ", SAMPLE_EXPECTED)
assert sample == SAMPLE_EXPECTED
print("\n*** SAMPLE PASSED ***\n")

solved = solve(REAL, 100)
print("SOLUTION: ", solved)

solved = solve(REAL, 100, True)
print("SOLUTION2: ", solved)
