from collections import defaultdict, deque, Counter
from itertools import combinations, combinations_with_replacement, permutations
from functools import reduce
import math
import numpy as np
from operator import add, mul, itemgetter, attrgetter
import re

DS = [[-1, 0], [1, 0], [0, 1], [0, -1]]
DS8 = DS + [[-1, -1], [1, -1], [-1, 1], [1, 1]]
def arounds_inside(x, y, diagonals, w, h):
    ret = []
    for dx, dy in DS8 if diagonals else DS:
        ret.append((x + dx, y + dy))


CHALLENGE_DAY = "13"
REAL = open(CHALLENGE_DAY + ".txt").read()

SAMPLE_EXPECTED = 13
if SAMPLE_EXPECTED:
    SAMPLE = open(CHALLENGE_DAY + ".s.txt").read()

def inty(i):
    try:
        i = int(i)
        return True
    except:
        return False

def parse_lines(raw):
    # Groups.
    groups = raw.split("\n\n")
    # return list(map(lambda group: group.split("\n"), groups))
    # lines = raw.split("\n")
    # return lines # raw
    # return list(map(lambda l: l.split(" "), lines)) # words.
    # return list(map(int, lines))
    # return list(map(lambda l: l.strip(), lines)) # beware leading / trailing WS
    return groups

def tokenized(p):
    p = p.replace("[", " [ ")
    p = p.replace("]", " ] ")
    p = p.replace(",", " ")

    l = [int(z) if inty(z) else z for z in p.split(" ") if z != ""]

    return deque(l)

def get_ordering(a, b):
    a = tokenized(a)
    b = tokenized(b)

    while len(a):
        l = a.popleft()
        if not len(b):
            return False
        r = b.popleft()

        if inty(l) and inty(r):
            if l < r:
                return True
            elif l > r:
                return False
        elif not inty(l) and not inty(r):
            if l == "]":
                if r == "]":
                    continue
                elif r == "[":
                    return True
            elif l == "[":
                if r == "[":
                    continue
                elif r == "]":
                    return False
            else:
                assert False
        elif inty(l) and not inty(r):
            if r == "[":
                a.appendleft("]")
                a.appendleft(l)
            else:
                return False
        elif not inty(l) and inty(r):
            if l == "[":
                b.appendleft("]")
                b.appendleft(r)
            else:
                return True
        else:
            assert False
    print("Fallthrough!")
    return True

def solve(raw):
    ordered = []
    groups = parse_lines(raw)
    for gi, g in enumerate(groups):
        a, b= g.split("\n")
        print(g)
        if gi == 7:
            print("7")
        o = get_ordering(a, b)
        if o:
            ordered.append(gi + 1)
        print(o, "\n----------------------")

    print(set(ordered) - set([1,2,4,6]))
    return sum(ordered)

if SAMPLE_EXPECTED != None:
    sample = solve(SAMPLE)
    if sample != SAMPLE_EXPECTED:
        print("SAMPLE FAILED: ", sample, " != ", SAMPLE_EXPECTED)
    assert sample == SAMPLE_EXPECTED
    print("\n*** SAMPLE PASSED ***\n")
else:
    print("Skipping sample")

solved = solve(REAL)
assert solved > 6353
print("SOLUTION: ", solved)
