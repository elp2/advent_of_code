from collections import defaultdict, deque, Counter
from itertools import combinations, combinations_with_replacement, permutations
from functools import reduce, cmp_to_key
import math
# import numpy as np
from operator import add, mul, itemgetter, attrgetter
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

CHAR_TO_DS = {"^": 3, ">": 1, "<": 0, "v": 2}
DS = [(-1, 0), (1, 0), (0, 1), (0, -1)]
DS8 = DS + [(-1, -1), (1, -1), (-1, 1), (1, 1)]
def arounds(x, y, diagonals):
    ret = []
    for dx, dy in DS8 if diagonals else DS:
        ret.append((x + dx, y + dy))
    return ret

CHALLENGE_DAY = argv[0].split("/")[-1].replace(".py", "").replace("p2.py", "")
AOC_DIR = os.path.dirname(argv[0])

print("Day: ", CHALLENGE_DAY)

######################
SAMPLE_EXPECTED = "2=-1=0"
######################
assert SAMPLE_EXPECTED != None

try:
    SAMPLE = open(os.path.join(AOC_DIR, CHALLENGE_DAY + ".s.txt")).read()
except:
    print("Did you create the sample file?")

try:
    REAL = open(os.path.join(AOC_DIR, CHALLENGE_DAY + ".txt")).read()
except:
    print("Did you create the solutions file?")


def parse_lines(raw):
    # Groups.
    # groups = raw.split("\n\n")
    # return list(map(lambda group: group.split("\n"), groups))
    lines = raw.split("\n")
    return lines # raw
    # return list(map(lambda l: l.split(" "), lines)) # words.
    # return list(map(int, lines))
    # return list(map(lambda l: l.strip(), lines)) # beware leading / trailing WS


R={"0": 0, "1": 1, "2": 2, "-": -1, "=": -2}


SNAFU="=-012"



def snafud(num):
    ret = 0
    num = num[::-1]
    p = 1
    for i, c in enumerate(num):
        here = p * R[c]
        ret += here
        print(c, here)
        p *= 5
    return ret

def adds(a, b):
    lendiff = len(a) - len(b)
    a = "0" * (-1 * lendiff) + a
    b = "0" * (1 * lendiff) + b
    assert len(a) == len(b)

    ret = []
    carry = 0
    for i in range(len(a) - 1, -1, -1):
        av = R[a[i]]
        bv = R[b[i]]
        here = av + bv + carry
        if -2 <= here <= 2:
            ret.append(here)
            carry = 0
        elif here > 2:
            ret.append(here - 5)
            carry = 1
        elif here < -2:
            ret.append(here + 5)
            carry = -1
        else:
            assert False

    if carry:
        ret.append(carry)
    stringy = ""
    for v in ret[::-1]:
        assert -2 <= v <= 2
        stringy += SNAFU[v + 2]
    
    return stringy

assert adds("-", "-") == "="
assert adds("1", "1") == "2"
assert adds("1", "2") == "1="


def solve(raw):


    parsed = parse_lines(raw)
    ret = "0"
    for n in parsed:
        ret = adds(ret, n)

    return ret

if SAMPLE_EXPECTED != None:
    sample = solve(SAMPLE)
    if sample != SAMPLE_EXPECTED:
        print("SAMPLE FAILED: ", sample, " != ", SAMPLE_EXPECTED)
    assert sample == SAMPLE_EXPECTED
    print("\n*** SAMPLE PASSED ***\n")
else:
    print("Skipping sample")


solved = solve(REAL)
print("SOLUTION: ", solved)


# def addsnafu(num):
#     def inc(c, carry):
#         if not carry:
#             return c, False
#         if c == "2":
#             return "=", True
#         else:
#             return SNAFU[SNAFU.index(c) + 1], False
#     num = num[::-1]
#     ret = ""
#     carry = True
#     for i, c in enumerate(num):
#         nc, carry = inc(c, carry)
#         ret += nc
#         if not carry:
#             break
#     ret = ret + ""
#     ret = ret[::-1]
#     if carry:
#         ret = "1" + ret
#     return ret

# num = "0"
# for i in range(20):
#     print(num)
#     num = addsnafu(num)


REV = {-2: "=", -1: "-", 0: "0", 1: "1", 2: "2"}
def reverse(snafud):
    dec = 0
    
    p = 1
    i = len(snafud) - 1
    carry = 0
    while i > -1:
        c = snafud[i]


        p *= 5
        i -= 1


# assert reverse("-") == -1


