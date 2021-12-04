from collections import defaultdict, deque, Counter
from itertools import combinations, combinations_with_replacement, permutations
import math
from operator import add, mul, itemgetter, attrgetter
import re

CHALLENGE_DAY = "3"
REAL = open(CHALLENGE_DAY + ".txt").read()
SAMPLE_EXPECTED = 230
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

def mc(lines, i, gt=True):
    ies = [l[i] for l in lines]
    zc = ies.count("0")
    oc = ies.count("1")
    if zc == oc:
        if gt:
            return "1"
        else:
            return "0"
        assert False
    elif oc > zc:
        return "1" if gt else "0"
    else:
        return "0" if gt else "1"

def solve(raw):
    parsed = parse_lines(raw)
    ret = 0

    lines = parsed.copy()
    for i in range(len(parsed[0])):
        com = mc(lines, i)
        lines = [l for l in lines if l[i] == com]
        if len(lines) == 1:
            oxy = lines[0]
            break
    lines = parsed.copy()
    for i in range(len(parsed[0])):
        com = mc(lines, i, False)
        lines = [l for l in lines if l[i] == com]
        if len(lines) == 1:
            c02 = lines[0]
            break

    print(oxy, com)
    return int(oxy, 2) * int(c02, 2)

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
