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

DAY = "13"
REAL = 3012210

SAMPLE_EXPECTED = 3

class Elf:
    def __init__(self, num, np=1):
        self.num = num
        self.presents = np
        self.left = self.right = None

    def grab_left(self):
        if self.left == None:
            print("Winner: ", self.num, self.presents)
        ll = self.left.left
        if ll == self:
            print("Winner: ", self.num, self.presents)
        self.presents += self.left.presents
        ll.right = self
        self.left = ll
        # print(self.left.num, self.right.num)

def solve(nelves):
    elves = []
    for e in range(nelves):
        # 0 1 2 3
        # 0 _ 2 _
        if nelves % 2 == 0:
            if e % 2 == 0:
                elves.append(Elf(e + 1, 2))
        else:
            if e < 2:
                continue
            if e == nelves - 1:
                elves.append(Elf(e + 1, 3))
            elif e % 2 == 0:
                elves.append(Elf(e + 1, 2))

    print("Created Elves")
    for i, e in enumerate(elves):
        # print("Elf: ", e.num, e.presents)
        e.right = elves[i - 1]
        if i == len(elves) - 1:
            e.left = elves[0]
        else:
            e.left = elves[i + 1]
    print("L/R")

    elf = elves[0]
    while True:
        elf.grab_left()
        nelf = elf.left
        if nelf == elf:
            return elf.num
        elf = nelf

if SAMPLE_EXPECTED != None:
    SAMPLE = 5
    sample = solve(SAMPLE)
    if sample != SAMPLE_EXPECTED:
        print("SAMPLE FAILED: ", sample, " != ", SAMPLE_EXPECTED)
    assert sample == SAMPLE_EXPECTED
    print("\n*** SAMPLE PASSED ***\n")
else:
    print("Skipping sample")


def round(elves):
    removed=0
    i = 0
    while i < len(elves):
        e = elves[i]
        if e == None:
            return [elves[(i + j) % len(elves)] for j in range(len(elves)) if elves[(i + j) % len(elves)] != None]
        across = (i + removed + (len(elves) - removed) // 2) % len(elves)
        assert elves[across] != None
        elves[across] = None
        removed+=1
        i+=1

def solve2(num_elves):
    elves = [e + 1 for e in range(num_elves)]
    while len(elves) > 1:
        elves = round(elves)
        print(len(elves))
    print('last elf', elves[0])

solve(5)
solve(REAL)


part1 = solve(REAL)
print("Part 1: ", part1)

part2 = solve2(REAL)
print("Part 2: ", part2)

try:
    import pandas as pd
    df=pd.DataFrame([str(solved)])
    df.to_clipboard(index=False,header=False)
    print("COPIED TO CLIPBOARD")
except ModuleNotFoundError:
    print("Pandas not installed.")