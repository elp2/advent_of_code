from collections import defaultdict, deque
from itertools import combinations, combinations_with_replacement, permutations
import math
import numpy as np
from operator import add, mul, itemgetter, attrgetter
import re
def flatten(t):
    return [item for sublist in t for item in sublist]
ON_TEXT = '\u2588'
OFF_TEXT = '\u2592'

DAY = "9"
REAL = open(DAY + ".in").read()

SAMPLE_EXPECTED = None

def solve(raw):
    decompressed_len = 0
    for line in raw.split("\n"):
        dec = ""
        i = 0
        while i < len(line):
            oi = line.find("(", i)
            dec += line[i:oi]
            oe = line.find(")", oi + 1)
            num_chars, num_repeats = map(int, line[oi + 1:oe].split("x"))
            chars = line[oe + 1:oe + 1 + num_chars]
            i = oe + num_chars + 1
            dec += chars * num_repeats

        print(line, "->", dec)
        decompressed_len += len(dec.strip())

    return decompressed_len

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
print("P1: ", solved)

class DecNode:
    def __init__(self, text, multiplier):
        self.children = []
        self.multiplier = multiplier
        i = 0
        while i < len(text):
            parens = text.find("(", i)
            if parens == -1:
                here = text[i:]
                if here:
                    self.children.append(len(here))
                return
            parene = text.find(")", parens + 1)

            self.children.append(len(text[i:parens]))

            num_chars, multiplier = map(int, text[parens + 1:parene].split("x"))

            new_node_text = text[parene + 1:parene + 1 + num_chars]
            self.children.append(DecNode(new_node_text, multiplier))
            i = parene + num_chars + 1

    def declen(self):
        l = 0
        for c in self.children:
            if type(c) == type(0):
                l += c
            else:
                l += c.declen()
        return self.multiplier * l

def part2(raw):
    ret = 0
    for line in raw.split("\n"):
        root = DecNode(line, 1)
        ret += root.declen()
    return ret


assert DecNode("(3x3)XYZ", 1).declen() == 9
assert DecNode("X(8x2)(3x3)ABCY", 1).declen() == len("XABCABCABCABCABCABCY")
assert DecNode("(27x12)(20x12)(13x14)(7x10)(1x12)A", 1).declen() == 241920
assert DecNode("(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN", 1).declen() == 445

print("P2: ", part2(REAL))

try:
    import pandas as pd
    df=pd.DataFrame([str(solved)])
    df.to_clipboard(index=False,header=False)
    print("COPIED TO CLIPBOARD")
except ModuleNotFoundError:
    print("Pandas not installed.")