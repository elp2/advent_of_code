from collections import defaultdict, deque, Counter
from itertools import combinations, combinations_with_replacement, permutations
from functools import reduce
import math
# import numpy as np
from operator import add, mul, itemgetter, attrgetter
import re
from dataclasses import dataclass

DS = [[-1, 0], [1, 0], [0, 1], [0, -1]]
DS8 = DS + [[-1, -1], [1, -1], [-1, 1], [1, 1]]
def arounds_inside(x, y, diagonals, w, h):
    ret = []
    for dx, dy in DS8 if diagonals else DS:
        ret.append((x + dx, y + dy))


CHALLENGE_DAY = "20"
REAL = open(CHALLENGE_DAY + ".txt").read()

SAMPLE_EXPECTED = 1623178306
if SAMPLE_EXPECTED:
    SAMPLE = open(CHALLENGE_DAY + ".s.txt").read()


class CodeNumber:
    next: any
    prev: any
    num: int


DEBUG=False
PRINT=False

def parse_lines(raw):
    lines = raw.split("\n")
    nums = list(map(lambda x: 811589153 * int(x), lines))
    ret = []

    prev = None
    for n in nums:
        c = CodeNumber()
        c.num = n 
        c.prev = prev
        if prev:
            c.prev.next = c
        prev = c
        ret.append(c)
    ret[0].prev = ret[-1]
    ret[-1].next = ret[0]

    return ret


def solve(raw):
    parsed = parse_lines(raw)

    def print_state(desc):
        if not DEBUG:
            return
        if PRINT:
            print("---- ", desc)

        printed = 0
        here = parsed[0]
        should_print = True
        for i in range(len(parsed) + 2):
            if PRINT and should_print:
                print(here.num)
            hprev = here
            here = here.next
            assert here.prev == hprev
            printed += 1
            if here == parsed[0]:
                assert printed == len(parsed)
                should_print = False

    def move_piece(c):
        spaces = c.num
        if spaces < 0:
            spaces = spaces % (len(parsed) - 1)
        else:
            spaces = spaces % (len(parsed) - 1)
        while spaces != 0:
            if spaces < 0:
                cnext = c.next
                cprev = c.prev

                c.prev = cprev.prev
                c.prev.next = c
                c.next = cprev

                cprev.prev = c
                cprev.next = cnext

                cnext.prev = cprev

                spaces += 1

            elif spaces > 0:
                cnext = c.next
                cprev = c.prev

                c.next = cnext.next
                c.next.prev = c
                c.prev = cnext

                cnext.next = c
                cnext.prev = cprev

                # cprev.prev
                cprev.next = cnext

                spaces -= 1
        
    for mix in range(10):
        print("Mix round ", mix)
        for c in parsed:
            print_state("Before: " + str(c.num))

            move_piece(c)

            print_state("After: " + str(c.num))

    for zero in parsed:
        if zero.num == 0:
            break
    
    rets = []
    for i in range(3):
        for a in range(1000):
            zero = zero.next
        rets.append(zero.num)
    return sum(rets)

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
