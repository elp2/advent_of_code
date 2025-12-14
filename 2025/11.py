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
SAMPLE_EXPECTED = 5
######################
assert SAMPLE_EXPECTED != None, "Must enter sample value"

def parse_group(group):
    lines = group.split("\n")
    ret = {}
    for y, line in enumerate(lines):
        line = line.strip()
        assert len(line) != 0

        split = line.split(":")
        f = split[0]
        tos = [s for s in split[1].split(" ") if len(s) > 0]
        ret[f] = tos
    return ret


def parse_lines(raw):
    # Groups.
    # groups = raw.split("\n\n")
    # Do something with the groups.

    return parse_group(raw)


def solve(raw):
    graph = parse_lines(raw)
    print(graph)
    ret = 0
    q = deque(["you"])
    while len(q):
        at = q.popleft()
        if at == "out":
            ret += 1
            continue
        for n in graph[at]:
            q.append(n)


    return ret

if __name__ == "__main__":
    SAMPLE, REAL = get_raw_inputs(sys.argv)

    sample = solve(SAMPLE)
    assert sample == SAMPLE_EXPECTED, "Sample Result %s != %s expected" % (sample, SAMPLE_EXPECTED)
    print("\n*** SAMPLE PASSED ***\n")

    solved = solve(REAL)
    print("SOLUTION: ", solved)
