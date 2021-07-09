from collections import defaultdict, deque
from itertools import combinations
from functools import reduce
from operator import add, mul

import re

CHALLENGE_DAY = "24"
REAL = open(CHALLENGE_DAY + ".txt").read()
SAMPLE = open(CHALLENGE_DAY + ".sample.txt").read()
SAMPLE_EXPECTED = 99

def parse_lines(raw):
    lines = raw.split("\n")
    return list(map(int, lines))

def quantum_entanglement(arr):
    return reduce(mul, arr)

def solve(raw, num_compartments):
    parsed = parse_lines(raw)

    target = sum(parsed) // num_compartments
    for smallest_size in range(len(parsed)):
        print(smallest_size)
        poss = [g for g in combinations(parsed, smallest_size) if sum(g) == target]
        if len(poss):
            qes = map(quantum_entanglement, poss)
            return min(qes)

    assert False

sample = solve(SAMPLE, 3)
if sample != SAMPLE_EXPECTED:
    print("SAMPLE FAILED: ", sample, " != ", SAMPLE_EXPECTED)
assert sample == SAMPLE_EXPECTED
print("\n*** SAMPLE PASSED ***\n")

solved = solve(REAL, 3)
print("Part1: ", solved) # 405925792351 high - max not min d'oh. # 11846773891

solved = solve(REAL, 4)
print("Part2: ", solved) # 405925792351 high - max not min d'oh. # 11846773891
