from collections import defaultdict, deque, Counter
from itertools import combinations, combinations_with_replacement, permutations
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

LEFT = 0
UP = 1
RIGHT = 2
DOWN = 3
CHAR_TO_DS = {"^": UP, ">": RIGHT, "<": LEFT, "v": DOWN}
DS = [(-1, 0), (0, -1), (1, 0), (0, 1)]
DS8 = DS + [(-1, -1), (1, -1), (-1, 1), (1, 1)]

def arounds(x, y, diagonals):
    ret = []
    for dx, dy in DS8 if diagonals else DS:
        ret.append((x + dx, y + dy))
    return ret

CHALLENGE_DAY = argv[0].split("/")[-1].replace("p2.py", "").replace(".py", "")
AOC_DIR = os.path.dirname(argv[0])

print("Day: ", CHALLENGE_DAY)

######################
SAMPLE_EXPECTED = 48
######################
assert SAMPLE_EXPECTED != None, "Set the expected sample"

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

DO = "do()"
DONT = "don't()"
def next_instruction(mem, ptr):
    while ptr < len(mem):
        print(ptr, mem[ptr])
        if mem[ptr] == "m":
            try:
                mul = mem[ptr:mem.index(")", ptr) + 1]
                print(mul)
                ma, mb = parse("mul({:d},{:d})", mul)
                return "mul", ptr + 1, (ma, mb)
            except:
                ptr += 1
        elif mem[ptr] == "d":
            if mem[ptr:ptr + len(DO)] == DO:
                return "do", ptr + 1, None
            elif mem[ptr:ptr + len(DONT)] == DONT:
                return "don't", ptr + 1, None
        else:
            ptr += 1

    return None, None, None
    


def parse_group(group):
    lines = group.split("\n")
    ret = []

    muls_enabled = True # ???
    for line in lines:
        line = line.strip()
        assert len(line) != 0

        muls = []
        start = 0
        while start < len(line):
            op, start, data = next_instruction(line, start)
            print(op, start, data)
            if op == "don't":
                muls_enabled = False
            elif op == "do":
                muls_enabled = True
            elif op == "mul":
                if muls_enabled:
                    muls.append((data[0], data[1]))
                else:
                    print("skipping ", data)
            else:
                assert op == None
                break

        ret.append(muls)

    return ret


def parse_lines(raw):
    # Groups.
    # groups = raw.split("\n\n")
    # Do something with the groups.

    return parse_group(raw)


def solve(raw):
    parsed = parse_lines(raw)

    ret = 0
    for line in parsed:
        for a, b in line:
            ret += a * b

    return ret

sample = solve(SAMPLE)
assert sample == SAMPLE_EXPECTED, "Sample Result %s != %s expected" % (sample, SAMPLE_EXPECTED)
print("\n*** SAMPLE PASSED ***\n")

solved = solve(REAL)
assert solved not in [3180907]
print("SOLUTION: ", solved)
