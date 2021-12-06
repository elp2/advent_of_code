from collections import defaultdict, deque, Counter
from itertools import combinations, combinations_with_replacement, permutations
import math
# import numpy as np
from operator import add, mul, itemgetter, attrgetter
import re
from typing import DefaultDict

CHALLENGE_DAY = "6"
REAL = open(CHALLENGE_DAY + ".txt").read()

SAMPLE_EXPECTED = 26984457539
if SAMPLE_EXPECTED:
    SAMPLE = open(CHALLENGE_DAY + ".s.txt").read()


def parse_lines(raw):
    return [int(f) for f in raw.split(",")]
    # Groups.
    # groups = raw.split("\n\n")
    # return list(map(lambda group: group.split("\n"), groups))
    # lines = raw.split("\n")
    # return lines # raw
    # return list(map(lambda l: l.split(" "), lines)) # words.
    # return list(map(int, lines))
    # return list(map(lambda l: l.strip(), lines)) # beware leading / trailing WS

def solve(raw):
    parsed = parse_lines(raw)
    # Debug here to make sure parsing is good.
    ret = 0

    fish = parsed

    pregnant = DefaultDict(lambda: 0)
    for f in fish:
        pregnant[f] += 1
    for d in range(256):
        new_pregnant = DefaultDict(lambda: 0)
        for k in pregnant.keys():
            curr = pregnant[k]
            k -= 1
            if k < 0:
                new_pregnant[6] += curr
                new_pregnant[8] += curr
            else:
                new_pregnant[k] += curr

        pregnant = new_pregnant

    return sum(pregnant.values())

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
