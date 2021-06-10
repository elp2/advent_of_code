from collections import defaultdict, deque
import re

CHALLENGE_DAY = "19"
REAL = open(CHALLENGE_DAY + ".txt").read()

def parse_lines(raw):
    # Groups.
    groups = raw.split("\n\n")

    molecule = groups[1]
    lines = groups[0].split("\n")
    rules = []
    for l in lines:
        f, t = l.split(" => ")
        rules.append((f, t))

    return rules, molecule

def solve(raw):
    rules, molecule = parse_lines(raw)

    seen = set()
    for rule in rules:
        f, t = rule
        if f not in molecule:
            continue
        start = 0
        while True:
            pos = molecule.find(f, start)
            if pos == -1:
                break
            fixed = molecule[0:pos] + t + molecule[pos + len(f):]
            seen.add(fixed)
            start = pos + 1
    return len(seen)

    return ret


solved = solve(REAL)
print("SOLUTION: ", solved)
