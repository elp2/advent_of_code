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
SAMPLE_EXPECTED = 3263827
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
    lines = raw.split("\n")
    oline = lines[-1]
    numlines = lines[:-1]
    ops = []
    for i, c in enumerate(oline):
        if c in "+*":
            ops.append([i, c])
    
    ret = []
    fro = ops[0][0]
    for i, c in enumerate(ops):
        fro = ops[i][0]

        if i == len(ops) -1:
            to = len(line)
        else:
            to = ops[i + 1][0]

        strs = []
        for line in numlines:
            strs.append(line[fro:to])
        ret.append((c[1], strs))

    return ret

def solve(raw):
    parsed = parse_lines(raw)
    print(parsed)

    ret = 0
    for op, nhuman in parsed:
        nums = ["" for _ in range(len(nhuman[0]))]
        mlen = max([len(n) for n in nhuman])

        for l in range(mlen):
            for i, nf in enumerate(nhuman):
                n = nf[::-1]
                if l < len(n) and n[l] != " ":
                    nums[l] += n[l]
        
        nums = [int(n) for n in nums if n != ""]
        nums = map(int, nums)
        nums = list(nums)
        print(op, nhuman, list(nums))
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
        print(op, nhuman, list(nums), "->", here)
        ret += here

    return ret

if __name__ == "__main__":
    SAMPLE, REAL = get_raw_inputs(sys.argv)

    sample = solve(SAMPLE)
    assert sample == SAMPLE_EXPECTED, "Sample Result %s != %s expected" % (sample, SAMPLE_EXPECTED)
    print("\n*** SAMPLE PASSED ***\n")

    solved = solve(REAL)
    print("SOLUTION: ", solved)
