from collections import defaultdict, deque, Counter
from itertools import combinations, combinations_with_replacement, permutations, product
from functools import reduce, cmp_to_key
import multiprocessing as mp
from operator import add, mul, itemgetter, attrgetter
import os
import sys

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, root_dir)
from aoc_elp import *

######################
SAMPLE_EXPECTED = 3121910778619
######################
assert SAMPLE_EXPECTED != None, "Must enter sample value"

def parse_group(group):
    lines = group.split("\n")
    ret = []
    for y, line in enumerate(lines):
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

def bankval(CACHE, bank, i, picked, sofar):
    if (i, picked) in CACHE and CACHE[(i, picked)] >= sofar:
        return 0
    CACHE[(i, picked)] = sofar
    if picked == 12:
        return sofar
    if i == len(bank):
        return 0
    pickat = sofar * 10 + bank[i]
    pbv = bankval(CACHE, bank, i + 1, picked + 1, pickat)

    skip = bankval(CACHE, bank, i + 1, picked, sofar)
    return max(pbv, skip)

    # ons = [False] * len(bank)
    # for _ in range(12):
    #     maxi, maxv = -1, -1
    #     for i in range(len(bank)):
    #         if ons[i]:
    #             continue
    #         if bank[i] > maxv:
    #             maxi = i
    #             maxv = bank[i]
    #     ons[maxi] = True
    
    # num = ""
    # for i, b, in enumerate(bank):
    #     if ons[i]:
    #         num += str(b)
    # assert len(num) == 12
    # return int(num)

def sbank(bank):
    CACHE = {}
    bv = bankval(CACHE, bank, 0, 0, 0)
    print("done")
    return bv



def solve(raw):
    parsed = parse_lines(raw)
    print(parsed)

    ret = 0

    with mp.Pool(processes=16) as pool:
        results = pool.map(sbank, parsed)


    return sum(results)

if __name__ == "__main__":
    SAMPLE, REAL = get_raw_inputs(sys.argv)

    sample = solve(SAMPLE)
    assert sample == SAMPLE_EXPECTED, "Sample Result %s != %s expected" % (sample, SAMPLE_EXPECTED)
    print("\n*** SAMPLE PASSED ***\n")

    solved = solve(REAL)
    print("SOLUTION: ", solved)
