from collections import defaultdict, deque
from itertools import combinations, combinations_with_replacement, permutations
import math
from operator import add, mul, itemgetter, attrgetter
import re
def flatten(t):
    return [item for sublist in t for item in sublist]

DAY = "7"
REAL = open(DAY + ".in").read()

SAMPLE_EXPECTED = None

def parse_line(line):
    s = re.split(r"\[([^\]]+)\]", line)
    return s[1::2], s[::2]

def has_abba(text):
    for a, b, c, d in zip(text, text[1:], text[2:], text[3:]):
        if a != b and a == d and b == c:
            return True
    return False

def parse_lines(raw):
    return [parse_line(line) for line in raw.split("\n")]


def solve(raw):
    parsed = parse_lines(raw)
    p1 = 0
    for ins, outs in parsed:
        if not any(map(has_abba, ins)) and any(map(has_abba, outs)):
            p1 += 1

    return p1


def part2(raw):
    parsed = parse_lines(raw)
    p2 = 0
    for ins, outs in parsed:
        def abas(l):
            def abify(l):
                return [(a, b) for a, b, c in zip(l, l[1:], l[2:]) if a == c and a != b]
            return flatten(map(abify, l))

        in_abas = abas(ins)
        for a, b in abas(outs):
            if (b, a) in in_abas:
                p2 += 1
                break
    return p2


if SAMPLE_EXPECTED != None:
    SAMPLE = open(DAY + ".sample").read()
    sample = solve(SAMPLE)
    if sample != SAMPLE_EXPECTED:
        print("SAMPLE FAILED: ", sample, " != ", SAMPLE_EXPECTED)
    assert sample == SAMPLE_EXPECTED
    print("\n*** SAMPLE PASSED ***\n")
else:
    print("Skipping sample")

assert not has_abba("asdfgh")
assert has_abba("ioxxoj")
print(parse_line("ioxxoj[asdfgh]zxcvbn"))
print(parse_line("azawpddzkqbosmltyxt[zoaaqnowmmwkmfkq]lgusvzwnimvgagupkt[scbjhqdftzssbvnvff]coiaslgcrwvyioxx[jouvwdiwvbsembzf]popmlnhjkoaeahcny"))
solved = solve(REAL)
print("SOLUTION: ", solved)

print("Part2", part2(REAL))
try:
    import pandas as pd
    df=pd.DataFrame([str(solved)])
    df.to_clipboard(index=False,header=False)
    print("COPIED TO CLIPBOARD")
except ModuleNotFoundError:
    print("Pandas not installed.")