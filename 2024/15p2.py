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
from aoc_elp.board import *

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
    return "\n".join(ret)


def parse_lines(raw):
    blines, moves = raw.split("\n\n")
    board = Board(expand_board(blines), ("@", "."))

    mret = ""
    for m in moves:
        mret += m.strip()

    return board, mret


def solve(raw):
    board, moves = parse_lines(raw)

    def get_neighbor(pos):
        assert board.atpos(pos) in "[]"

        if board.atpos(pos) == "]":
            return pos.add(Vel(-1, 0))
        elif board.atpos(pos) == "[":
            return pos.add(Vel(1, 0))
        else:
            assert False

    for m in moves:
        board.print_board(board.movers, "@")
        print(m)
        board.validate_board(".")
        v = VelFromChar(m)

        moved = board.mover().add(v)
        mat = board.atpos(moved)
        if mat == "#":
            continue
        if mat == ".":
            board.mover().step(v)
            continue

        # Box.
        assert mat in "[]"
        if v.vx == 0:
            # Up
            neighbor = get_neighbor(moved)

            transactions = []
            valid = True
            q = deque([neighbor, moved])
            while len(q):
                moving = q.popleft()
                next = moving.add(v)
                if board.atpos(next) == "#":
                    valid = False
                    break
                transactions.append((moving, next, (".", board.atpos(moving))))

                if board.atpos(next) == ".":
                    continue
                neighbor = get_neighbor(next)
                q.append(next)
                q.append(neighbor)
            if valid:
                assert len(q) == 0
                board.apply_transactions(transactions)
                board.mover().step(v)
            else:
                pass
        else:
            transactions = []
            q = deque([moved])
            valid = True
            while len(q):
                moving = q.popleft()
                after = moving.add(v).add(v)
                if board.atpos(after) == "#":
                    valid = False
                    break
                neighbor = get_neighbor(moving)
                transactions.append((moving, moving.add(v), (".", board.atpos(moving))))
                transactions.append((neighbor, neighbor.add(v), (".", board.atpos(neighbor))))

                if board.atpos(after) == ".":
                    continue
                else:                    
                    q.append(after)

            if valid:
                assert len(q) == 0
                board.apply_transactions(transactions)
                board.mover().step(v)
            else:
                pass




    
    # Score
    ret = 0
    for y in range(board.height):
        for x in range(board.width):
            if board.at(x, y) == "[":
                ret += 100 * y + x

    return ret

if __name__ == "__main__":
    SAMPLE, REAL = get_raw_inputs(sys.argv)

    sample = solve(SAMPLE)
    assert sample == SAMPLE_EXPECTED, "Sample Result %s != %s expected" % (sample, SAMPLE_EXPECTED)
    print("\n*** SAMPLE PASSED ***\n")

    solved = solve(REAL)
    print("SOLUTION: ", solved)
