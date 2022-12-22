from collections import defaultdict, deque, Counter
from itertools import combinations, combinations_with_replacement, permutations
from functools import reduce
import math
# import numpy as np
from operator import add, mul, itemgetter, attrgetter
import re

PIECES=[
"####",

""" # 
###
 # """,

"""  #
  #
###""",

"""#
#
#
#""",

"""##
##"""]

PIECES = [list(reversed(p.split("\n"))) for p in PIECES]

DS = [[-1, 0], [1, 0], [0, 1], [0, -1]]
DS8 = DS + [[-1, -1], [1, -1], [-1, 1], [1, 1]]
def arounds_inside(x, y, diagonals, w, h):
    ret = []
    for dx, dy in DS8 if diagonals else DS:
        ret.append((x + dx, y + dy))


CHALLENGE_DAY = "17"
REAL = open(CHALLENGE_DAY + ".txt").read()

SAMPLE_EXPECTED = 1514285714288
if SAMPLE_EXPECTED:
    SAMPLE = open(CHALLENGE_DAY + ".s.txt").read()


def parse_lines(raw):
    return raw.strip()
    # Groups.
    # groups = raw.split("\n\n")
    # return list(map(lambda group: group.split("\n"), groups))
    # lines = raw.split("\n")
    # return lines # raw
    # return list(map(lambda l: l.split(" "), lines)) # words.
    # return list(map(int, lines))
    # return list(map(lambda l: l.strip(), lines)) # beware leading / trailing WS

WIDTH = 7
EMPTY = "."
ROCK = "#"

def solve(raw, num_drop_pieces):
    moves = parse_lines(raw).strip()
    ret = 0

    highest_rock = 0 # Also our return
    # Each rock appears so that its left edge is two units away from the left wall
    # and its bottom edge is three units above the highest rock in the room (or the floor,

    pposes = set()
    board = defaultdict(lambda: EMPTY)
    mi = 0
    def board_at(x, y):
        assert 0 <= x < WIDTH
        return board[(x, y)]
    
    states = Counter()

    ftt = []
    def can_move(p, px, py, board):
        if px < 0 or px + len(p[0]) - 1 >= WIDTH:
            return False
        if py == 0:
            return False
        
        for y in range(len(p)):
            cy = py + y
            for x in range(len(p[0])):
                if ROCK != p[y][x]:
                    continue
                cx = x + px
                if board_at(cx, cy) == ROCK:
                    return False
        return True

    def print_board(board):
        return
        for y in range(highest_rock, 0, -1):
            line = "|"
            for x in range(WIDTH):
                line += board_at(x, y)
            line += "|"
            print(line)
        print("+-------+\n")

    rock_places = []
    for ri in range(num_drop_pieces):
        p = PIECES[ri % len(PIECES)]
        x = 2
        y = highest_rock + 4
        states[(mi, ri % len(PIECES))] += 1
        mistart = mi

        if (42,2) == (mi, ri % len(PIECES)):
            diff = None if not len(ftt) else ri -ftt[-1][0]
            ftt.append((ri, diff))
        while True:
            move = moves[mi]
            mi += 1
            if mi == len(moves):
                mi = 0

            if move == "<":
                dx = -1
            elif move == ">":
                dx = 1
            else:
                assert False
            if can_move(p, x + dx, y, board):
                x += dx
                #print("Move", "Left" if dx == -1 else "Right")
            # else:
            #     print("Couldn't move", "Left" if dx == -1 else "Right")

            # Fall
            if can_move(p, x, y - 1, board):
                # print("Fall")
                y -= 1
            else:
                # print("Placing at ", y)
                pposes.add((x, y))
                prev_highest_rock = highest_rock

                for py in range(len(p)):
                    for px in range(len(p[0])):
                        if p[py][px] != ROCK:
                            continue
                        ax = px + x
                        ay = py + y
                        assert board_at(ax, ay) == EMPTY
                        board[(ax, ay)] = ROCK
                        highest_rock = max(ay, highest_rock)
                rock_places.append((ri, ri % len(PIECES), mistart, prev_highest_rock, highest_rock))

                # print("Placed at ", highest_rock)
                print_board(board)
                break

    # Any impossibly skipped rows?
    for y in range(1, highest_rock + 1):
        row_seen = False
        for x in range(WIDTH):
            if board_at(x, y) == ROCK:
                row_seen = True
        assert row_seen
    
    PART2 = 1000000000000
    (mi, pi), _ = states.most_common(1)[0]
    loops = []
    for i, r in enumerate(rock_places):
        if r[1] == pi and r[2] == mi:
            # ((ri, ri % len(PIECES), mistart, prev_highest_rock, highest_rock))
            print(r)
            loops.append(r)
    loops = loops[1:]
    loop_start_height = loops[0][-2]
    loop_start_ri = loops[0][0]
    loop_len = loops[1][0] - loops[0][0]
    loop_height = loops[1][-1] - loops[0][-1]

    ret = loop_start_height
    num_loops = int((PART2 - loop_start_ri) / loop_len)
    ret += num_loops * loop_height
    rem_rocks = PART2 - num_loops * loop_len - loop_start_ri

    i = loops[0][0]
    r = loops[0]

    # for i, r in enumerate(rock_places):
    #     if r[1] == pi and r[2] == mi:
    #         break
    while rem_rocks:
        i += 1
        rem_rocks -= 1
    rinew = rock_places[i]
    gained = rinew[-2] - r[-2]

    return ret + gained

if SAMPLE_EXPECTED != None:
    sample = solve(SAMPLE, 10000)
    if sample != SAMPLE_EXPECTED:
        print("SAMPLE FAILED: ", sample, " != ", SAMPLE_EXPECTED)
    assert sample == SAMPLE_EXPECTED
    print("\n*** SAMPLE PASSED ***\n")
else:
    print("Skipping sample")

solved = solve(REAL, 10000)
assert solved > 1595988538690
print(solved)