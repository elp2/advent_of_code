from collections import defaultdict, deque, Counter
from itertools import combinations, combinations_with_replacement, permutations
from functools import reduce
import math
# import numpy as np
from operator import add, mul, itemgetter, attrgetter
import re

DS = [[-1, 0], [1, 0], [0, 1], [0, -1]]
DS8 = DS + [[-1, -1], [1, -1], [-1, 1], [1, 1]]
def arounds_inside(x, y, diagonals, w, h):
    ret = []
    for dx, dy in DS8 if diagonals else DS:
        ret.append((x + dx, y + dy))


CHALLENGE_DAY = "21"
REAL = open(CHALLENGE_DAY + ".txt").read()

SAMPLE_EXPECTED = 152
if SAMPLE_EXPECTED:
    SAMPLE = open(CHALLENGE_DAY + ".s.txt").read()


def parse_lines(raw):
    # Groups.
    # groups = raw.split("\n\n")
    # return list(map(lambda group: group.split("\n"), groups))

    ret = {}
    lines = raw.split("\n")
    for l in lines:
        word, func = l.split(": ")
        ret[word] = func
    return ret

def inty(val):
    try:
        i = int(val)
        return True
    except:
        return False

def solve(raw):
    monkeys = parse_lines(raw)

    while not inty(monkeys["root"]):
        for m, exp in monkeys.items():
            if inty(exp):
                continue
            if " " in exp:
                ak, op, bk = exp.split(" ")
                if not inty(monkeys[ak]) or not inty(monkeys[bk]):
                    continue
                a = int(monkeys[ak])
                b = int(monkeys[bk])
                if op == "*":
                    val = a * b
                elif op == "+":
                    val = a + b
                elif op == "-":
                    val = a - b
                elif op == "/":
                    val = a // b
                else:
                    assert False
                monkeys[m] = val
            

    # Debug here to make sure parsing is good.
    ret = 0

    return monkeys["root"]

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
