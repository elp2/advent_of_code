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


CHALLENGE_DAY = "24"
REAL = open(CHALLENGE_DAY + ".txt").read()

SAMPLE_EXPECTED = None
if SAMPLE_EXPECTED:
    SAMPLE = open(CHALLENGE_DAY + ".s.txt").read()



def execute(program, input, w = 0, z = 0):
    # assert len(input) == 14
    # Debug here to make sure parsing is good.
    ret = 0
    ii = 0

    regs = {"x": 0, "y": 0, "z": z, "w": w}
    def val(v):
        try:
            ret = int(v)
            return ret
        except:
            return regs[v]

    for i, l in enumerate(program):
        if l[0] == "inp":
            regs[l[1]] = int(input[ii])
            ii += 1
            # print(regs)
        elif l[0] == "add":
            a, b = l[1:]
            regs[a] = val(a) + val(b)
        elif l[0] == "mul":
            a, b = l[1:]
            regs[a] = val(a) * val(b)
        elif l[0] == "div":
            a, b = l[1:]
            regs[a] = int(val(a) / val(b))
        elif l[0] == "mod":
            a, b = l[1:]
            regs[a] = val(a) % val(b)
        elif l[0] == "eql":
            a, b = l[1:]
            regs[a] = 1 if val(a) == val(b) else 0
        else:
            assert False

    return val("z")

def make_func(lines):
    assert len(lines) == 18
    assert lines[0][0] == "inp"
    zdiv = int(lines[4][2])
    xdelta = int(lines[5][2])
    ydelta = int(lines[15][2])

    def piece(w, x, y, z0):
        x = (z0 % 26) + xdelta
        xneqw = 1 if x != w else 0
        y = 26 if xneqw == 1 else 1
        c = (ydelta + w) * xneqw

        a = int(z0 / zdiv) # zorig = (x - xdelta) + 26 * a
        b = a * y
        z = b + c
        return w, x, c, z

    def zprevs(z, w):
        zp = []
        for zmod26 in range(26):
            # zmod26 = z0 % 26
            x = zmod26 + xdelta
            xneqw = 1 if x != w else 0
            y = 26 if xneqw == 1 else 1
            c = (ydelta + w) * xneqw

            b = z - c
            a = b / y
            if int(a) != a:
                continue
            a = int(a)
            if zdiv == 1:
                for xd in range(26):
                    z0 = a + xd
                    forwards = piece(w, 0, 0, z0)[3]
                    if forwards == z:
                        forwards = piece(w, 0, 0, z0)[3]
                        assert z == forwards
                        zp.append(z0)
                assert len(zp) > 0
            else:
                z0 = zmod26 + zdiv * a
                forwards = piece(w, 0, 0, z0)[3]
                if forwards != z:
                    forwards = piece(w, 0, 0, z0)[3]
                    assert z == forwards
            zp.append(z0)
        return zp
    
    # for w in range(1, 10):
    #     zps = zprevs(0, w)
    #     for zp in zps:
    #         p = piece(w, 0, 0, zp)[3]

    return piece, zprevs


def parse_lines(raw):
    # Groups.
    # groups = raw.split("\n\n")
    # return list(map(lambda group: group.split("\n"), groups))
    lines = raw.split("\n")
    # return lines # raw
    lines = list(map(lambda l: l.split(" "), lines)) # words.
    funcs = []
    for i in range(0, len(lines), 18):
        section = lines[i:i+18]
        func, zps = make_func(section)
        for w in range(1, 10):
            _, _, _, z = func(w, 0, 0, 0)
            ex = execute(section, str(w) * 14)
            assert ex == z
            # zpa = zps(ex, w)
            # assert len(zpa) != 0
            # for zp in zpa:
            #     _, _, _, z2 = func(w, 0, 0, zp)
            #     assert z2 == ex

        funcs.append((func, zps))
    return lines, funcs


def solve_backwards(raw, num_funcs, end_target):
    parsed, funcs = parse_lines(raw)

    # funcs = funcs[:2]
    funcs = funcs[:num_funcs]
    mid = int(num_funcs / 2)
    parsed = parsed[:18 * num_funcs]
    # mid = 8

    forward_funcs = funcs[:mid]
    back_funcs = funcs[mid:]
    back_funcs = back_funcs[::-1]

    best_path = {end_target: ""}
    for depth in range(len(back_funcs)):

        bpnew = {}
        # at this depth, what zs do we need to export?
        for target, history in best_path.items():
            for w in range(1, 10):
                # What would the original z need to be here?
                zps = back_funcs[depth][1](target, w)
                for zp in zps:
                    here = str(w) + history
                    if zp not in bpnew or int(bpnew[zp]) < int(here):
                        bpnew[zp] = here
        best_path = bpnew
        print("back: ", depth, len(best_path))
        # print([k for k, v in best_path.items() if v == "9999"])


    def it(l):
        num = int(l * "9")

        while num > int((l-1) * "9"):
            yield str(num)
            while True:
                num -= 1
                if "0" not in str(num):
                    break            

    seens = 0
    for f in it(len(forward_funcs)):
        seens += 1
        if seens % 100000 == 0:
            print(seens)
        w = x = y = z = 0
        if len(f) != len(forward_funcs):
            print(f, len(forward_funcs))
            assert len(f) == len(forward_funcs)

        for depth in range(len(forward_funcs)):
            w, x, y, z = forward_funcs[depth][0](int(f[depth]), 0, 0, z)
        if z in best_path.keys():
            sol = str(f) + best_path[z]
            print("SOLUTION?", sol)
            if execute(parsed, sol) == end_target:
                return sol

    assert False
    return None

def check_shared(raw):
    raw, funcs = parse_lines(raw)
    for i in range(len(raw) - 19):
        l1 = raw[i]
        l2 = raw[i+18]
        assert l1[0] == l2[0]
        assert l1[1] == l2[1]
        if len(l1) == 3:
            print(l1[2], l2[2])


# check_shared(REAL)

if SAMPLE_EXPECTED != None:
    sample = solve(SAMPLE)
    if sample != SAMPLE_EXPECTED:
        print("SAMPLE FAILED: ", sample, " != ", SAMPLE_EXPECTED)
    assert sample == SAMPLE_EXPECTED
    print("\n*** SAMPLE PASSED ***\n")
else:
    print("Skipping sample")


def brute(raw):
    def it():
        num = 99999999999999
        while True:
            yield str(num)
            while True:
                num -= 1
                if "0" not in str(num):
                    break         

    parsed, funcs = parse_lines(raw)
    seens = 0
    for f in it():
        seens += 1
        if seens % 100000 == 0:
            print(seens)
        w = x = y = z = 0
        if len(f) != len(funcs):
            print(f, len(funcs))
        for depth in range(len(funcs)):
            w, x, y, z = funcs[depth][0](int(f[depth]), 0, 0, z)
        if z == 0:
            print("!", f)
            assert False

def test(raw):
    parsed, funcs = parse_lines(raw)
    nf = 8
    x = y = z = w = 0
    path = "99971192"
    for i in range(nf):
        w, x, y, z = funcs[i][0](int(path[i]), x, y, z)
        print(i, z)

    zc = execute(parsed[:18 * 8], path)
    assert zc == z



    sb = solve_backwards(raw, len(path), z)
    print(sb, path)
    assert sb == path

test(REAL)
# brute(REAL)
solved = solve_backwards(REAL, 14, 0)
assert int(solved) < 93792949489995
assert int(solved) == 92793949489995

print("SOLUTION: ", solved)
