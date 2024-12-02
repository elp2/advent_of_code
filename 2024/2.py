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

LEFT = 0
UP = 1
RIGHT = 2
DOWN = 3
CHAR_TO_DS = {"^": UP, ">": RIGHT, "<": LEFT, "v": DOWN}
DS = [(-1, 0), (0, -1), (1, 0), (0, 1)]
DS8 = DS + [(-1, -1), (1, -1), (-1, 1), (1, 1)]

def arounds(x, y, diagonals):
    ret = []
    for dx, dy in DS8 if diagonals else DS:
        ret.append((x + dx, y + dy))
    return ret

CHALLENGE_DAY = argv[0].split("/")[-1].replace(".py", "").replace("p2.py", "")
AOC_DIR = os.path.dirname(argv[0])

print("Day: ", CHALLENGE_DAY)

######################
SAMPLE_EXPECTED = 4
######################
assert SAMPLE_EXPECTED != None

try:
    SAMPLE = open(os.path.join(AOC_DIR, CHALLENGE_DAY + ".s.txt")).read()
except:
    print("Did you create the sample file?")

try:
    REAL = open(os.path.join(AOC_DIR, CHALLENGE_DAY + ".txt")).read()
except:
    print("Did you create the solutions file?")


def parse_lines(raw):
    # Groups.
    # groups = raw.split("\n\n")
    # return list(map(lambda group: group.split("\n"), groups))
    lines = raw.split("\n")
    ret = []
    for l in lines:
        rl = []
        for n in l.split(" "):
            rl.append(int(n))
        ret.append(rl)

    return ret # raw
    # return list(map(lambda l: l.split(" "), lines)) # words.
    # return list(map(int, lines))
    # return list(map(lambda l: l.strip(), lines)) # beware leading / trailing WS


def solve(raw):
    parsed = parse_lines(raw)
    print(parsed)

    ret = 0

    results = {}

    for rorig in parsed:
        results[str(rorig)] = False

    for rorig in parsed:
        for roi in range(len(rorig)):
            report = rorig[:]
            report.pop(roi)
            diffs = []
            valid = True
            incordec = None
            for di in range(1, len(report)):
                diff = report[di] - report[di - 1]
                diffs.append(diff)
                if 1 <= abs(diff) <= 3:
                    valid = True
                else:
                    print("diffoff", diff)
                    valid = False
                    break
                if incordec == None:
                    incordec = diff
                else:
                    sameinc = (incordec < 0 and diff < 0) or (incordec > 0 and diff > 0)
                    print("notsame?", incordec, diff, sameinc)
                    valid = valid and sameinc
                    if not valid:
                        break
            
            print(report, diffs, valid)
            if valid:
                ret += 1
                results[str(rorig)] = True
                break
        
        print("------")
        report = rorig[:]
        def stepvalid(rep, i, i2, ab):
            if i2 >= len(rep):
                return True
            diff = report[i] - report[i2]
            if (diff < 0 and ab > 0) or (diff > 0 and ab < 0):
                print("toolarge skip", diff, ab)
                return False
            
            if 1 <= abs(diff) <= 3:
                return True
            else:
                return False

        def valid(rep):
            skipped = False
            ab = rep[0] - rep[1]
            i = 0

            if ab == 0:
                ab = rep[1] - rep[2]
                if ab == 0:
                    return False
                skipped = True
            while i < len(report):
                if stepvalid(rep, i, i + 1, ab):
                    i += 1
                else:
                    if skipped:
                        return False
                    if stepvalid(rep, i, i + 2, ab):
                        skipped = True
                        i += 2
                    else:
                        print("Second chance no", i)
                        return False
            return True
        
        wouldadd = False
        print(report)
        if valid(report):
            print("forwards valid")
            wouldadd = True
        else:
            report.reverse()
            print("round2 ", report)
            if valid(report):
                wouldadd = True
                print("reverse valid")
            report.reverse()

        if wouldadd != results[str(report)]:
            print("wa!=", wouldadd, report)
        # print(ret)
        print("------")

    return ret

sample = solve(SAMPLE)
if sample != SAMPLE_EXPECTED:
    print("SAMPLE FAILED: ", sample, " != ", SAMPLE_EXPECTED)
assert sample == SAMPLE_EXPECTED
print("\n*** SAMPLE PASSED ***\n")

solved = solve(REAL)
assert solved not in [576]
print("SOLUTION: ", solved)
