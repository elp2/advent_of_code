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

def all_guesses(g_orig, fives, sixes):
    for f in fives:
        assert(len(f)) == 5
    for s in sixes:
        assert(len(s)) == 6
    for fc in permutations(fives, len(fives)):
        for sc in permutations(sixes, len(sixes)):
            guesses = g_orig.copy()
            guesses[0] = sc[0]
            guesses[2] = fc[0]
            guesses[3] = fc[1]
            guesses[5] = fc[2]
            guesses[6] = sc[1]
            guesses[9] = sc[2]

            yield guesses
    

def decode(seen):
    guesses = [None] * 10

    fives = []
    sixes = []
    for s in seen:
        if len(s) == 5:
            fives.append(s)
        elif len(s) == 6:
            sixes.append(s)
        elif len(s) == 2:
            guesses[1] = s
        elif len(s) == 4:
            guesses[4] = s
        elif len(s) == 3:
            guesses[7] = s
        elif len(s) == 7:
            guesses[8] = s
    
    work = []
    for g in all_guesses(guesses, fives, sixes):
        def safe_first(s):
            if len(s) == 0:
                return set(["z"])
            else:
                return set([list(s)[0]])

        for i in range(10):
            assert len(g[i]) == len(LIGHTS[i])

        def valid(g):
            wiring = {}
            wiring["d"] = set(g[8]) - set(g[0])
            wiring["a"] = set(g[7]) - set(g[1])
            wiring["e"] = set(g[8]) - set(g[9])
            wiring["c"] = set(g[1]) - set(g[5])
            wiring["g"] = set(g[5]) - set(g[4]) - set(g[7])
            wiring["b"] = set(g[5]) - set(g[3])
            if len(wiring["c"]) != 1:
                return False
            wiring["f"] = set(g[1]) - wiring["c"]

            all_values = set()
            for v in wiring.values():
                all_values |= v
            if all_values == set(list("abcdefg")) and all([len(v) == 1 for v in wiring.values()]):
                for gi in range(0, 10): #TODO
                    mapped = set()
                    for w in LIGHTS[gi]:
                        mapped |= wiring[w]
                    if set(g[gi]) != mapped:
                        return False

                print(wiring)
                return True
            else:
                return False

        if valid(g):
            work.append(["".join(sorted(list(gx))) for gx in g])

    assert len(work) == 1
    print(work)
    return work[0]

def solve(raw):
    mapping = parse_lines(raw)

    ret = 0
    for k, v in mapping.items():
        wirings = decode(k.split(" "))
        val = 0
        for num in v:
            num = "".join(sorted(list(num)))
            val *= 10
            val += wirings.index(num)
        print(v, val)
        ret += val

    return ret


wirings_test = decode("acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab".split(" "))


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
