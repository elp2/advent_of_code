from collections import defaultdict, deque
import re

CHALLENGE_DAY = "6"
REAL = open(CHALLENGE_DAY + ".txt").read()
SAMPLE = open(CHALLENGE_DAY + ".sample.txt").read()
# SAMPLE_EXPECTED = 4

def parse_lines(raw):
    # Groups.
    # groups = raw.split("\n\n")
    # return list(map(lambda group: group.split("\n"), groups))
    
    lines = raw.split("\n")
    return lines # raw
    # return list(map(lambda l: l.split(" "), lines)) # words.
    # return list(map(int, lines))
    # return list(map(lambda l: l.strip(), lines)) # beware leading / trailing WS

def line_action(line):
    if "toggle" in line:
        line = "toggle " + line
    
    split = line.split(" ")
    _, action, f, _, t = split
    fx, fy = map(int, f.split(","))
    tx, ty = map(int, t.split(","))

    return action, fx, fy, tx, ty

def solve(raw):
    parsed = parse_lines(raw)
    # Debug here to make sure parsing is good.
    ret = 0

    lights = {}

    for i, line in enumerate(parsed):
        print(i, line, len(lights))
        action, fx, fy, tx, ty = line_action(line)
        for x in range(fx, tx + 1):
            for y in range(fy, ty + 1):
                pos = (x, y)
                here = lights[pos] if pos in lights else 0
                assert here >= 0
                if action == "toggle":
                    lights[pos] = here + 2
                elif action == "on":
                    lights[pos] = here + 1
                elif action == "off":
                    if here >= 1:
                        lights[pos] = here - 1
                else:
                    assert False
    return sum(lights.values()) # 17325717 low  # 17836115 juuuust right!

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
