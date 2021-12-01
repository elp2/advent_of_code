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

DAY = "18"
REAL = "^^^^......^...^..^....^^^.^^^.^.^^^^^^..^...^^...^^^.^^....^..^^^.^.^^...^.^...^^.^^^.^^^^.^^.^..^.^"

SAMPLE_EXPECTED = 38

def solve(row, num_rows):
    num_traps = 0
    num_traps += row.count(".")
    rows = [row]
    while len(rows) != num_rows:
        prow = "." + rows[-1] + "."
        row = ""
        for i in range(len(rows[0])):
            check = prow[i:i+3]
            traps = ["^^.", ".^^", "^..", "..^"]
            if check in traps:
                row = row + "^"
            else:
                row = row + "."
        num_traps += row.count(".")
        rows.append(row)
        assert len(rows[-1]) == len(rows[-2])
    
    return num_traps


    return ret

if SAMPLE_EXPECTED != None:
    SAMPLE = ".^^.^.^^^^"
    sample = solve(SAMPLE, 10)
    if sample != SAMPLE_EXPECTED:
        print("SAMPLE FAILED: ", sample, " != ", SAMPLE_EXPECTED)
    assert sample == SAMPLE_EXPECTED
    print("\n*** SAMPLE PASSED ***\n")
else:
    print("Skipping sample")

part1 = solve(REAL, 40)
print("Part 1: ", part1)

part2 = solve(REAL, 400000)
print("Part 2: ", part2)

try:
    import pandas as pd
    df=pd.DataFrame([str(solved)])
    df.to_clipboard(index=False,header=False)
    print("COPIED TO CLIPBOARD")
except ModuleNotFoundError:
    print("Pandas not installed.")
