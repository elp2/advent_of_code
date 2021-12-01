from collections import defaultdict, deque
import re

CHALLENGE_DAY = "8"
REAL = open(CHALLENGE_DAY + ".txt").read()
SAMPLE = open(CHALLENGE_DAY + ".sample.txt").read()
SAMPLE_EXPECTED = 19

def parse_lines(raw):
    # Groups.
    # groups = raw.split("\n\n")
    # return list(map(lambda group: group.split("\n"), groups))
    
    lines = raw.split("\n")
    return lines # raw
    # return list(map(lambda l: l.split(" "), lines)) # words.
    # return list(map(int, lines))
    # return list(map(lambda l: l.strip(), lines)) # beware leading / trailing WS

def unquote(literal):
    literal = literal[1:-1] # remove outer ""
    transformed = []
    i = 0
    while i < len(literal):
        c = literal[i]
        if c == "\\":
            n = literal[i+1] if i + 1 < len(literal) else None
            assert n
            if n == "\"":
                transformed.append("\"")
                i += 1
            elif n == "x":
                assert i + 3 < len(literal)
                i += 3
                transformed.append("?") # TODO?
            elif n == "\\":
                i += 1
                transformed.append("\\")
            else:
                assert False
        else:
            transformed.append(c)
        i += 1
    return "".join(transformed)

def encode(literal):
    transformed = ["\""]
    i = 0
    while i < len(literal):
        c = literal[i]
        if c == "\"":
            transformed.append("\\\"")
        elif c == "\\":
            transformed.append("\\\\")
        else:
            transformed.append(c)
        i += 1
    
    transformed.append("\"")

    return "".join(transformed)

def solve(raw):
    parsed = parse_lines(raw)
    # Debug here to make sure parsing is good.
    ret = 0

    for line in parsed:
        line = line.strip()
        e = encode(line)
        print(line, "->", e, len(e), len(line))
        ret += (len(e) - len(line))

    return ret

sample = solve(SAMPLE)
if sample != SAMPLE_EXPECTED:
    print("SAMPLE FAILED: ", sample, " != ", SAMPLE_EXPECTED)
assert sample == SAMPLE_EXPECTED
print("\n*** SAMPLE PASSED ***\n")

solved = solve(REAL)
print("SOLUTION: ", solved)
import pandas as pd
df=pd.DataFrame([str(solved)])
df.to_clipboard(index=False,header=False)
print("COPIED TO CLIPBOARD")
