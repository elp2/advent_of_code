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
SAMPLE_EXPECTED = 1928
######################
assert SAMPLE_EXPECTED != None, "Must enter sample value"

def parse_group(group):
    lines = group.split("\n")
    ret = []
    for line in lines:
        line = line.strip()
        assert len(line) != 0

        split = list(map(int, list(line)))
        assert len(split) != 0
        ret.append(split)

    return ret


def parse_lines(raw):
    # Groups.
    # groups = raw.split("\n\n")
    # Do something with the groups.

    return parse_group(raw)

def checksum(fs):
    print(fs)
    ret = 0
    for i, f in enumerate(fs):
        if f == None:
            continue
        ret += i * f
    return ret

def expand(fs):
    expanded = []
    fsi = 0

    blocknum = 0
    while fsi < len(fs):
        here = fs[fsi:fsi + 2]
        if len(here) == 1:
            here.append(None)
        
        block, empty = here
        for _ in range(block):
            expanded.append(blocknum)

        print(blocknum, block)
        blocknum += 1
        if empty != None:
            for _ in range(empty):
                expanded.append(None)

        fsi += 2

    return expanded
        
def compress(e):
    left = e.index(None)
    right = len(e) - 1
    while left < right:
        assert e[left] == None
        assert e[right] != None
        e[left] = e[right]
        left = e.index(None, left + 1)
        e[right] = None
        while e[right] == None and left < right:
            right -= 1
    return e



def solve(raw):
    parsed = parse_lines(raw)[0]
    print(parsed)
    e = expand(parsed)
    print("exp: ", e)
    c = compress(e)
    print(c)

    return(checksum(e))

if __name__ == "__main__":
    SAMPLE, REAL = get_raw_inputs(sys.argv)

    sample = solve(SAMPLE)
    assert sample == SAMPLE_EXPECTED, "Sample Result %s != %s expected" % (sample, SAMPLE_EXPECTED)
    print("\n*** SAMPLE PASSED ***\n")

    solved = solve(REAL)
    print("SOLUTION: ", solved)
