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
SAMPLE_EXPECTED = 1227775554
######################
assert SAMPLE_EXPECTED != None, "Must enter sample value"

def parse_group(group):
    ranges = group.split(",")
    ret = []
    for r in ranges:
        a, b = map(int, r.split("-"))
        ret.append((a, b))

    return ret


def parse_lines(raw):
    # Groups.
    # groups = raw.split("\n\n")
    # Do something with the groups.

    return parse_group(raw)

def valid(num):
    nstr = str(num)
    if len(nstr) % 2 == 1:
        return True
    a = nstr[:int(len(nstr) / 2)]
    b = nstr[int(len(nstr) / 2):]
    return a != b


def solve(raw):
    parsed = parse_lines(raw)
    print(parsed)

    ret = 0
    for a, b in parsed:
        for x in range(a, b + 1):
            if not valid(x):
                ret += x

    return ret

if __name__ == "__main__":
    SAMPLE, REAL = get_raw_inputs(sys.argv)

    sample = solve(SAMPLE)
    assert sample == SAMPLE_EXPECTED, "Sample Result %s != %s expected" % (sample, SAMPLE_EXPECTED)
    print("\n*** SAMPLE PASSED ***\n")

    solved = solve(REAL)
    print("SOLUTION: ", solved)
