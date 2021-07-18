from collections import defaultdict, deque
from itertools import combinations, combinations_with_replacement, permutations
import math
import numpy as np
from operator import add, mul, itemgetter, attrgetter
import re
def flatten(t):
    return [item for sublist in t for item in sublist]
ON_TEXT = '\u2588'
OFF_TEXT = '\u2592'

DAY = "11"
REAL = open(DAY + ".in").read()

SAMPLE_EXPECTED = None

def solve(raw):
    ret = 0

    return ret

if SAMPLE_EXPECTED != None:
    SAMPLE = open(DAY + ".sample").read()
    sample = solve(SAMPLE)
    if sample != SAMPLE_EXPECTED:
        print("SAMPLE FAILED: ", sample, " != ", SAMPLE_EXPECTED)
    assert sample == SAMPLE_EXPECTED
    print("\n*** SAMPLE PASSED ***\n")
else:
    print("Skipping sample")

solved = solve(REAL)
print("SOLUTION: ", solved)

try:
    import pandas as pd
    df=pd.DataFrame([str(solved)])
    df.to_clipboard(index=False,header=False)
    print("COPIED TO CLIPBOARD")
except ModuleNotFoundError:
    print("Pandas not installed.")