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

DAY = "12"
REAL = open(DAY + ".in").read()

SAMPLE_EXPECTED = 42

# cpy x y copies x (either an integer or the value of a register) into register y.
# inc x increases the value of register x by one.
# dec x decreases the value of register x by one.
# jnz x y jumps to an instruction y away (positive means forward; negative means backward), but only if x is not zero.




def solve(raw, c=0):
    regs = {'c': c}
    lines = raw.split("\n")
    pc = 0

    ats = Counter()
    iteratitions = 0


    def get_val(src):
        try:
            return int(src)
        except ValueError:
            if src in regs:
                return regs[src]
            else:
                return 0

    while True:
        iteratitions += 1
        if iteratitions == 10000:
            for z in [10, 11, 12]:
                print(z, lines[z])
            print(ats.most_common(5))
        if pc >= len(lines):
            break
        ats[pc] += 1
        offset = 1
        s = lines[pc].split(" ")
        if pc == 10:
            regs["a"] += regs["b"]
            regs["b"] = 0
            pc = 13
            continue
        if s[0] == "cpy":
            src = s[1]
            regs[s[2]] = get_val(src)
        elif s[0] == "inc":
            regs[s[1]] += 1
        elif s[0] == "dec":
            regs[s[1]] -= 1
        elif s[0] == "jnz":
            if get_val(s[1]) != 0:
                offset = get_val(s[2])
        pc += offset

    return regs['a']

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
print("Part 1: ", solved)

solved = solve(REAL, 1)
print("Part 2: ", solved)

try:
    import pandas as pd
    df=pd.DataFrame([str(solved)])
    df.to_clipboard(index=False,header=False)
    print("COPIED TO CLIPBOARD")
except ModuleNotFoundError:
    print("Pandas not installed.")