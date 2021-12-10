from collections import defaultdict, deque, Counter
from itertools import combinations, combinations_with_replacement, permutations
import math
# import numpy as np
from operator import add, mul, itemgetter, attrgetter
import re
from typing import DefaultDict

LIGHTS = {0: "abcefg", 1: "cf", 2: "acdeg", 3: "acdfg", 4: "bcdf", 5: "abdfg", 6: "abdefg", 7: "acf", 8: "abcdefg", 9: "abcdfg"}

for k in LIGHTS.keys():
    LIGHTS[k] = set(LIGHTS[k])

LIGHTS_BY_LEN=DefaultDict(lambda: [])
for i in range(10):
    LIGHTS_BY_LEN[len(LIGHTS[i])].append(i)

#   0:      1:      2:      3:      4:
#  aaaa    ....    aaaa    aaaa    ....
# b    c  .    c  .    c  .    c  b    c
# b    c  .    c  .    c  .    c  b    c
#  ....    ....    dddd    dddd    dddd
# e    f  .    f  e    .  .    f  .    f
# e    f  .    f  e    .  .    f  .    f
#  gggg    ....    gggg    gggg    ....

#   5:      6:      7:      8:      9:
#  aaaa    aaaa    aaaa    aaaa    aaaa
# b    .  b    .  .    c  b    c  b    c
# b    .  b    .  .    c  b    c  b    c
#  dddd    dddd    ....    dddd    dddd
# .    f  e    f  .    f  e    f  .    f
# .    f  e    f  .    f  e    f  .    f
#  gggg    gggg    ....    gggg    gggg


CHALLENGE_DAY = "8"
REAL = open(CHALLENGE_DAY + ".txt").read()

SAMPLE_EXPECTED = 61229
if SAMPLE_EXPECTED:
    SAMPLE = open(CHALLENGE_DAY + ".s.txt").read()


def parse_lines(raw):
    ret = {}
    for line in raw.split("\n"):
        mappings, output = line.split(" | ")
        ret[mappings] = output.split(" ")
    return ret


def guess_ordering(actual, ordering, orig_poss):
    poss = orig_poss.copy()
    possible_wiring = [LIGHTS_BY_LEN[len(actual[0])][ordering[i]] for i in range(3)]

    for i in range(len(actual)):
        a = actual[i]
        pw = possible_wiring[i]
        for l in a:
            poss[l] = poss[l].intersection(pw)

    for v in poss.values():
        if len(v) == 0:
            return False
    return poss

def all_guesses(actuals):
    

def decode(seen):
    actual_by_len = DefaultDict(lambda: [])
    for a in seen:
        actual_by_len[len(a)].append(a)

    for guess in all_guesses(actual_by_len):
        poss = {}
        for l in "abcdefg":
            poss[l] = set(l).remove(l)
        for alen, lenguesses in guess.items():
            for l in 



    return poss

def solve(raw):
    mapping = parse_lines(raw)

    ret = 0
    for k, v in mapping.items():
        val = decode(k.split(" "))
        print(k, val)
        ret += val

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
