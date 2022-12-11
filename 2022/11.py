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


CHALLENGE_DAY = "11"
REAL = open(CHALLENGE_DAY + ".txt").read()

SAMPLE_EXPECTED = 10605
if SAMPLE_EXPECTED:
    SAMPLE = open(CHALLENGE_DAY + ".s.txt").read()


# addx V takes two cycles to complete. After two cycles, the X register is increased by the value V. (V can be negative.)
# noop takes one cycle to complete. It has no other effect.

MNAME="NAME"
ITEMS="items"
OPERATION="operation"
TEST="test"
MTRUE="mtrue"
MFALSE="mfalse"
MINSPECTS="inspects"
MDIVISIBLE="MDIVISIBLE"

def parse_lines(raw):
    # Groups.
    monkeys = []
    groups = raw.split("\n\n")
    for mt in groups:
        ml = mt.split("\n")
        # Monkey 2:
        #   Starting items: 79, 60, 97
        #   Operation: new = old * old
        #   Test: divisible by 13
        #     If true: throw to monkey 1
        #     If false: throw to monkey 3

        monkey = {}
        monkey[MNAME] = ml[0]
        monkey[MINSPECTS] = 0
        items = ml[1].split(": ")[1].split(", ")
        items = deque(list(map(int, items)))
        monkey[ITEMS] = items
        monkey[OPERATION] = ml[2].split( " = ")[1]
        monkey[MDIVISIBLE] = int(ml[3].split(" ")[5])
        monkey[MTRUE] = int(ml[-2].split(" ")[-1])
        monkey[MFALSE] = int(ml[-1].split(" ")[-1])

        print(monkey)
        monkeys.append(monkey)
    return monkeys


def solve(raw):
    monkeys = parse_lines(raw)

    for round in range(20):
        for m in monkeys:
            while True:
                if not len(m[ITEMS]):
                    break
                m[MINSPECTS] += 1
                old = m[ITEMS].popleft()
#   Monkey inspects an item with a worry level of 79.
#     Worry level is multiplied by 19 to 1501.
                item = eval(m[OPERATION])
                item = item // 3
                if item % m[MDIVISIBLE] == 0:
                    monkeys[m[MTRUE]][ITEMS].append(item)
                else:
                    monkeys[m[MFALSE]][ITEMS].append(item)


#     Monkey gets bored with item. Worry level is divided by 3 to 500.
#     Current worry level is not divisible by 23.
#     Item with worry level 500 is thrown to monkey 3.
    print(monkeys)
    inspects = map(lambda m: m[MINSPECTS], monkeys)
    si = sorted(inspects)
    return si[-1] * si[-2]





if SAMPLE_EXPECTED != None:
    sample = solve(SAMPLE)
    if sample != SAMPLE_EXPECTED:
        print("SAMPLE FAILED: ", sample, " != ", SAMPLE_EXPECTED)
    assert sample == SAMPLE_EXPECTED
    print("\n*** SAMPLE PASSED ***\n")
else:
    print("Skipping sample")

solved = solve(REAL)
print("SOLUTION: ", solved) # not 1870
