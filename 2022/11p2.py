from collections import defaultdict, deque, Counter
from dataclasses import dataclass
from itertools import combinations, combinations_with_replacement, permutations
from functools import reduce
import math
# import numpy as np
from operator import add, mul, itemgetter, attrgetter
import re
from typing import List

DS = [[-1, 0], [1, 0], [0, 1], [0, -1]]
DS8 = DS + [[-1, -1], [1, -1], [-1, 1], [1, 1]]
def arounds_inside(x, y, diagonals, w, h):
    ret = []
    for dx, dy in DS8 if diagonals else DS:
        ret.append((x + dx, y + dy))


CHALLENGE_DAY = "11"
REAL = open(CHALLENGE_DAY + ".txt").read()

SAMPLE_EXPECTED = 2713310158
if SAMPLE_EXPECTED:
    SAMPLE = open(CHALLENGE_DAY + ".s.txt").read()


@dataclass
class Monkey:
    name: str
    items: deque[int]
    operation: str
    true_monkey: int
    false_monkey: int
    divisible: int
    num_inspects: int = 0

    def __init__(self, s):
        s = s.split("\n")
#Monkey 1:
        self.name = s[0]
#   Starting items: 76, 62, 61, 54, 69, 60, 85
        self.items = deque(map(int, re.findall(r"[0-9]+", s[1])))
#   Operation: new = old + 1
        self.operation = s[2].split(" = ")[1]
#   Test: divisible by 17
        self.divisible = int(s[3].split(" ")[-1])
#     If true: throw to monkey 0
        self.true_monkey = int(s[4].split(" ")[-1])
#     If false: throw to monkey 6
        self.false_monkey = int(s[5].split(" ")[-1])

    def turn(self, reducer):
        if not len(self.items):
            return None
        self.num_inspects += 1
        item = self.items.popleft()
        old = item % reducer
        item = eval(self.operation)

        if item % self.divisible == 0:
            return(self.true_monkey, item)
        else:
            return(self.false_monkey, item)


def parse_lines(raw):
    # Groups.
    monkeys = []
    groups = raw.split("\n\n")
    for mt in groups:
        monkey = Monkey(mt)
        print(monkey)
        monkeys.append(monkey)
    return monkeys


def solve(raw):
    monkeys = parse_lines(raw)
    mods = map(lambda m: m.divisible, monkeys)
    reducer = reduce(mul, mods)
    for round in range(10000):        
        if round % 100 == 0:
            print(round)
        for m in monkeys:
            while True:
                turn = m.turn(reducer)
                if turn:
                    recipient, item = turn
                    monkeys[recipient].items.append(item)
                else:
                    break


#     Monkey gets bored with item. Worry level is divided by 3 to 500.
#     Current worry level is not divisible by 23.
#     Item with worry level 500 is thrown to monkey 3.
    print(monkeys)
    inspects = map(lambda m: m.num_inspects, monkeys)
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
