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
SAMPLE_EXPECTED = 3749
######################
assert SAMPLE_EXPECTED != None

def parse_group(group):
    lines = group.split("\n")
    ret = []
    for line in lines:
        line = line.strip()
        assert len(line) != 0
        line = line.replace(":", "")
        ints = list(map(int, line.split(" ")))
        target = ints[0]
        nums = ints[1:]
        ret.append((target, nums))

    return ret


def parse_lines(raw):
    # Groups.
    # groups = raw.split("\n\n")
    # Do something with the groups.

    return parse_group(raw)


def solve(raw):
    parsed = parse_lines(raw)
    print(parsed)

    ret = 0
    for (target, nums) in parsed:
        for ops in product(["+", "*"], repeat=len(nums) - 1):
            actual = nums[0]
            for i in range(1, len(nums)):
                o = ops[i-1]
                if o == "+":
                    actual += nums[i]
                else:
                    actual *= nums[i]

            if actual == target:
                print(ops, actual)
                ret += target
                break

    return ret

if __name__ == "__main__":
    SAMPLE, REAL = get_raw_inputs(sys.argv)

    sample = solve(SAMPLE)
    assert sample == SAMPLE_EXPECTED, "Sample Result %s != %s expected" % (sample, SAMPLE_EXPECTED)
    print("\n*** SAMPLE PASSED ***\n")

    solved = solve(REAL)
    print("SOLUTION: ", solved)
