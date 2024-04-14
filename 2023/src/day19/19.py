from collections import defaultdict, deque, Counter
from itertools import combinations, combinations_with_replacement, permutations
from functools import reduce, cmp_to_key
import math
# import numpy as np
from operator import add, mul, itemgetter, attrgetter
import os
import re
from sys import argv

def flatten(t):
    return [item for sublist in t for item in sublist]

# Sorts with cmp. cmp < 0 for a < b, == 0 for a==b, > 0 for a > b.
def elpsort(array, cmp):
    return sorted(array, key=cmp_to_key(cmp))

ON_TEXT = '\u2588'
OFF_TEXT = '\u2592'

CHAR_TO_DS = {"^": 3, ">": 1, "<": 0, "v": 2}
DS = [(-1, 0), (1, 0), (0, 1), (0, -1)]
DS8 = DS + [(-1, -1), (1, -1), (-1, 1), (1, 1)]
def arounds(x, y, diagonals):
    ret = []
    for dx, dy in DS8 if diagonals else DS:
        ret.append((x + dx, y + dy))
    return ret

CHALLENGE_DAY = "19"
AOC_DIR = os.path.dirname(argv[0])

print("Day: ", CHALLENGE_DAY)

######################
SAMPLE_EXPECTED = 167409079868000
######################
assert SAMPLE_EXPECTED != None

try:
    SAMPLE = open(os.path.join(AOC_DIR, CHALLENGE_DAY + ".s.txt")).read()
except:
    print("Did you create the sample file?", os.path.join(AOC_DIR, CHALLENGE_DAY + ".s.txt"))

try:
    REAL = open(os.path.join(AOC_DIR, CHALLENGE_DAY + ".txt")).read()
except:
    print("Did you create the solutions file?")


def parse_lines(raw):
    # Groups.
    # groups = raw.split("\n\n")
    # return list(map(lambda group: group.split("\n"), groups))

    ret = {}
    defs, _ = raw.split("\n\n")
    lines = defs.split("\n")
    for l in lines:
        at, nexts = l.split("{")
        nexts = nexts.replace("}", "")
        here = {"conditions": [], "else": None}

        for n in nexts.split(","):
            if ">" in n:
                cond = ">"
            elif "<" in n:
                cond = "<"
            else:
                cond = None
            if cond != None:
                varnum, to = n.split(":")
                var, num = varnum.split(cond)
                num = int(num)
                here["conditions"].append((var, cond, num, to))
            else:
                here["else"] = n
        ret[at] = here

    return ret


def validate_xmas(xmas):
    """Returns a valid xmas object or None if it has become invalid"""
    for c in "xmas":
        if xmas[c][0] > xmas[c][1]:
            return None
    return xmas


def get_all():
    all = {}
    for c in "xmas":
        all[c] = (1, 4000)

    return all


def apply_condition(xmas, condition):
    var, cond, num, _ = condition
    if cond == "<":
        num -= 1
        ### ???
    a = xmas.copy()
    a[var] = (num + 1, a[var][1])
    b = xmas.copy()
    b[var] = (b[var][0], num)

    if cond == ">":
        return (validate_xmas(a), validate_xmas(b))
    else:
        return (validate_xmas(b), validate_xmas(a))

print("AC1", apply_condition(get_all(), ("x", ">", 1000, "A")))
print("AC2", apply_condition(get_all(), ("x", "<", 1000, "A")))


def intersect(a, b):
    ret = {}
    for c in "xmas":
        ac = a[c]
        bc = b[c]
        if bc[0] > ac[1] or ac[0] > bc[1]:
            return None
        ret[c] = (max(ac[0], bc[0]), min(ac[1], bc[1]))
    return ret

def union(a, b):
    intersected = intersect(a, b)
    if intersected == None:
        return [a, b]
    
    

def solve(raw):
    transitions = parse_lines(raw)
    print(transitions)


    ret = 0
    q = deque()
    q.append(("in", get_all()))
    endings = []
    while len(q) > 0:
        name, xmas = q.popleft()
        
        if name == "R":
            continue
        elif name == "A":
            endings.append(xmas)
            
        else:
            here = transitions[name]
            a = xmas
            for cond in here["conditions"]:
                if a == None:
                    break
                [a, b] = apply_condition(a, cond)
                q.append((cond[3], a))
                a = b
            if a != None:
                q.append((here["else"], a))

    print("---------", len(endings))
    print(endings)
    for e in endings:
        here = 1
        for c in "xmas":
            here *= (e[c][1] - e[c][0] + 1)
        print(here, ret)
        ret += here
    return ret

sample = solve(SAMPLE)
if sample != SAMPLE_EXPECTED:
    print("SAMPLE FAILED: ", sample, " != ", SAMPLE_EXPECTED)
assert sample == SAMPLE_EXPECTED
print("\n*** SAMPLE PASSED ***\n")

solved = solve(REAL)
print("SOLUTION: ", solved)