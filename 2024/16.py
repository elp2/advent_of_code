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
SAMPLE_EXPECTED = 7036
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

    best_to = {}
    best_queued = {}
    q = deque([(start, Vel(1, 0), 0)])
    best_queued[(start, Vel(1, 0))] = 1
    ret = None

    times = 0
    while len(q):
        times += 1
        if times < 10:
            print(len(q), "\n", best_to, "\n", best_queued)
        if times % 1000 == 0:
            print(len(q))
        at, facing, steps = q.popleft()
        if board[at] == "#":
            continue
        if at == end:
            print("End!!!")
            if ret == None or ret > steps:
                ret = steps
            continue
         
        k = (at, facing)
        if best_queued[k] < steps:
            continue
        if k not in best_to or best_to[k] > steps:
            best_to[k] = steps
        else:
            continue
        
        def maybeq(p, f, s):
            if board[p] == "#":
                return
            k = (p, f)
            if p in best_queued and best_queued[k] > s:
                return          
            best_queued[k] = s
            q.append((p, f, s))

        maybeq(at.add(facing), facing, steps + 1)
        tl = facing.leftdir()
        maybeq(at.add(tl), tl, steps + 1 + 1000)
        tr = facing.rightdir()
        maybeq(at.add(tr), tr, steps + 1 + 1000)

    return ret

if __name__ == "__main__":
    SAMPLE, REAL = get_raw_inputs(sys.argv)

    sample = solve(SAMPLE)
    assert sample == SAMPLE_EXPECTED, "Sample Result %s != %s expected" % (sample, SAMPLE_EXPECTED)
    print("\n*** SAMPLE PASSED ***\n")

    solved = solve(REAL)
    print("SOLUTION: ", solved)
