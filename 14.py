from collections import defaultdict, deque, Counter
from itertools import combinations, combinations_with_replacement, permutations
import hashlib
import math
import numpy as np
from operator import add, mul, itemgetter, attrgetter
import re

def flatten(t):
    return [item for sublist in t for item in sublist]

ON_TEXT = '\u2588'
OFF_TEXT = '\u2592'

DAY = "13"
REAL = "cuanljph"

SAMPLE_EXPECTED = 22728

def solve(key, extra_hashes=0):
    md5s = []

    def get_three_fives(key, i):
        h = (key + str(i)).encode()
        h = hashlib.md5(h).hexdigest()

        for _ in range(extra_hashes):
            h = h.encode()
            h = hashlib.md5(h).hexdigest()

        three = None
        fives = []
        for j in range(len(h) - 2):
            if three is None and len(set([h[k] for k in range(j, j + 3)])) == 1:
                three = h[j]
        for j in range(len(h) - 4):
            if len(set([h[k] for k in range(j, j + 5)])) == 1:
                fives.append(h[j])
        if fives:
            assert three in fives
        return (three, fives)
            
    def md5_at(i):
        while i >= len(md5s):
            at = get_three_fives(key, i)
            md5s.append(at)
        return md5s[i]

    i = 0
    valids = []
    while True:
        if len(valids) == 64:
            return valids[-1][0]
        
        three, fives = md5_at(i)
        if three:
            for j in range(i + 1, i + 1 + 1000):
                _, fj = md5_at(j)
                if three in fj:
                    valids.append((i, three, fives))
                    if extra_hashes:
                        print(len(valids), i, three, fives)
                    break
        i += 1
        # print(i)
        

if SAMPLE_EXPECTED != None:
    SAMPLE = "abc"
    sample = solve(SAMPLE)
    if sample != SAMPLE_EXPECTED:
        print("SAMPLE FAILED: ", sample, " != ", SAMPLE_EXPECTED)
    assert sample == SAMPLE_EXPECTED
    print("\n*** SAMPLE PASSED ***\n")
else:
    print("Skipping sample")

part1 = solve(REAL)
print("Part 1: ", part1)

part2 = solve(REAL, 2016)
print("Part 2: ", part2)

try:
    import pandas as pd
    df=pd.DataFrame([str(solved)])
    df.to_clipboard(index=False,header=False)
    print("COPIED TO CLIPBOARD")
except ModuleNotFoundError:
    print("Pandas not installed.")