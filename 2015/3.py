from collections import defaultdict, deque
import re

CHALLENGE_DAY = "3"
REAL = open(CHALLENGE_DAY + ".txt").read()
SAMPLE = open(CHALLENGE_DAY + ".sample.txt").read()
SAMPLE_EXPECTED = 2

def parse_lines(raw):
    # Groups.
    # groups = raw.split("\n\n")
    # return list(map(lambda group: group.split("\n"), groups))
    
    lines = raw.split("\n")
    l = lines[0].strip()
    return l
    # return lines # raw
    # return list(map(lambda l: l.split(" "), lines)) # words.
    # return list(map(int, lines))
    # return list(map(lambda l: l.strip(), lines)) # beware leading / trailing WS

def solve(raw):
    parsed = parse_lines(raw)

    pos = (0,0)
    visited = {}
    visited[pos] = True
    for move in parsed:
        dx, dy = {"^": (0, -1), "v": (0, 1), ">": (1, 0), "<": (-1, 0)}[move]
        x, y = pos
        pos = (x + dx, y + dy)
        visited[pos] = True
    ret = 0

    return len(visited)

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
