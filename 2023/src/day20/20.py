from collections import defaultdict, deque, Counter
from itertools import combinations, combinations_with_replacement, permutations
from functools import reduce, cmp_to_key
import math
# import numpy as np
from operator import add, mul, itemgetter, attrgetter
import os
import re
from sys import argv

def flatten(t):
    return [item for sublist in t for item in sublist]

# Sorts with cmp. cmp < 0 for a < b, == 0 for a==b, > 0 for a > b.
def elpsort(array, cmp):
    return sorted(array, key=cmp_to_key(cmp))

ON_TEXT = '\u2588'
OFF_TEXT = '\u2592'

LOW="L"
HIGH="H"

FLIPFLOP="%"
CONJUNCTION="&"
BROADCASTER="broadcaster"
LEFT = 0
UP = 1
RIGHT = 2
DOWN = 3
CHAR_TO_DS = {"^": UP, ">": RIGHT, "<": LEFT, "v": DOWN}
DS = [(-1, 0), (0, -1), (1, 0), (0, 1)]
DS8 = DS + [(-1, -1), (1, -1), (-1, 1), (1, 1)]

def arounds(x, y, diagonals):
    ret = []
    for dx, dy in DS8 if diagonals else DS:
        ret.append((x + dx, y + dy))
    return ret

CHALLENGE_DAY = argv[0].split("/")[-1].replace(".py", "").replace("p2.py", "")
AOC_DIR = os.path.dirname(argv[0])

print("Day: ", CHALLENGE_DAY)

######################
SAMPLE_EXPECTED = 32000000
######################
assert SAMPLE_EXPECTED != None

try:
    SAMPLE = open(os.path.join(AOC_DIR, CHALLENGE_DAY + ".s.txt")).read()
except:
    print("Did you create the sample file?")

try:
    REAL = open(os.path.join(AOC_DIR, CHALLENGE_DAY + ".txt")).read()
except:
    print("Did you create the solutions file?")


def parse_lines(raw):
    lines = raw.split("\n")

    ret = defaultdict(lambda: {})

    for l in lines:
        name, targets = l.split(" -> ")
        targets = targets.split(", ")

        if name == BROADCASTER:
            ret[name] = {
                "name": name,
                "targets": targets,
                "ins": [],
                "type": name,
            }
        else:
            t = name[0]
            name = name[1:]
            ret[name]["type"] = t
            

            ret[name]["name"] = name
            if "ins" not in ret[name]:
                ret[name]["ins"] = []
            for targ in targets:
                if ret[targ] == {}:
                    ret[targ] = {"ins": []}
                ret[targ]["ins"].append(name)
            ret[name]["targets"] = targets

    for name in ret.keys():
        h = ret[name]
        if name == "rx":
            continue
        if h["type"] == FLIPFLOP:
            h["state"] = False
        elif h["type"] == CONJUNCTION:
            h["memory"] = {}
            for k in h["ins"]:
                h["memory"][k] = LOW

    return ret

def actions_for(from_name, node, pulse):
    if "type" not in node:
        return []
    print("processing: ", from_name, "->", pulse, "->", node["name"])
    ret = []
    if node["type"] == BROADCASTER:
        for t in node["targets"]:
            ret.append((node["name"], t, LOW))
    elif node["type"] == FLIPFLOP:
        if pulse == "H":
            return []
        node["state"] = not node["state"]
        for t in node["targets"]:
            ret.append((node["name"], t, HIGH if node["state"] else LOW))
    elif node["type"] == CONJUNCTION:
# Conjunction modules (prefix &) remember the type of the most recent pulse received from each of their connected 
# input modules; they initially default to remembering a low pulse for each input. 

# When a pulse is received, the conjunction module first updates its memory for that input. 
        node["memory"][from_name] = pulse
        # Then, if it remembers high pulses for all inputs, it sends a low pulse; otherwise, it sends a high pulse.
        conj_send = LOW if all(m == HIGH for m in node["memory"].values()) else HIGH
        for t in node["targets"]:
            ret.append((node["name"], t, conj_send))
    return ret        


def solve(raw):
    graph = parse_lines(raw)

    highs, lows = 0, 0
    for presses in range(1000):
        q = deque()
        q.append(("button", BROADCASTER, LOW))

        while len(q):
            from_name, to_name, pulse = q.popleft()
            node = graph[to_name]
            if pulse == LOW:
                lows += 1
            else:
                highs += 1
            actions = actions_for(from_name, node, pulse)
            for a in actions:
                q.append(a)
        print(lows, highs)

    print("-------")
    return highs * lows

sample = solve(SAMPLE)
if sample != SAMPLE_EXPECTED:
    print("SAMPLE FAILED: ", sample, " != ", SAMPLE_EXPECTED)
assert sample == SAMPLE_EXPECTED
print("\n*** SAMPLE PASSED ***\n")

solved = solve(REAL)
print("SOLUTION: ", solved)