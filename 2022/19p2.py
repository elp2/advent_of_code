from collections import defaultdict, deque, Counter
from itertools import combinations, combinations_with_replacement, permutations
from functools import reduce
import math
# import numpy as np
from operator import add, mul, itemgetter, attrgetter
import re

MAX_BUILDABLE_GEODES={}


DS = [[-1, 0], [1, 0], [0, 1], [0, -1]]
DS8 = DS + [[-1, -1], [1, -1], [-1, 1], [1, 1]]
def arounds_inside(x, y, diagonals, w, h):
    ret = []
    for dx, dy in DS8 if diagonals else DS:
        ret.append((x + dx, y + dy))


CHALLENGE_DAY = "19"
REAL = open(CHALLENGE_DAY + ".txt").read()

SAMPLE_EXPECTED = 56 * 62
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
    return ret[:3]

END_SECONDS = 33
def bp(b):
    def can_afford(a, b, robot):
        return a >= robot[0] and b >= robot[1]
    
    num, ore_robot_cost, clay_robot_cost, obs_robot_cost, geode_robot_cost = b

    q = deque()
    q.append((0, 0, 1, 0, 0, 0, 0, 0, 0))

    max_geodes = -1

    def need_obs(s, obs, obsr):
        s = END_SECONDS - s
        # Can we buy a geode robot every turn until the end?
        obs_needed = s * geode_robot_cost[1]
        obs_ending = s * obsr + obs
        obs_remaining = obs_ending - obs_needed
        return obs_remaining < 0

    def need_ore(s, ore, orer):
        # Can we buy a geode robot every turn until the end?
        s = END_SECONDS - s

        ore_needed = s * geode_robot_cost[0]
        ore_ending = s * orer + ore
        ore_remaining = ore_ending - ore_needed
        return ore_remaining < 0


    def advance(state, elapsed, dore, dclay, dobs, dgeode):
        s, ore, orer, c, cr, obs, obsr, g, gr = state

        s += elapsed
        ore += orer * elapsed
        if dore:
            ore -= ore_robot_cost
        elif dclay:
            ore -= clay_robot_cost
        elif dobs:
            ore -= obs_robot_cost[0]
        elif dgeode:
            ore -= geode_robot_cost[0]
        c += cr * elapsed - dobs * obs_robot_cost[1]
        obs += obsr * elapsed - dgeode * geode_robot_cost[1]
        g += gr * elapsed
        assert ore >= 0
        assert c >= 0
        assert obs >= 0

        return (s, ore, orer + dore, c, cr + dclay, obs, obsr + dobs, g, gr + dgeode)

    def secs_to_afford_and_build(a, b, buya, buyb, arobots, brobots): 
        if arobots == 0 or brobots == 0:
            return None

        secs = 0
        while True:
            gapa = buya - a
            gapb = buyb - b
            if gapa <= 0 and gapb <= 0:
                return secs + 1 # 1 sec for building
            secs += 1
            a += arobots
            b += brobots

    maxs = 0
    seens = set()
    i = 0
    while len(q):
        i += 1
        if i == 100000:
            print(len(q), len(seens), max_geodes, maxs)
            i = 0
        state = q.popleft()
        s, ore, orer, c, cr, obs, obsr, g, gr = state

        maxs = max(s, maxs)
        max_geodes = max(g, max_geodes)

        if s == END_SECONDS:
            continue
        assert s < END_SECONDS

        # Wait until buy geode
        elapsed = secs_to_afford_and_build(ore, obs, geode_robot_cost[0], geode_robot_cost[1], orer, obsr)
        if elapsed != None and elapsed + s < END_SECONDS:
            ns = advance(state, elapsed, 0, 0, 0, 1)
            if ns not in seens:
                seens.add(ns)
                q.append(ns)
            if elapsed <= 1:
                continue

        # Wait until we have enough to buy an ore miner
        if need_ore(s, ore, orer):
            elapsed = secs_to_afford_and_build(ore, ore, ore_robot_cost, ore_robot_cost, orer, orer)
            if elapsed != None and elapsed + s < END_SECONDS:
                ns = advance(state, elapsed, 1, 0, 0, 0)
                if ns not in seens:
                    seens.add(ns)
                    q.append(ns)
        

        #  Wait until can buy obs
        if need_obs(s, obs, obsr):
            elapsed = secs_to_afford_and_build(ore, c, obs_robot_cost[0], obs_robot_cost[1], orer, cr)
            if elapsed != None and elapsed + s < END_SECONDS:
                ns = advance(state, elapsed, 0, 0, 1, 0)
                if ns not in seens:
                    seens.add(ns)
                    q.append(ns)

            # Wait until can buy a clay (don't need it if we don't need obs)
            elapsed = secs_to_afford_and_build(ore, ore, clay_robot_cost, clay_robot_cost, orer, orer)
            if elapsed != None and elapsed + s < END_SECONDS:
                ns = advance(state, elapsed, 0, 1, 0, 0)
                if ns not in seens:
                    seens.add(ns)
                    q.append(ns)



        if gr > 0:
            elapsed = END_SECONDS - s
            if elapsed != None and elapsed + s < END_SECONDS:
                ns = advance(state, elapsed, 0, 0, 0, 0)
                if ns not in seens:
                    seens.add(ns)
                    q.append(ns)


    return max_geodes


def solve(raw):
    blueprints = parse_lines(raw)
    ret = []

    for b in blueprints:
        print(b)
        geodes = bp(b)
        ret.append(geodes)
    print(ret)
    return reduce(mul, ret)

if SAMPLE_EXPECTED != None:
    sample = solve(SAMPLE)
    if sample != SAMPLE_EXPECTED:
        print("SAMPLE FAILED: ", sample, " != ", SAMPLE_EXPECTED)
    assert sample == SAMPLE_EXPECTED
    print("\n*** SAMPLE PASSED ***\n")
else:
    print("Skipping sample")

solved = solve(REAL)
assert solved > 12960
print("SOLUTION: ", solved)
