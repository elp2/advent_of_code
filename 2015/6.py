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

    lights = set()

    for i, line in enumerate(parsed):
        print(i, line, len(lights))
        action, fx, fy, tx, ty = line_action(line)
        for x in range(fx, tx + 1):
            for y in range(fy, ty + 1):
                pos = (x, y)
                if action == "toggle":
                    if pos in lights:
                        lights.remove(pos)
                    else:
                        lights.add(pos)
                elif action == "on":
                    lights.add(pos)
                elif action == "off":
                    if pos in lights:
                        lights.remove(pos)
                else:
                    assert False

    return len(lights)

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
