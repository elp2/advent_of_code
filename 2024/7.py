from collections import defaultdict, deque, Counter
from itertools import combinations, combinations_with_replacement, permutations, product
from functools import reduce, cmp_to_key
import math
# import numpy as np
from operator import add, mul, itemgetter, attrgetter
from parse import parse
import os
import re
from sys import argv

def flatten(t):
    return [item for sublist in t for item in sublist]

# Sorts with cmp. cmp < 0 for a < b, == 0 for a==b, > 0 for a > b.
def elpsort(array, cmp):
    return sorted(array, key=cmp_to_key(cmp))

ON_TEXT = '\u2588'
OFF_TEXT = '\u2592'

LEFT = (-1, 0)
UP = (0, -1)
RIGHT = (1, 0)
DOWN = (0, 1)
CHAR_TO_DS = {"^": UP, ">": RIGHT, "<": LEFT, "v": DOWN}
DS = [LEFT, UP, RIGHT, DOWN] # +IDX = TURN RIGHT
UPLEFT = (-1, -1)
UPRIGHT = (1, -1)
DOWNRIGHT = (1, 1)
DOWNLEFT = (-1, 1)
DS8 = [LEFT, UPLEFT, UP, UPRIGHT, RIGHT, DOWNRIGHT, DOWN, DOWNLEFT] # +IDX = TURN RIGHT

def arounds(x, y, diagonals):
    ret = []
    for dx, dy in DS8 if diagonals else DS:
        ret.append((x + dx, y + dy))
    return ret

CHALLENGE_DAY = argv[0].split("/")[-1].replace("p2.py", "").replace(".py", "")
AOC_DIR = os.path.dirname(argv[0])

print("Day: ", CHALLENGE_DAY)

######################
SAMPLE_EXPECTED = 3749
######################
assert SAMPLE_EXPECTED != None

try:
    sample_file = os.path.join(AOC_DIR, CHALLENGE_DAY + ".s.txt")
    SAMPLE = open(sample_file).read()
except:
    assert None, "Missing Sample File: %s" % (sample_file)

try:
    solutions_file = os.path.join(AOC_DIR, CHALLENGE_DAY + ".txt")
    REAL = open(solutions_file).read()
except:
    assert None, "Missing Solutions File: %s" % (solutions_file)

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

            # func = ""
            # for i in range(len(nums)):
            #     func += str(nums[i])
            #     if i != len(nums) - 1:
            #         func += ops[i]
            # # print(func)
            # actual = eval(func)
            # if target == 292:
            #     print("???", actual, func)
            if actual == target:
                print(ops, actual)
                ret += target
                break

    return ret

sample = solve(SAMPLE)
assert sample == SAMPLE_EXPECTED, "Sample Result %s != %s expected" % (sample, SAMPLE_EXPECTED)
print("\n*** SAMPLE PASSED ***\n")

solved = solve(REAL)
print("SOLUTION: ", solved)
