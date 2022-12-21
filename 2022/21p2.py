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

SAMPLE_EXPECTED = 301
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
    monkeys["humn"] = "humn"

    def expify(exp, mult=1):
        if inty(exp):
            return str(exp)
        if "humn" == exp:
            return "x"
        if " " not in exp:
            return "(" + str(expify(monkeys[exp])) + ")"
        a, op, b = exp.split(" ")
        av = expify(monkeys[a])
        bv = expify(monkeys[b])
        if False: #inty(av) and inty(bv):
            v = int(eval(str(av) + op + str(bv)))
        else:
            v =  "(" + str(av) + op + str(bv) + ")"
        return v

    a, _, b = monkeys["root"].split(" ")
    ea = expify(a)
    eb = expify(b)

    
    if "x" in ea:
        print(ea)
        constant = eval(eb)
        var = ea
    else:
        print(eb)
        constant = eval(ea)
        var = eb

    def simplify(exp):
        here = ""
        for i in range(len(exp)):
            c = exp[i]
            if "(" == c:
                for j in range(i + 1, len(exp)):
                    if exp[j] == "(":
                        break
                    if exp[j] == ")":
                        inside = exp[i:j]
                        if "x" in inside:
                            here += inside
                        else:
                            here += str(eval(inside))
                        i = j
                        break
                
            else:
                here += c
        return here

    # print(var, simplify(var))

    at = 0
    i = 0

    x = 0
    zero = eval(var) - constant
    x = 1000
    onek = eval(var) - constant
    m = float(onek - zero) / 1000
    b = zero
    y = constant
    x = (y-b) / m
    around = 3759560018017 + 29235750 // 5
    x = int(around)
    while True:
        if x % 1000 == 0:
            print(abs(e - constant), x)

        e = eval(var)
        if e == constant:
            return x
        if e - constant > 10000:
            x += 50
        x += 1


# if SAMPLE_EXPECTED != None:
#     sample = solve(SAMPLE)
#     if sample != SAMPLE_EXPECTED:
#         print("SAMPLE FAILED: ", sample, " != ", SAMPLE_EXPECTED)
#     assert sample == SAMPLE_EXPECTED
#     print("\n*** SAMPLE PASSED ***\n")
# else:
#     print("Skipping sample")

solved = solve(REAL)
print("SOLUTION: ", solved)
