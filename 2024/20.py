from collections import defaultdict, deque, Counter
from itertools import combinations, combinations_with_replacement, permutations, product
from functools import reduce, cmp_to_key
import heapq
from operator import add, mul, itemgetter, attrgetter
import os
from parse import parse
import sys

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, root_dir)
from aoc_elp import *

######################
SAMPLE_EXPECTED = 5
######################
assert SAMPLE_EXPECTED != None, "Must enter sample value"

def parse_group(group):
    lines = group.split("\n")
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

    return start, end


def parse_lines(raw):
    start, end = parse_group(raw)
    raw = raw.replace("E", ".")
    raw = raw.replace("S", ".")
    return Board(raw), start, end


def solve(raw, minsaved):
    board, start, end = parse_lines(raw)

    ret = 0
    

    # best_to
    q = []
    q.append((0, 0, end))

    best_to = defaultdict(lambda: float('inf'))
    while q:
        cost, skips, pos = heapq.heappop(q)
        if cost >= best_to[pos]:
            continue
        best_to[pos] = cost
        for v in [Vel(1, 0), Vel(0, 1), Vel(0, -1), Vel(-1, 0)]:
            nextpos = pos.add(v)
            nextskips = skips
            nextcost = cost + 1
            if not board.validpos(nextpos) or board[pos] == "#":
                continue
            if best_to[nextpos] <= nextcost:
                continue
            heapq.heappush(q, (nextcost, nextskips, nextpos))

    noskipcost = best_to[start]
    print("NSC:", noskipcost)

    print("!")

    ret = 0
    # Starting at S, go backwards upon all decreasing cost paths. Attempt all skips.
    # We should be able to tell with our skip the continuing cost without needing to recurse again.
    visited = set()
    q = deque()
    q.append(start)
    while q:
        pos = q.popleft()
        if pos == end:
            # Reached end w/out skipping, no save possible.
            continue
        if pos in visited:
            continue
        visited.add(pos)
        for v in [Vel(1, 0), Vel(0, 1), Vel(0, -1), Vel(-1, 0)]:
            nextpos = pos.add(v)
            if board[nextpos] == "." and nextpos not in visited:
                q.append(nextpos)
            else:
                backwards = v.leftdir().leftdir()
                for sv in [Vel(1, 0), Vel(0, 1), Vel(0, -1), Vel(-1, 0)]:
                    if sv == backwards:
                        continue
                    skippos = nextpos.add(sv)
                    if not board.validpos(skippos):
                        continue
                    if board[skippos] == "#":
                        continue # no skipping into wall.
                    
                    # takes 2 to get there
                    # TODO
                    continue_cost = best_to[pos] - 2 # could be negative, do we care?
                    if continue_cost < 0:
                        print("?????negative???? skipping ", nextpos, "to", skippos, "saves", saved)
                    saved = continue_cost - best_to[skippos]
                    if saved >= minsaved:
                        ret += 1
                        print("skipping ", nextpos, "to", skippos, "saves", saved)

    return ret


if __name__ == "__main__":
    SAMPLE, REAL = get_raw_inputs(sys.argv)

    sample = solve(SAMPLE, 20)
    assert sample == SAMPLE_EXPECTED, "Sample Result %s != %s expected" % (sample, SAMPLE_EXPECTED)
    print("\n*** SAMPLE PASSED ***\n")

    solved = solve(REAL, 100)
    assert solved > 1173
    print("SOLUTION: ", solved)
