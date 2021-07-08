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


def part2(raw):
    rules, molecule = parse_lines(raw)

    seen = set()
    steps = 0

    here = ["e"]
    while True:
        evolutions = []
        print(steps, len(here))
        for h in here:
            for rule in rules:
                f, t = rule
                if f not in h:
                    continue
                start = 0
                while True:
                    pos = h.find(f, start)
                    if pos == -1:
                        break
                    fixed = h[0:pos] + t + h[pos + len(f):]
                    if fixed == h:
                        return steps
                    if fixed not in seen and len(fixed) < len(molecule) + 5:
                        evolutions.append(fixed)
                    seen.add(fixed)
                    start = pos + 1

        here = evolutions
        steps += 1

print("Part 2:", part2(REAL))
