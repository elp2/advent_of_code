from collections import defaultdict, deque, Counter
from itertools import combinations, combinations_with_replacement, permutations, product
from functools import reduce, cmp_to_key
from operator import add, mul, itemgetter, attrgetter
import os
from parse import parse
import sys

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, root_dir)
from aoc_elp import *

######################
SAMPLE_EXPECTED = 9021
######################
assert SAMPLE_EXPECTED != None, "Must enter sample value"

def expand_board(smol):
    ret = []
    for line in smol.split("\n"):
        r = ""
        for xc in line:
            # If the tile is #, the new map contains ## instead.
            # If the tile is O, the new map contains [] instead.
            # If the tile is ., the new map contains .. instead.
            # If the tile is @, the new map contains @. instead.
            if xc == "#":
                r += "##"
            elif xc == "O":
                r += "[]"
            elif xc == ".":
                r += ".."
            elif xc == "@":
                r += "@."
            else:
                assert False
        
        ret.append(r)
    return ret


def parse_group(group):
    lines = expand_board(group)
    robot = None
    ret = []
    for y, line in enumerate(lines):
        line = line.strip()
        assert len(line) != 0

        split = list(line)

        for x, xc in enumerate(split):
            if xc == "@":
                robot = (x, y)
                split[x] = "."
        ret.append(split)

    return robot, ret, len(lines[0]), len(lines)


def parse_lines(raw):
    tank, moves = raw.split("\n\n")
    robot, board, w, h = parse_group(tank)

    mret = ""
    for m in moves:
        mret += m.strip()

    return robot, board, w, h, mret

def print_board(board, rx, ry):
    for y, line in enumerate(board):
        for x, xc in enumerate(line):
            if y == ry:
                line = line[:]
                line[rx] = "@"
        print("".join(line))

def solve(raw):
    robot, board, w, h, mret = parse_lines(raw)
    print(robot, board, mret, w, h)
    def sanity_check_board(board):
        numboxes = 0
        for y, row in enumerate(board):
            for x, xc in enumerate(row):
                if "[" == xc:
                    assert row[x+1] == "]"
                    numboxes += 1
                if "]" == xc:
                    assert row[x-1] == "["
        return numboxes

    bsan = sanity_check_board(board)

    x, y = robot
    for m in mret:
        # print_board(board, x, y)
        # print(m)
        assert sanity_check_board(board) == bsan
        dx, dy = CHAR_TO_DS[m]
        nx, ny = dx + x, dy + y
        n = board[ny][nx]
        if n == "#":
            continue # would go out of bounds or hit edge.
        elif n == ".":
            x, y = nx, ny
        elif n in "[]":
            bx, by = nx, ny
            q = deque([(bx, by, board[by][bx])])
            if dy != 0:
                if board[ny][nx] == "[":
                    q.append((nx + 1, ny, board[ny][nx + 1]))
                elif board[ny][nx] == "]":
                    q.append((nx - 1, ny, board[ny][nx - 1]))

            tomoves = []

            blocked = False
            while len(q):
                (bx, by, c) = q.popleft()
                if dy != 0:
                    nbx, nby = bx + dx, by + dy
                    if board[nby][nbx] == "#":
                        blocked = True
                        break
                    tomoves.append(((bx, by), (nbx, nby), c))
                    if board[nby][nbx] == ".":
                        continue
                    else:
                        assert board[nby][nbx] in "[]"
                    # Move block and its pair
                    q.append((nbx, nby, board[nby][nbx]))
                    if board[nby][nbx] == "[":
                        q.append((nbx + 1, nby, board[nby][nbx + 1]))
                    elif board[nby][nbx] == "]":
                        q.append((nbx - 1, nby, board[nby][nbx - 1]))
                else:
                    if dx == -1:
                        assert c == "]"
                    elif dx == 1:
                        assert c == "["

                    tomoves.append(((bx, by), (bx + dx, by), c))
                    tomoves.append(((bx + dx, by), (bx + dx + dx, by), board[by][bx + dx]))

                    ebx, eby = bx + 2 * dx, by + dy # next edge
                    ec = board[eby][ebx]

                    if ec == "#":
                        blocked = True
                        break
                    elif ec == ".":
                        continue
                    else:
                        if dx == -1:
                            assert ec == "]"
                        elif dx == 1:
                            assert ec == "["
                        
                        q.append((ebx, eby, ec))
            
            if len(q) or blocked:
                # Couldn't move, do nothing.
                pass
            else:
                for (bx, by), (nbx, nby), c in tomoves:
                    board[by][bx] = "."
                for (bx, by), (nbx, nby), c in tomoves:
                    board[nby][nbx] = c
                x, y = x + dx, y + dy

        else:
            assert False

    ret = 0
    for y, row in enumerate(board):
        for x, xc in enumerate(row):
            if xc == "[":
                ret += 100 * y + x

    return ret

if __name__ == "__main__":
    SAMPLE, REAL = get_raw_inputs(sys.argv)

    sample = solve(SAMPLE)
    assert sample == SAMPLE_EXPECTED, "Sample Result %s != %s expected" % (sample, SAMPLE_EXPECTED)
    print("\n*** SAMPLE PASSED ***\n")

    solved = solve(REAL)
    print("SOLUTION: ", solved)
