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

DAY = "23"
REAL = open(DAY + ".in").read()

SAMPLE_EXPECTED = 3

# cpy x y copies x (either an integer or the value of a register) into register y.
# inc x increases the value of register x by one.
# dec x decreases the value of register x by one.
# jnz x y jumps to an instruction y away (positive means forward; negative means backward), but only if x is not zero.
# tgl x toggles the instruction x away (pointing at instructions like jnz does: positive means forward; negative means backward):

def solve(raw, a=0):
    regs = {'a': a}
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

    toggles = [0] * len(lines)
    while True:
        iteratitions += 1
        if pc >= len(lines):
            break
        # print(pc, toggles[pc], lines[pc], regs)
        ats[pc] += 1
        offset = 1
        s = lines[pc].split(" ")
        toggled = toggles[pc] != 0
        oper = s[0]
        if toggled:
            if oper in ["inc"]:
                oper = "dec"
            elif oper in ["dec", "tgl"]:
                oper = "inc"
            elif oper in ["jnz"]:
                oper = "cpy"
            elif oper in ["cpy"]:
                oper = "jnz"
            else:
                print(oper)
                assert False
        if oper == "cpy":
            src = s[1]
            dest = s[2]
            if not dest.isnumeric():
                regs[dest] = get_val(src)
        elif oper == "inc":
            dest = s[1]
            if not dest.isnumeric():
                regs[dest] += 1
        elif oper == "dec":
            dest = s[1]
            if not dest.isnumeric():
                regs[dest] -= 1
        elif oper == "jnz":
            if get_val(s[1]) != 0:
                offset = get_val(s[2])
        elif oper == "tgl":
            delta = get_val(s[1])
            if 0 <= delta + pc < len(lines):
                toggles[delta + pc] = iteratitions
        else:
            assert False
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

solved = solve(REAL, 7)
print("Part 1: ", solved)

try:
    import pandas as pd
    df=pd.DataFrame([str(solved)])
    df.to_clipboard(index=False,header=False)
    print("COPIED TO CLIPBOARD")
except ModuleNotFoundError:
    print("Pandas not installed.")