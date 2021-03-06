from collections import defaultdict, deque, Counter
from itertools import combinations, combinations_with_replacement, permutations
import math
# import numpy as np
from operator import add, mul, itemgetter, attrgetter
import re
from typing import Deque

CHALLENGE_DAY = "10"
REAL = open(CHALLENGE_DAY + ".txt").read()

SAMPLE_EXPECTED = 26397
if SAMPLE_EXPECTED:
    SAMPLE = open(CHALLENGE_DAY + ".s.txt").read()

ILLEGAL = {")": 3, "]": 57, "}": 1197, ">": 25137}
CLOSERS = {"(": ")", "[": "]", "{": "}", "<": ">"}
CLOSER_EXPECTED = {}
for k, v in CLOSERS.items():
    CLOSER_EXPECTED[v] = k

def parse_lines(raw):
    # Groups.
    # groups = raw.split("\n\n")
    # return list(map(lambda group: group.split("\n"), groups))
    lines = raw.split("\n")
    return lines # raw
    # return list(map(lambda l: l.split(" "), lines)) # words.
    # return list(map(int, lines))
    # return list(map(lambda l: l.strip(), lines)) # beware leading / trailing WS

def solve(raw):
    parsed = parse_lines(raw)

    ret = 0
    for line in parsed:
        print(line, ret)
        stack = Deque()
        for c in line:
            if c in CLOSERS.values():
                top = stack.pop()
                expected = CLOSER_EXPECTED[c]
                if expected != top:
                    print(c, expected)
                    ret += ILLEGAL[c]
                    break
            else:
                stack.append(c)


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
import pandas as pd
df=pd.DataFrame([str(solved)])
df.to_clipboard(index=False,header=False)
print("COPIED TO CLIPBOARD")
