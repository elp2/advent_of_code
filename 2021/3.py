from collections import defaultdict, deque, Counter
from itertools import combinations, combinations_with_replacement, permutations
import math
from operator import add, mul, itemgetter, attrgetter
import re

CHALLENGE_DAY = "3"
REAL = open(CHALLENGE_DAY + ".txt").read()
SAMPLE_EXPECTED = 198
if SAMPLE_EXPECTED:
    SAMPLE = open(CHALLENGE_DAY + ".s.txt").read()


def parse_lines(raw):
    # Groups.
    # groups = raw.split("\n\n")
    # return list(map(lambda group: group.split("\n"), groups))
    lines = raw.split("\n")
    return lines # raw
    # return list(map(lambda l: l.split(" "), lines)) # words.
    # return list(map(int, lines))
    # return list(map(lambda l: l.strip(), lines)) # beware leading / trailing WS

def mc(lines, i):
    ies = [l[i] for l in lines]
    zc = ies.count("0")
    oc = ies.count("1")
    if zc == oc:
        assert False
    elif oc > zc:
        return "1"
    else:
        return "0"

def solve(raw):
    parsed = parse_lines(raw)
    ret = 0
    gamma = "".join([mc(parsed, i) for i in range(len(parsed[0]))])
    epsilon = "".join(["1" if g == "0" else "0" for g in gamma])        

    return int(gamma, 2) * int(epsilon, 2)

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
