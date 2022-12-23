from collections import defaultdict, deque, Counter
from itertools import combinations, combinations_with_replacement, permutations
from functools import reduce
import math
# import numpy as np
from operator import add, mul, itemgetter, attrgetter
import re

DS = [[-1, 0], [1, 0], [0, 1], [0, -1]]
DS8 = DS + [[-1, -1], [1, -1], [-1, 1], [1, 1]]
def arounds_inside(x, y, diagonals):
    ret = []
    for dx, dy in DS8 if diagonals else DS:
        ret.append((x + dx, y + dy))
    return ret


CHALLENGE_DAY = "23"
REAL = open(CHALLENGE_DAY + ".txt").read()

SAMPLE_EXPECTED = 20
if SAMPLE_EXPECTED:
    SAMPLE = open(CHALLENGE_DAY + ".s.txt").read()

ELF = "#"
def parse_lines(raw):
    # Groups.
    # groups = raw.split("\n\n")
    # return list(map(lambda group: group.split("\n"), groups))
    ret = set()
    lines = raw.split("\n")
    for y, row in enumerate(lines):
        for x, here in enumerate(row):
            if here == ELF:
                ret.add((x, y))
    return ret
    # return lines # raw
    # return list(map(lambda l: l.split(" "), lines)) # words.
    # return list(map(int, lines))
    # return list(map(lambda l: l.strip(), lines)) # beware leading / trailing WS

RULES=[[(-1, -1), (0, -1), (1, -1)], [(-1, 1), (0, 1), (1, 1)], [(-1, -1), (-1, 0), (-1, 1)], [(1, 1), (1, 0), (1, -1)]]
RULEMOVE=[(0, -1), (0, 1), (-1, 0), (1, 0)]
def solve(raw):
    world = parse_lines(raw)

    def get_moving_elves(world):
        ret = []
        for x, y in world:
            for ex, ey in arounds_inside(x, y, True):
                if (ex, ey) in world:
                    ret.append((x, y))
                    break
        return ret

    def propose(x, y, world, round):
        for ri in range(round, round + 4):
            adjacent_elf = False
            for (dx, dy) in RULES[ri % 4]:
                if (x + dx, y + dy) in world:
                    adjacent_elf = True
            if not adjacent_elf:
                return RULEMOVE[ri % 4]
        return None

    def run_round(world, round):
        moving_elves = get_moving_elves(world)
        deltas = {}
        for x, y in moving_elves:
            prop = propose(x, y, world, round)
            if prop:
                nx, ny = x + prop[0], y + prop[1]
                if (nx, ny) in deltas:
                    deltas[(nx, ny)] = None
                else:
                    deltas[(nx, ny)] = (x, y)
        moved = 0
        for move, old in deltas.items():
            if old == None:
                continue
            assert old != move
            world.remove(old)
            world.add(move)
            moved += 1
        if moved == 0:
            return None
        return world

    worldsize = len(world)
    round = 0
    while True:
        world = run_round(world, round)
        if not world:
            return round + 1
        assert len(world) == worldsize
        round += 1

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
