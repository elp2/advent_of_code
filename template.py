from collections import defaultdict, deque
import re

CHALLENGE_DAY = "22"
REAL = open(CHALLENGE_DAY + ".txt").read()
SAMPLE = open(CHALLENGE_DAY + ".sample.txt").read()
# SAMPLE_EXPECTED = None
# SAMPLE_EXPECTED = 


def parse_lines(raw):
    # Groups.
    # split = raw.split("\n\n")
    # return list(map(lambda group: group.split("\n"), split))
    
    # split = raw.split("\n")
    # return split # raw
    # return list(map(lambda l: l.split(" "), split)) # words.
    # return list(map(int, split))
    # return list(map(lambda l: l.strip(), split)) # beware leading / trailing WS

def solve(raw):
    parsed = parse_lines(raw)
    # Debug here to make sure parsing is good.
    ret = 0

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
