from collections import defaultdict, deque, Counter
from itertools import combinations, combinations_with_replacement, permutations, product
from functools import reduce, cmp_to_key
from operator import add, mul, itemgetter, attrgetter
import os
from parse import parse
import sys

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, root_dir)
from aoc_elp import *

######################
SAMPLE_EXPECTED = 2024
######################
assert SAMPLE_EXPECTED != None, "Must enter sample value"

def parse_group(group):
    lines = group.split("\n")
    ret = []
    for y, line in enumerate(lines):
        line = line.strip()
        assert len(line) != 0

        split = line.split(" ")

        for x, xc in enumerate(split):
            pass

        assert len(split) != 0
        ret.append(split)

    return ret


def parse_lines(raw):
    initialsstr, gatesstr = raw.split("\n\n")
    namevals = {}
    for line in initialsstr.split("\n"):
        name, val = line.split(": ")
        namevals[name] = 1 if val == "1" else 0
    
    gates = []
    for line in gatesstr.split("\n"):
        # qgv OR dsf -> mjm
        a, op, b, _, to = line.split(" ")
        gates.append((a, op, b, to))

    return namevals, gates


def solve(raw):
    namevals, gates = parse_lines(raw)

    while gates:
        for gi, (a, op, b, to) in enumerate(gates):
            if a in namevals and b in namevals:
                av, bv = namevals[a], namevals[b]
                gates[gi] = None
                if op == "AND":
                    val = av and bv
                elif op == "OR":
                    val = av or bv
                elif op == "XOR":
                    val = av ^ bv
                else:
                    assert False
                print(a, av, op, b, bv, to, val)
                namevals[to] = val  
        gates = [g for g in gates if g]

    binary = []
    for i in range(100):
        if f"z{i:02d}" in namevals:
            v = 1 if namevals[f"z{i:02d}"] else 0
            binary.append(v)
            print(f"z{i:02d}", v)
    binary.reverse()
    ret = int("".join([str(bb) for bb in binary]), 2)
    return ret

if __name__ == "__main__":
    SAMPLE, REAL = get_raw_inputs(sys.argv)

    S2 = """x00: 1
x01: 1
x02: 1
y00: 0
y01: 1
y02: 0

x00 AND y00 -> z00
x01 XOR y01 -> z01
x02 OR y02 -> z02"""
    s2 = solve(S2)
    assert s2 == 4

    sample = solve(SAMPLE)
    assert sample == SAMPLE_EXPECTED, "Sample Result %s != %s expected" % (sample, SAMPLE_EXPECTED)
    print("\n*** SAMPLE PASSED ***\n")

    solved = solve(REAL)
    print("SOLUTION: ", solved)
