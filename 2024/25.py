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


def parse_lines(raw):
    keys = []
    locks = []

    for lines in raw.split("\n\n"):
        lines = lines.split("\n")
        islock = lines[0] == "....."
        print(islock)
        if islock:
            lines.reverse()
        
        kl = [0] * len(lines[0])
        for i in range(1, len(lines)):
            print(lines[i])
            for j in range(len(lines[i])):
                if lines[i][j] == "#":
                    kl[j] += 1
        
        if islock:
            locks.append(kl)
        else:
            keys.append(kl)

    return keys, locks

def solve(raw):
    keys, locks = parse_lines(raw)

    ret = 0
    for k in keys:
        for l in locks:
            fit = [0] * len(l)
            for i in range(len(k)):
                fit[i] = k[i] + l[i]
            fits = all([f <= 5 for f in fit])
            if fits:
                ret += 1
                print("FIT", k, l)
            print(k, l, fit)


    return ret

if __name__ == "__main__":
    SAMPLE, REAL = get_raw_inputs(sys.argv)

    sample = solve(SAMPLE)
    assert sample == SAMPLE_EXPECTED, "Sample Result %s != %s expected" % (sample, SAMPLE_EXPECTED)
    print("\n*** SAMPLE PASSED ***\n")

    solved = solve(REAL)
    print("SOLUTION: ", solved)
