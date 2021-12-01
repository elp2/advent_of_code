from collections import defaultdict, deque, Counter
from itertools import combinations, combinations_with_replacement, permutations
import math
import numpy as np
from operator import add, mul, itemgetter, attrgetter
import re

def flatten(t):
    return [item for sublist in t for item in sublist]

ON_TEXT = '\u2588'
OFF_TEXT = '\u2592'


SAMPLE_EXPECTED = "01100"

def expand(e):
    ret = e + "0"
    ex = e[::-1]
    ex = ex.replace("0", "o")
    ex = ex.replace("1", "0")
    ex = ex.replace("o", "1")
    return ret + ex

def solve(raw):
    data, dlen = raw
    while len(data) < dlen:
        # print(data)
        data = expand(data)

    data = data[:dlen]
    while len(data) % 2 == 0:
        # print(data)
        dn = ""
        for i in range(0, len(data), 2):
            dh = data[i:i+2]
            if dh[0] == dh[1]:
                dn += "1"
            else:
                dn += "0"
        data = dn

    return data

if SAMPLE_EXPECTED != None:
    sample = solve(("10000", 20))
    if sample != SAMPLE_EXPECTED:
        print("SAMPLE FAILED: ", sample, " != ", SAMPLE_EXPECTED)
    assert sample == SAMPLE_EXPECTED
    print("\n*** SAMPLE PASSED ***\n")
else:
    print("Skipping sample")

part1 = solve(("01110110101001000", 272))
print("Part 1: ", part1)

part2 = solve(("01110110101001000", 35651584))
print("Part 2: ", part2)

try:
    import pandas as pd
    df=pd.DataFrame([str(solved)])
    df.to_clipboard(index=False,header=False)
    print("COPIED TO CLIPBOARD")
except ModuleNotFoundError:
    print("Pandas not installed.")