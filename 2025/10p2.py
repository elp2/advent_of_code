from collections import defaultdict, deque, Counter
from itertools import combinations, combinations_with_replacement, permutations, product
from functools import reduce, cmp_to_key
from operator import add, mul, itemgetter, attrgetter
import os
import sys
from z3 import *

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, root_dir)
from aoc_elp import *

######################
SAMPLE_EXPECTED = 33
######################
assert SAMPLE_EXPECTED != None, "Must enter sample value"

def parse_group(group):
    lines = group.split("\n")
    ret = []
    for y, line in enumerate(lines):
        line = line.strip()
        assert len(line) != 0

        split = line.split(" ")
        lights = [b == "#" for b in split[0][1:-1]]
        buttons = split[1:-1]
        buttons = [b.replace("(", "[").replace(")", "]") for b in buttons]
        buttons = [set(eval(b)) for b in buttons]
        joltage = list(map(int, split[-1][1:-1].split(",")))

        assert len(split) != 0
        ret.append((lights, buttons, joltage))

    return ret


def parse_lines(raw):
    # Groups.
    # groups = raw.split("\n\n")
    # Do something with the groups.

    return parse_group(raw)

def solve(raw):
    parsed = parse_lines(raw)
    print(parsed)

    ret = 0
    a = Int('a')
    b = Int('b')
    c = Int('c')
    d = Int('d')
    e = Int('e')
    f = Int('f')
    g = Int('g')
    h = Int('h')
    i = Int('i')
    j = Int('j')
    k = Int('k')
    l = Int('l')
    m = Int('m')
    alphabet = 'abcdefghijklm'
    alphavars = [a,b,c,d,e,f,g,h,i,j,k,l, m]
    for _, buttons, joltages in parsed:
        here = 0
        s = Optimize()
        for char in alphabet:
            s.add(eval(char + " >= 0"))
        eqs = []
        for x, joltage in enumerate(joltages):
            eq = []
            for bi, but in enumerate(buttons):
                if x in but:
                    eq.append(alphabet[bi])
            eqstr = " + ".join(eq) + " == " + str(joltage)
            eqs.append(eqstr)
            print("EEE ", eqstr)
            s.add(eval(eqstr))
        # print(s)
        s.minimize(a+b+c+d+e+f+g+h+i+j+k+l+m)
        assert s.check() == sat
        here = 0
        for kk in alphavars:
            print(kk, s.model()[kk])
            here += eval(str(s.model()[kk]))
        print("HERE: ", here)
        ret += here

    return ret

if __name__ == "__main__":
    SAMPLE, REAL = get_raw_inputs(sys.argv)

    sample = solve(SAMPLE)
    assert sample == SAMPLE_EXPECTED, "Sample Result %s != %s expected" % (sample, SAMPLE_EXPECTED)
    print("\n*** SAMPLE PASSED ***\n")

    solved = solve(REAL)
    print("SOLUTION: ", solved)



# 19129 too high