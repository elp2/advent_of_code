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
SAMPLE_EXPECTED = 3
######################
assert SAMPLE_EXPECTED != None, "Must enter sample value"

def parse_group(group):
    lines = group.split("\n")
    ret = []
    for y, line in enumerate(lines):
        line = line.strip()
        ret.append(int(line))

    return ret


def parse_lines(raw):
    # Groups.
    groups = raw.split("\n\n")
    print(groups)
    # Do something with the groups.
    ranges = []
    for rline in groups[0].split("\n"):
        print(rline)
        a, b = rline.split("-")
        ranges.append((int(a), int(b)))
    

    return ranges, parse_group(groups[1])


def solve(raw):
    ranges, ingredients = parse_lines(raw)
    ret = 0
    for i in ingredients:
        for ra, rb in ranges:
            if ra <= i <= rb:
                ret += 1
                break
        


    return ret

if __name__ == "__main__":
    SAMPLE, REAL = get_raw_inputs(sys.argv)

    sample = solve(SAMPLE)
    assert sample == SAMPLE_EXPECTED, "Sample Result %s != %s expected" % (sample, SAMPLE_EXPECTED)
    print("\n*** SAMPLE PASSED ***\n")

    solved = solve(REAL)
    print("SOLUTION: ", solved)
