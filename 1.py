from collections import defaultdict, deque
import re

CHALLENGE_DAY = "1"
REAL = open(CHALLENGE_DAY + ".txt").read()
# SAMPLE = open(CHALLENGE_DAY + ".sample.txt").read()
# SAMPLE_EXPECTED = None
# SAMPLE_EXPECTED = 


def parse_lines(raw):
    # Groups.
    # groups = raw.split("\n\n")
    # return list(map(lambda group: group.split("\n"), groups))
    
    lines = raw.split("\n")
    return lines[0] # raw
    # return list(map(lambda l: l.split(" "), lines)) # words.
    # return list(map(int, lines))
    # return list(map(lambda l: l.strip(), lines)) # beware leading / trailing WS

def solve(raw):
    parsed = parse_lines(raw)
    # Debug here to make sure parsing is good.
    ret = 0
    for i,  c in enumerate(parsed):
        if c == "(":
            ret += 1
        elif c == ")":
            ret -= 1
        else:
            print(c)
        if ret == -1:
            print(i + 1)

    return ret

# sample = solve(SAMPLE)
# if sample != SAMPLE_EXPECTED:
#     print("SAMPLE FAILED: ", sample, " != ", SAMPLE_EXPECTED)
# assert sample == SAMPLE_EXPECTED
# print("\n*** SAMPLE PASSED ***\n")

solved = solve(REAL)
print("SOLUTION: ", solved)
import pandas as pd
df=pd.DataFrame([str(solved)])
df.to_clipboard(index=False,header=False)
print("COPIED TO CLIPBOARD")

# Sat Jan  9 20:48:09 PST 2021
# Sat Jan  9 20:50:49 PST 2021
# Sat Jan  9 20:51:47 PST 2021