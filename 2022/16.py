from collections import defaultdict, deque, Counter
from itertools import combinations, combinations_with_replacement, permutations
from functools import reduce
import math
import numpy as np
from operator import add, mul, itemgetter, attrgetter
import re

DS = [[-1, 0], [1, 0], [0, 1], [0, -1]]
DS8 = DS + [[-1, -1], [1, -1], [-1, 1], [1, 1]]
def arounds_inside(x, y, diagonals, w, h):
    ret = []
    for dx, dy in DS8 if diagonals else DS:
        ret.append((x + dx, y + dy))


CHALLENGE_DAY = "16"
REAL = open(CHALLENGE_DAY + ".txt").read()

SAMPLE_EXPECTED = 1651
if SAMPLE_EXPECTED:
    SAMPLE = open(CHALLENGE_DAY + ".s.txt").read()


def parse_lines(raw, solve_row):
    sensor_exclusion = {}
    lines = raw.split("\n")

    ret = []
    order_mapping = {}
    for i in range(len(lines)):
        name = lines[i].split(" ")[1]
        order_mapping[name] = i
    # Valve AW has flow rate=0; tunnels lead to valves DS, AA
    for l in lines:
        # Valve AW has flow rate=0; tunnels lead to valves DS, AA
        l = l.replace(";", "")
        l = l.replace(",", "")
        l = l.replace("=", " ")

        ls = l.split(" ")
        f = ls[1]
        rate = int(ls[5])
        dests = list(map(lambda d: order_mapping[d], ls[10:]))
        ret.append((f, rate, dests))

    distances = {}
    for i in range(len(lines)):
        q = deque()
        q.append((i, 0))
        idists = {}
        while len(q):
            at, dist = q.popleft()
            if at in idists:
                continue
            idists[at] = dist
            for n in ret[at][2]:
                q.append((n, dist + 1))
        distances[i] = idists

    return ret, distances

def solve(raw, solve_row):
    pipes, distances = parse_lines(raw, solve_row)
    flows = list(map(lambda p: p[1], pipes))
    bests = defaultdict(lambda: -1)

    max_flow = 0
    q = deque([(0, tuple(flows), 30, 0)])
    i = 0
    while len(q):
        i += 1
        if i % 10000 == 0:
            print(i, len(q))
        # Get a next state off the queue
        at, state, secs, end_flow = q.popleft()
        if secs == 0:
            continue
        max_flow = max(end_flow, max_flow)

        if bests[(at, state)] >= end_flow:
            continue
        bests[(at, state)] = end_flow

        # Is this worse than we have already seen? Continue
        # Worse? Less flow, same opens

        # Try Options:
        # If the current room is not on and > 0 flow, start it on, put flow in for 30 - secs - 1 more
        if state[at] > 0 and secs >= 2:
            lstate = list(state)
            newflow = end_flow + lstate[at] * (secs - 1)
            lstate[at] = 0
            q.append((at, tuple(lstate), secs - 1, newflow))
        
        # Try going to any other room
        for d in pipes[at][2]:
            q.append((d, state, secs - 1, end_flow))
    return max_flow

if SAMPLE_EXPECTED != None:
    sample = solve(SAMPLE, 10)
    if sample != SAMPLE_EXPECTED:
        print("SAMPLE FAILED: ", sample, " != ", SAMPLE_EXPECTED)
    assert sample == SAMPLE_EXPECTED
    print("\n*** SAMPLE PASSED ***\n")
else:
    print("Skipping sample")

solved = solve(REAL, 2000000)
print("SOLUTION: ", solved)
