from collections import defaultdict, deque
from itertools import combinations, combinations_with_replacement, permutations
import math
from operator import add, mul, itemgetter, attrgetter
import re

DAY = "6"
REAL = open(DAY + ".in").read()
SAMPLE = open(DAY + ".sample").read()

SAMPLE_EXPECTED = ("easter", "advent")

def parse_line(line):
    return line

def parse_lines(raw):
    return [parse_line(line) for line in raw.split("\n")]

def solve(raw):
    parsed = parse_lines(raw)
    letters = [defaultdict(lambda: 0) for i in range(len(parsed[0]))]
    for row in parsed:
        if not row:
            continue
        for i, l in enumerate(row):
            letters[i][l] += 1
    message = []
    for s in letters:
        rsort = sorted(s.items(), key=itemgetter(1), reverse=True)
        message.append(rsort[0][0])

    part2 = []
    for s in letters:
        rsort = sorted(s.items(), key=itemgetter(1))
        part2.append(rsort[0][0])

    return ("".join(message), "".join(part2))

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