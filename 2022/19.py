from collections import defaultdict, deque, Counter
from itertools import combinations, combinations_with_replacement, permutations
from functools import reduce
import math
# import numpy as np
from operator import add, mul, itemgetter, attrgetter
import re

DS = [[-1, 0], [1, 0], [0, 1], [0, -1]]
DS8 = DS + [[-1, -1], [1, -1], [-1, 1], [1, 1]]
def arounds_inside(x, y, diagonals, w, h):
    ret = []
    for dx, dy in DS8 if diagonals else DS:
        ret.append((x + dx, y + dy))


CHALLENGE_DAY = "19"
REAL = open(CHALLENGE_DAY + ".txt").read()

SAMPLE_EXPECTED = 33
if SAMPLE_EXPECTED:
    SAMPLE = open(CHALLENGE_DAY + ".s.txt").read()


def parse_lines(raw):
    lines = raw.split("\n")
    ret = []

    for l in lines:
        s = l.split(" ")
        num = int(s[1].replace(":", ""))
        ore_ore = int(s[6])
        clay_ore = int(s[12])
        obs_ore = int(s[18])
        obs_clay = int(s[21])
        geo_ore = int(s[27])
        geo_clay = int(s[30])

        ret.append((num, ore_ore, clay_ore, (obs_ore, obs_clay), (geo_ore, geo_clay)))
    return ret

END_SECONDS = 24
def bp(b):
    def can_afford(a, b, robot):
        return a >= robot[0] and b >= robot[1]
    
    num, ore_robot_cost, clay_robot_cost, obs_robot_cost, geode_robot_cost = b

    q = deque()
    q.append((0, 0, 1, 0, 0, 0, 0, 0, 0))

    max_geodes = -1
    i = 0
    bests = {}
    secs_seen = defaultdict(lambda: 0)
    max_ore = max(obs_robot_cost[0], max(ore_robot_cost, max(clay_robot_cost, geode_robot_cost[0]))) +1
    while len(q):
        i += 1
        if i == 10000000:
            print(len(q), len(bests), secs_seen, max_geodes)
            i = 0
        s, ore, orer, c, cr, obs, obsr, g, gr = q.popleft()
        aore = ore + orer
        asec = s + 1
        ac = c + cr
        aobs = obs + obsr
        ag = g + gr
        secs_seen[s] += 1
        max_geodes = max(max_geodes, g)
        if s == END_SECONDS:
            continue
        # Buy a ore if possible

        if s >= 20:
            if g < max_geodes // 2:
                continue


        if can_afford(ore, obs, geode_robot_cost):
            q.append((asec, aore - geode_robot_cost[0], orer, ac, cr, aobs - geode_robot_cost[1], obsr, ag, gr + 1))
            continue

        if ore >= ore_robot_cost:
            q.append((asec, aore - ore_robot_cost, orer + 1, ac, cr, aobs, obsr, ag, gr))

        # Buy a clay
        if ore >= clay_robot_cost:
            q.append((asec, aore - clay_robot_cost, orer, ac, cr + 1, aobs, obsr, ag, gr))

        # Buy obsidian
        if can_afford(ore, c, obs_robot_cost):
            q.append((asec, aore - obs_robot_cost[0], orer, ac - obs_robot_cost[1], cr, aobs, obsr + 1, ag, gr))

        # Buy a geode
        if ore < max_ore:
            q.append((asec, aore, orer, ac, cr, aobs, obsr, ag, gr))


    return max_geodes


def solve(raw):
    blueprints = parse_lines(raw)
    ret = []

    for b in blueprints:
        print(b)
        ql = bp(b)
        ret.append(ql * b[0])

    return sum(ret)

if SAMPLE_EXPECTED != None:
    sample = solve(SAMPLE)
    if sample != SAMPLE_EXPECTED:
        print("SAMPLE FAILED: ", sample, " != ", SAMPLE_EXPECTED)
    assert sample == SAMPLE_EXPECTED
    print("\n*** SAMPLE PASSED ***\n")
else:
    print("Skipping sample")

solved = solve(REAL)
print("SOLUTION: ", solved)
