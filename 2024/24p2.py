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


def parse_lines(raw, swaps):
    initialsstr, gatesstr = raw.split("\n\n")
    namevals = {}
    for line in initialsstr.split("\n"):
        name, val = line.split(": ")
        namevals[name] = 1 if val == "1" else 0
    
    gates = []
    
    for line in gatesstr.split("\n"):
        # qgv OR dsf -> mjm
        a, op, b, _, to = line.split(" ")
        if to in swaps:
            to = swaps[to]
        gates.append((a, op, b, to))

    return namevals, gates


def investigate_down(gates, bit):
    q = deque()
    q.append((f"x{bit:02d}", [f"x{bit:02d}"]))
    q.append((f"y{bit:02d}", [f"y{bit:02d}"]))
    unexpected = []
    seen_gates = []
    seen_wires = set()
    while q:
        node, path = q.popleft()
        seen_wires.add(node)
        # print("NP", node, path)
        if node[0] == "z":
            nbit = int(node[1:])
            if nbit not in [bit, bit+1]:
                # if path[1] == "nvv" and path[2] == "whj" and path[3] == "ghb":
                #     continue
                unexpected.append((node, path))
            else:
                print("GOOD: ", path)
            continue

        ingates = [g for g in gates if g[0] == node or g[2] == node]
        assert ingates
        for ig in ingates:
            q.append((ig[-1], path + [f"{ig[1]}->{ig[-1]}"]))
            # print(ig)
            seen_gates.append(ig)
    
    questionable_gates = []
    if len(unexpected):
        questionable_gates = seen_gates
    return unexpected, questionable_gates, seen_wires

def investigate_up(gates, bit):
    q = deque()
    q.append((f"z{bit:02d}", [f"z{bit:02d}"]))
    # q.append((f"y{bit:02d}", [f"y{bit:02d}"]))
    unexpected = []
    seen_gates = set()
    while q:
        node, path = q.popleft()
        if node[0] in ["x", "y"]:
            num = int(node[1:])
            print(path)
            # if num not in [bit, bit-1, bit+1]:
            #     if path[1] == "jvs" and path[2] == "wtr":
            #         continue
            #     if path[1] == "ngw" and path[2] == "jsc":
            #         continue
            #     if path[1] == "brq" and path[2] == "fgf":
            #         continue

            unexpected.append((node, path))
            continue
        for g in gates:
            if g[3] == node:
                q.append((g[0], path + [f"<{g[1]}-{g[0]}"]))
                q.append((g[2], path + [f"<{g[1]}-{g[2]}"]))
            seen_gates.add(g)
            
    questionable_gates = set()
    if len(unexpected):
        questionable_gates = seen_gates
    
    return unexpected, questionable_gates

SWAPS=[]

def solve(raw):
    doswaps = [
        ("qjb", "gvw"), # 8
        ("z15", "jgc"), # 15
        ("drg", "z22"), # 22
        ('z35', 'jbp'),
    ]
    ret = []
    for (a,b) in doswaps:
        ret.append(a)
        ret.append(b)
    return ",".join(sorted(ret))


    def set_input(namevals, x, y):
        num_xys = 46
        namevals = namevals.copy()
        xb = bin(x)[2:]
        xb = "0" * (num_xys - len(xb)) + xb
        xb = list(xb)
        xb.reverse()
        yb = bin(y)[2:]
        yb = "0" * (num_xys - len(yb)) + yb
        yb = list(yb)
        yb.reverse()
        for xi, xv in enumerate(xb):
            namevals[f"x{xi:02d}"] = int(xv)
        for yi, yv in enumerate(yb):
            namevals[f"y{yi:02d}"] = int(yv)
        return namevals

    def test_swapped(namevals, gates):
        broken = Counter()
        ret = 0
        doprint = False
        for _ in range(100):
            def run_test(na, nb):
                expected = na + nb
                ane = set_input(namevals, na, nb)
                bne = set_input(namevals, nb, na)
                a = execute(ane, gates)
                b = execute(bne, gates)
                assert a == b
                if a != expected or b != expected:
                    ba = bin(a)[2:]
                    be = bin(expected)[2:]
                    be = "0" * (46 - len(be)) + be
                    ba = "0" * (46 - len(ba)) + ba
                    if doprint:
                        print(ba)
                        print(be)
                        line = ""
                        for i, ic in enumerate(be):
                            if be[i] == ba[i]:
                                line += " "
                            else:
                                broken[i] += 1
                                line += "*"
                        print(line)
                    return 0
                else:
                    if doprint:
                        print("OK!", bin(a), bin(b))
                    return 1

            import random
            na = random.randint(pow(2, 25), pow(2, 45))
            nb = random.randint(pow(2, 25), pow(2, 45))
            ret += run_test(na, nb)
        return ret

    _, gates = parse_lines(raw, {})
    def test_swap_pair(p1, p2):
        swaps = {}
        for (sa, sb) in doswaps:
            swaps[sa] = sb
            swaps[sb] = sa
        swaps[p1] = p2
        swaps[p2] = p1
        namevals, gates = parse_lines(raw, swaps)
        return test_swapped(namevals, gates)

    all_wires = set()
    for i in [33, 34, 35]:
        _, _, seen_wires = investigate_down(gates, i)
        all_wires = all_wires.union(seen_wires)
        print("------------")

    bests = Counter()
    t = 0
    for (p1, p2) in combinations(all_wires, 2):
        r = test_swap_pair(p1, p2)
        if r == 100:
            print("!!!!!!!!!!!!!!!!", p1, p2)
        bests[(p1, p2)] = r
        print()
        t += 1
        if t % 10 == 0:
            print(t, bests.most_common(5))
    print(bests.most_common(5))

    print("bests")



def execute(namevals, gates):
    namevals = namevals.copy()
    gates = gates[:]
    safety = 0
    while gates:
        safety += 1
        if safety > 100:
            return 0
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
                # print(a, av, op, b, bv, to, val)
                namevals[to] = val  
        gates = [g for g in gates if g]

    binary = []
    for i in range(100):
        if f"z{i:02d}" in namevals:
            v = 1 if namevals[f"z{i:02d}"] else 0
            binary.append(v)
            # print(f"z{i:02d}", v)
    binary.reverse()
    ret = int("".join([str(bb) for bb in binary]), 2)
    return ret

if __name__ == "__main__":
    SAMPLE, REAL = get_raw_inputs(sys.argv)

    S2 = """x00: 0
x01: 1
x02: 0
x03: 1
x04: 0
x05: 1
y00: 0
y01: 0
y02: 1
y03: 1
y04: 0
y05: 1

x00 AND y00 -> z05
x01 AND y01 -> z02
x02 AND y02 -> z01
x03 AND y03 -> z03
x04 AND y04 -> z04
x05 AND y05 -> z00"""
    # s2 = solve(S2)
    # assert s2 == "z00,z01,z02,z05"

    # sample = solve(SAMPLE)
    # assert sample == SAMPLE_EXPECTED, "Sample Result %s != %s expected" % (sample, SAMPLE_EXPECTED)
    # print("\n*** SAMPLE PASSED ***\n")

    solved = solve(REAL)
    print("SOLUTION: ", solved)
