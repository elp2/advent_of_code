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
SAMPLE_EXPECTED = 4277556
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
    def ssplit(l):
        l = l.strip()
        s = l.split(" ")
        return [x for x in s if x != ""]
    lines = raw.split("\n")
    ops = ssplit(lines[-1])
    probs = [[o, []] for o in ops]
    
    for nline in lines[:-1]:
        for i, n in enumerate(ssplit(nline)):
            probs[i][1].append(int(n))
    
    return probs


def solve(raw):
    parsed = parse_lines(raw)
    print(parsed)

    ret = 0
    for op, nums in parsed:
        here = None
        if op == "*":
            here = 1
        elif op == "+":
            here = 0
        
        for n in nums:
            if op == "*":
                here *= n
            else:
                here += n

        print(here)
        ret += here

    return ret

if __name__ == "__main__":
    SAMPLE, REAL = get_raw_inputs(sys.argv)

    sample = solve(SAMPLE)
    assert sample == SAMPLE_EXPECTED, "Sample Result %s != %s expected" % (sample, SAMPLE_EXPECTED)
    print("\n*** SAMPLE PASSED ***\n")

    solved = solve(REAL)
    print("SOLUTION: ", solved)
