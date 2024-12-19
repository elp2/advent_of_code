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
SAMPLE_EXPECTED = 16
######################
assert SAMPLE_EXPECTED != None, "Must enter sample value"

def parse_group(group):
    lines = group.split("\n")
    ret = []
    for y, line in enumerate(lines):
        line = line.strip()
        assert len(line) != 0

        split = line.split(" ")

        for x, xc in enumerate(split):
            pass

        assert len(split) != 0
        ret.append(split)

    return ret


def parse_lines(raw):
    # Groups.
    towels, patterns = raw.split("\n\n")
    # Do something with the groups.

    return towels.split(", "), patterns.split("\n")

def can_make(pattern, towels):
    starts = defaultdict(lambda: set())
    for i in range(len(pattern)):
        for t in towels:
            if pattern[i:i + len(t)] == t:
                print(i, t)
                starts[i].add(len(t))
    cache = {}
    def rec(i, plen, starts):
        if i in cache:
            return cache[i]
        
        if i >= plen:
            return 1

        ret = 0
        for l in starts[i]:
            ret += rec(i + l, plen, starts)
            
        cache[i] = ret
        return ret
    return rec(0, len(pattern), starts)


def solve(raw):
    towels, patterns = parse_lines(raw)
    
    ret = 0
    for p in patterns:
        made = can_make(p, towels)
        if made: print(p, "made ", made)
        ret += made
    return ret

if __name__ == "__main__":
    SAMPLE, REAL = get_raw_inputs(sys.argv)

    sample = solve(SAMPLE)
    assert sample == SAMPLE_EXPECTED, "Sample Result %s != %s expected" % (sample, SAMPLE_EXPECTED)
    print("\n*** SAMPLE PASSED ***\n")

    solved = solve(REAL)
    print("SOLUTION: ", solved)
