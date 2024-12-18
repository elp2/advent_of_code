from collections import defaultdict, deque, Counter
import heapq
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
SAMPLE_EXPECTED = 45
######################
assert SAMPLE_EXPECTED != None, "Must enter sample value"

def parse_group(group):
    lines = group.split("\n")
    start = None
    end = None
    ret = []
    for y, line in enumerate(lines):
        line = line.strip()
        assert len(line) != 0

        split = list(line)

        for x, xc in enumerate(split):
            if xc == "S":
                start = Pos(x, y)
            elif xc == "E":
                end = Pos(x, y)
            pass

        assert len(split) != 0
        ret.append(split)
    group = group.replace("S", ".")
    group = group.replace("E", ".")

    board = Board(group)
    return board, start, end


def parse_lines(raw):
    # Groups.
    # groups = raw.split("\n\n")
    # Do something with the groups.

    return parse_group(raw)

def solve(raw):
    board, start, end = parse_lines(raw)
    q = [(0, start, Vel(1, 0))]

    best_to = defaultdict(lambda: float('inf'))
    parents = defaultdict(lambda: set())

    while q:
        score, at, facing = heapq.heappop(q)
        # print(at, facing, score, frm)
        if board[at] == "#" or best_to[(at, facing)] < score:
            continue
        best_to[(at, facing)] = score

        if at == end:
            continue

        for move_score_delta, move_pos, move_facing in [
            (1, at.add(facing), facing),
            (1000, at, facing.leftdir()),
            (1000, at, facing.rightdir()),
        ]:
            if board[move_pos] == "#": continue
            move_score = score + move_score_delta
            btk = (move_pos, move_facing)
            if best_to[btk] > move_score:
                best_to[btk] = move_score
                parents[btk] = [(at, facing)]
                heapq.heappush(q, (move_score, move_pos, move_facing))
            elif best_to[btk] == move_score:
                parents[btk].append((at, facing))
                heapq.heappush(q, (move_score, move_pos, move_facing))

    print("Backtrack")
    end_min = float('inf')
    end_parents = []
    for endv in [Vel(1,0), Vel(0,1), Vel(-1,0), Vel(0,-1)]:
        if (end, endv) in best_to:
            if best_to[(end, endv)] < end_min:
                end_min = best_to[(end, endv)]
                end_parents = [(end, endv)]
            elif best_to[(end, endv)] < end_min:
                end_parents.append((end, endv))
    print(end_parents, end_min)

    tiles = set()
    visited_posfacing = set()

    def backtrack(pos, facing):
        if (pos, facing) in visited_posfacing: return
        visited_posfacing.add((pos, facing))

        tiles.add(pos)

        for parent_pos, parent_facing in parents[(pos, facing)]:
            backtrack(parent_pos, parent_facing)
    
    for end_parent_pos, end_parent_vel in end_parents:
        backtrack(end_parent_pos, end_parent_vel)

    return len(tiles)    


if __name__ == "__main__":
    SAMPLE, REAL = get_raw_inputs(sys.argv)

    sample = solve(SAMPLE)
    assert sample == SAMPLE_EXPECTED, "Sample Result %s != %s expected" % (sample, SAMPLE_EXPECTED)
    print("\n*** SAMPLE PASSED ***\n")
    
    solved = solve(REAL)
    assert solved > 516
    print("SOLUTION: ", solved)
