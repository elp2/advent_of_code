from collections import defaultdict, deque, Counter
from itertools import combinations, combinations_with_replacement, permutations
import math
# import numpy as np
from operator import add, mul, itemgetter, attrgetter
import re
from typing import Deque

CHALLENGE_DAY = "10"
REAL = open(CHALLENGE_DAY + ".txt").read()

SAMPLE_EXPECTED = 288957
if SAMPLE_EXPECTED:
    SAMPLE = open(CHALLENGE_DAY + ".s.txt").read()

ILLEGAL = {")": 3, "]": 57, "}": 1197, ">": 25137}
GOOD = {")": 1, "]": 2, "}": 3, ">": 4}

CLOSERS = {"(": ")", "[": "]", "{": "}", "<": ">"}
CLOSER_EXPECTED = {}
for k, v in CLOSERS.items():
    CLOSER_EXPECTED[v] = k

def parse_lines(raw):
    lines = raw.split("\n")
    return lines # raw

def solve(raw):
    parsed = parse_lines(raw)

    scores = []
    for line in parsed:
        stack = Deque()
        incomplete = True
        for c in line:
            if c in CLOSERS.values():
                top = stack.pop()
                expected = CLOSER_EXPECTED[c]
                if expected != top:
                    print(c, expected)
                    incomplete = False
                    break
            else:
                stack.append(c)
        if not incomplete:
            continue
        print(line, "incomplete")
        score = 0
        while len(stack) != 0:
            score *= 5
            here = stack.pop()
            score += GOOD[CLOSERS[here]]
        scores.append(score)

    scores = sorted(scores)
    return scores[int(len(scores) / 2)]

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
