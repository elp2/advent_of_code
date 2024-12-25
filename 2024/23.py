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
SAMPLE_EXPECTED = 7
######################
assert SAMPLE_EXPECTED != None, "Must enter sample value"


def parse_lines(raw):
    connections = defaultdict(lambda: [])
    names = set()
    for line in raw.split("\n"):
        a, b = line.split("-")
        connections[a].append(b)
        connections[b].append(a)
        names.add(a)
        names.add(b)
    return names, connections

def solve(raw):
    names, connections = parse_lines(raw)
    
    ret = 0
    three_groups = set()
    for n in names:
        if n[0] != "t":
            continue
        q = deque()
        q.append([n])
        while q:
            path = q.popleft()
            if len(path) == 3:
                if path[0] in connections[path[-1]]:
                    three_groups.add(tuple(sorted(path)))
                continue
            for around in connections[path[-1]]:
                if around not in path:
                    q.append(path + [around])
    return len(three_groups)

if __name__ == "__main__":
    SAMPLE, REAL = get_raw_inputs(sys.argv)

    sample = solve(SAMPLE)
    assert sample == SAMPLE_EXPECTED, "Sample Result %s != %s expected" % (sample, SAMPLE_EXPECTED)
    print("\n*** SAMPLE PASSED ***\n")

    solved = solve(REAL)
    assert solved < 2660
    print("SOLUTION: ", solved)
