from collections import defaultdict, deque, Counter
from itertools import combinations, combinations_with_replacement, permutations, product
from functools import reduce, cmp_to_key
from operator import add, mul, itemgetter, attrgetter
import os
from parse import parse
import sys
import heapq

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, root_dir)
from aoc_elp import *

######################
SAMPLE_EXPECTED = 40
######################
assert SAMPLE_EXPECTED != None, "Must enter sample value"

def parse_group(group):
    lines = group.split("\n")
    ret = []
    for y, line in enumerate(lines):
        line = line.strip()
        assert len(line) != 0
        x, y, z = map(int, line.split(","))
        ret.append((x, y, z))

    return ret


def parse_lines(raw):
    # Groups.
    # groups = raw.split("\n\n")
    # Do something with the groups.

    return parse_group(raw)


def solve(raw, joins):
    parsed = parse_lines(raw)

    heap = []
    heapq.heapify(heap)
    for i, (ax, ay, az) in enumerate(parsed):
        for j, (bx, by, bz) in enumerate(parsed[i + 1:]):
            dx, dy, dz = abs(ax - bx), abs(ay - by), abs(az - bz)
            heapq.heappush(heap, (dx * dx + dy * dy + dz * dz, ((ax, ay, az), (bx, by, bz))))
    
    seens = set()

    groups = []
    while joins > 0:
        glens = [len(g) for g in groups]
        print(sorted(glens))

        (dist, (a, b)) = heapq.heappop(heap)
        print(dist, a, b)
        ag, bg = None, None
        for g in groups:
            if a in g:
                ag = g
            if b in g:
                bg = g
        if ag != None and ag == bg:
            print("Skipping ", a, b)        
        elif ag == None and bg == None:
            print("new group for ", a, b)
            ng = set()
            ng.add(a)
            ng.add(b)
            groups.append(ng)
        elif ag == None and bg != None:
            print("adding ", a, " to ", bg)
            bg.add(a)
        elif ag != None and bg == None:
            print("adding ", b, " to ", ag)
            ag.add(b)
        else:
            groups.remove(ag)
            groups.remove(bg)
            groups.append(ag.union(bg))

        joins -= 1

    ret = 1
    print(groups)
    glens = [len(g) for g in groups]
    print(glens)

    for glen in sorted(glens)[-3:]:
        ret *= glen
    return ret

if __name__ == "__main__":
    SAMPLE, REAL = get_raw_inputs(sys.argv)

    sample = solve(SAMPLE, 10)
    assert sample == SAMPLE_EXPECTED, "Sample Result %s != %s expected" % (sample, SAMPLE_EXPECTED)
    print("\n*** SAMPLE PASSED ***\n")

    solved = solve(REAL, 1000)
    print("SOLUTION: ", solved)
