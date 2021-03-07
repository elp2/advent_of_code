from collections import defaultdict, deque
from itertools import permutations
import re

CHALLENGE_DAY = "9"
REAL = open(CHALLENGE_DAY + ".txt").read()
SAMPLE = open(CHALLENGE_DAY + ".sample.txt").read()
SAMPLE_EXPECTED = 605

def parse_lines(raw):
    lines = raw.split("\n")
    distances = {}
    cities = set()
    for line in lines:
        a, _, b, _, d = line.split(" ")
        d = int(d)
        distances[(a, b)] = d
        distances[(b, a)] = d
        cities.add(a)
        cities.add(b)
    
    return distances, cities

def solve(raw):
    distances, cities = parse_lines(raw)

    keys = list(cities)
    perms = permutations(keys)

    lowest = None
    highest = None
    for perm in perms:
        here = 0
        at = None
        has_path = True
        for loc in perm:
            if at == None:
                at = loc
            else:
                to = loc
                if (at, to) in distances:
                    here += distances[(at, to)]
                else:
                    has_path = False
                    break
                at = to
        if not has_path:
            continue
        if not lowest or here < lowest:
            lowest = here
        if not highest or here > highest:
            highest = here
    print(lowest, highest)
    return lowest

sample = solve(SAMPLE)
if sample != SAMPLE_EXPECTED:
    print("SAMPLE FAILED: ", sample, " != ", SAMPLE_EXPECTED)
assert sample == SAMPLE_EXPECTED
print("\n*** SAMPLE PASSED ***\n")

solved = solve(REAL)
print("SOLUTION: ", solved)
import pandas as pd
df=pd.DataFrame([str(solved)])
df.to_clipboard(index=False,header=False)
print("COPIED TO CLIPBOARD")
