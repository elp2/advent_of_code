from collections import defaultdict

def return_default():
    return 0

REAL=open("12.txt").read()
SAMPLE=open("12.sample").read()

def parse_lines(raw):
    groups = raw.split("\n\n")

    pots = set()
    for i, s in enumerate(groups[0].split(": ")[1]):
        if s == "#":
            pots.add(i)

    rules = {}
    for line in groups[1].split("\n"):
        rule, output = line.split(" => ")
        rules[rule] = True if output == "#" else False

    return pots, rules

from collections import deque
import copy

def new_val(pots, p, rules):
    key = ""
    for i in range(p - 2, p + 3):
        if i in pots:
            key += "#"
        else:
            key += "."
    if key in rules:
        return rules[key]
    else:
        return False


    return rules[key]

def print_pots(minp, maxp, pots):
    line = ""
    under = ""
    for i in range(minp, maxp):
        line += "#" if i in pots else "."
        under +="^" if i == 0 else " " 
    print(line)
    print(under)

def part2(base, num_pots, round_num):
    return base + num_pots * (round_num - 91)

def solve(raw, num_rounds=20):
    pots, rules = parse_lines(raw)

    for round_num in range(num_rounds):
        new_pots = set()
        for p in range(min(pots) - 5, max(pots) + 5):
            if new_val(pots, p, rules):
                new_pots.add(p)
        pots = new_pots
        if round_num >= 85:
            if round_num == 91:
                base = sum(pots)
                num_pots = len(pots)                
            if round_num > 91:
                assert sum(pots) == part2(base, num_pots
                , round_num)

            print(round_num, sum(pots))
            print_pots(-10, 200, new_pots)
            print()

    return part2(base, num_pots, 50000000000 - 1)

# sample = solve(SAMPLE)
# assert sample == 325
# print("*** SAMPLE PASSED ***")
# assert solve(REAL) == 3725

print("Part2: ", solve(REAL, 150))
