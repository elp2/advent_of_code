from collections import defaultdict

def return_default():
    return 0

def dd():
    return defaultdict(return_default)


CHALLENGE_DAY = "11"
REAL = open(CHALLENGE_DAY + ".txt").read()
SAMPLE = open(CHALLENGE_DAY + ".sample.txt").read()
SAMPLE_EXPECTED = 26
# SAMPLE_EXPECTED = 

FLOOR = "."
EMPTY = "L"
OCCUPIED = "#"

def parse_lines(raw):
    # Groups.
    # split = raw.split("\n\n")
    # return list(map(lambda group: group.split("\n"), split))

    split = raw.split("\n")

    # return split # raw
    # return list(map(lambda l: l.split(" "), split)) # words.
    # return list(map(int, split))
    return list(map(lambda l: list(l.strip()), split)) # beware leading / trailing WS

import copy
def run_round(old_board):
    b = copy.deepcopy(old_board)
    changed = 0
    for y in range(len(b)):
        for x in range(len(b[y])):
            here = old_board[y][x]
            if here == FLOOR:
                continue
            occ_adj = 0
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    if dx == dy and dx == 0:
                        continue
                    nx = x
                    ny = y
                    while True:
                        nx += dx
                        ny += dy
                        if 0 <= ny < len(b) and 0 <= nx < len(b[ny]):
                            if nx == x and ny == y:
                                break
                            if old_board[ny][nx] == OCCUPIED:
                                occ_adj += 1
                                break
                            elif old_board[ny][nx] == EMPTY:
                                break
                        else:
                            break
            # print(occ_adj)
            nv = here
            if here == EMPTY:
                if occ_adj == 0:
                    changed += 1
                    nv = OCCUPIED
            elif here == OCCUPIED:
                if occ_adj >= 5:
                    changed += 1
                    nv = EMPTY
            b[y][x] = nv
    print("\n".join(map(lambda l: "".join(l), b)))
    print("\n")
    return (b, changed)    

def solve(raw):
    board = parse_lines(raw)
    # Debug here to make sure parsing is good.
    ret = 0
    while True:
        board, changed = run_round(board)
        if not changed:
            num_occ = 0
            for y in range(len(board)):
                for x in range(len(board[y])):
                    if board[y][x] == OCCUPIED:
                        num_occ += 1
            return num_occ
    assert False
    return ret

def test_parsing(lines):
    if isinstance(lines, list):
        for i in range(min(5, len(lines))):
            print(lines[i])
    elif isinstance(lines, dict) or isinstance(lines, defaultdict):
        nd = {}
        for k in list(lines.keys())[0: 5]:
            print("\"" + k + "\": " + str(lines[k]))
test_parsing(parse_lines(SAMPLE))
print("^^^^^^^^^PARSED SAMPLE SAMPLE^^^^^^^^^")

sample = solve(SAMPLE)
if SAMPLE_EXPECTED is None:
    print("*** SKIPPING SAMPLE! ***")
else:
    assert sample == SAMPLE_EXPECTED
    print("*** SAMPLE PASSED ***")

solved = solve(REAL)
print("SOLUTION: ", solved)
import pandas as pd
df=pd.DataFrame([str(solved)])
df.to_clipboard(index=False,header=False)
print("COPIED TO CLIPBOARD")
# assert solved
