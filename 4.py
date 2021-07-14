from collections import defaultdict, deque
from itertools import combinations, combinations_with_replacement, permutations
from operator import add, mul, itemgetter, attrgetter
import math
import re

DAY = "4"
REAL = open(DAY + ".in").read()

SAMPLE_EXPECTED = None

def parse_line(line):
    ret = list(re.findall(r'([a-z-]+)(\d+)\[([a-z]+)', line)[0])
    ret[1] = int(ret[1])
    return ret

def parse_lines(raw):
    return [parse_line(line) for line in raw.split("\n") if line]

def validate(seen, checksum):
    def o(x):
        return -26 * x[1] + ord(x[0]) - ord('a')
    ordered = sorted(seen.items(), key=o)
    actual = "".join([x[0] for x in ordered])[:5]

    return actual == checksum


def solve(raw):
    parsed = parse_lines(raw)
    ret = 0
    for letters, lid, checksum in parsed:
        seen = defaultdict(lambda: 0)
        for l in letters:
            if "-" == l:
                continue
            seen[l] += 1
        if validate(seen, checksum):
            ret += lid

    return ret

if SAMPLE_EXPECTED != None:
    SAMPLE = open(DAY + ".sample").read()
    sample = solve(SAMPLE)
    if sample != SAMPLE_EXPECTED:
        print("SAMPLE FAILED: ", sample, " != ", SAMPLE_EXPECTED)
    assert sample == SAMPLE_EXPECTED
    print("\n*** SAMPLE PASSED ***\n")
else:
    print("Skipping sample")

solved = solve(REAL)
print("SOLUTION: ", solved)


def part2(raw):
    parsed = parse_lines(raw)
    ret = 0
    def unencrypt(l, lid):
        if l == "-":
            return " "
        assert ord('a') <= ord(l) <= ord('z')
        cord = ord(l) - ord('a')
        cord += lid
        cord = cord % 26
        return chr(cord + ord('a'))

    for letters, lid, _ in parsed:
        unencrypted = [unencrypt(l, lid) for l in letters]
        print("".join(unencrypted), lid)

part2(REAL) # northpole object storage  993

try:
    import pandas as pd
    df=pd.DataFrame([str(solved)])
    df.to_clipboard(index=False,header=False)
    print("COPIED TO CLIPBOARD")
except ModuleNotFoundError:
    print("Pandas not installed.")