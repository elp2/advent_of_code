from collections import defaultdict, deque
from itertools import combinations, combinations_with_replacement, permutations
import math
from operator import add, mul, itemgetter, attrgetter
import re

DAY = "4"
REAL = open(DAY + ".in").read()

SAMPLE_EXPECTED = None

def parse_line(line):
    ret = re.findall(r'([a-z-]+)(\d+)\[([a-z]+)', line)
    ret[1] = int(ret[1])

def parse_lines(raw):
    return [parse_line(line) for line in raw.split("\n")]

def solve(raw):
    parsed = parse_lines(raw)
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