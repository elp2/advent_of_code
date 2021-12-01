from collections import defaultdict, deque
import hashlib
from itertools import combinations, combinations_with_replacement, permutations
import math
import re

DAY = "5"
REAL = "ffykfhsq"

SAMPLE_EXPECTED = None

def parse_line(line):
    ret = re.findall(r'([a-z-]+)(\d+)\[([a-z]+)', line)
    ret[1] = int(ret[1])

def parse_lines(raw):
    return [parse_line(line) for line in raw.split("\n")]

def solve(base):
    password = []
    i = 0
    while len(password) < 8:
        h = base + str(i)
        h = h.encode()
        hashed = hashlib.md5(h).hexdigest()
        if hashed[:5] == "00000":
            password.append(hashed[5])
        i += 1
    return "".join(password)

def part2(base):
    password = [None] * 8
    i = 0
    while None in password:
        h = base + str(i)
        h = h.encode()
        hashed = hashlib.md5(h).hexdigest()
        if hashed[:5] == "00000":
            char = hashed[6]
            pos = int(hashed[5], 16)

            if 0 <= pos < len(password):
                if password[pos] == None:
                    password[pos] = char
                    print("! ", password)
                else:
                    print("Can't put ", char, " in ", password)
            else:
                print("can't put ", char, "After array", password)
        i += 1
    return "".join(password)


if SAMPLE_EXPECTED != None:
    SAMPLE = open(DAY + ".sample").read()
    sample = solve(SAMPLE)
    if sample != SAMPLE_EXPECTED:
        print("SAMPLE FAILED: ", sample, " != ", SAMPLE_EXPECTED)
    assert sample == SAMPLE_EXPECTED
    print("\n*** SAMPLE PASSED ***\n")
else:
    print("Skipping sample")

# solved = solve(REAL)
# print("SOLUTION: ", solved)


p2 = part2(REAL)
print("Part2: ", p2)

try:
    import pandas as pd
    df=pd.DataFrame([str(solved)])
    df.to_clipboard(index=False,header=False)
    print("COPIED TO CLIPBOARD")
except ModuleNotFoundError:
    print("Pandas not installed.")