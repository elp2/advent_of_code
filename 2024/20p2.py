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
SAMPLE_EXPECTED = 22 + 4 + 3
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


def solve(raw, minsaved, maxskips):
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
    for pos in best_to:
        if pos == end:
            continue
        if board[pos] == "#":
            continue

        for y in range(pos.y - 21, pos.y + 21):
            for x in range(pos.x - 21, pos.x + 21):

                manhattan = abs(pos.x - x) + abs(pos.y - y)
                if manhattan <= maxskips:
                    skippos = Pos(x, y)
                    if not board.validpos(skippos):
                        continue
                    if board[skippos] != ".":
                        continue
                    continue_cost = best_to[pos] - manhattan
                    saved = continue_cost - best_to[skippos]
                    if saved >= minsaved:
                        # if (pos, skippos) not in scored_skips:
                        #     scored_skips.add((pos, skippos))
                        ret += 1
                        # print("skipping ", pos, "to", skippos, "saves", saved)



    return ret


if __name__ == "__main__":
    SAMPLE, REAL = get_raw_inputs(sys.argv)

    sample = solve(SAMPLE, 12, 2)
    assert sample == 8, "Sample Result %s != %s expected" % (sample, 8)
    print("\n*** SAMPLE5 PASSED ***\n")

    sample = solve(SAMPLE, 72, 20)
    assert sample == SAMPLE_EXPECTED, "Sample Result %s != %s expected" % (sample, SAMPLE_EXPECTED)
    print("\n*** SAMPLE PASSED ***\n")

    solved = solve(REAL, 100, 20)
    print("S", solved)
    assert solved > 939553
    assert solved != 1825816
    print("SOLUTION: ", solved)
