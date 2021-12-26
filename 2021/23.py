from collections import defaultdict, deque, Counter
from itertools import combinations, combinations_with_replacement, permutations
from functools import reduce
import math
# import numpy as np
from operator import add, mul, itemgetter, attrgetter
import re
from typing import DefaultDict

DS = [[-1, 0], [1, 0], [0, 1], [0, -1]]
DS8 = DS + [[-1, -1], [1, -1], [-1, 1], [1, 1]]
def arounds_inside(x, y, diagonals, w, h):
    ret = []
    for dx, dy in DS8 if diagonals else DS:
        ret.append((x + dx, y + dy))


CHALLENGE_DAY = "23"
REAL = ("BC", "AD", "BD", "CA", "           ", 0)


SAMPLE_EXPECTED = 12521
if SAMPLE_EXPECTED:
    SAMPLE = ("BA", "CD", "BC", "DA", "           ", 0)


HOMES = {"A": (0, 2), "B": (1, 4), "C": (2, 6), "D": (3, 8)}
HOME_FOR = ["A", "B", "C", "D"]
COSTS = {"A": 1, "B": 10, "C": 100, "D": 1000}

def move_cost(pod, f, to):
    fx, fy = f
    tx, ty = to
    dist = abs(fx - tx) + abs(fy - ty)
    return COSTS[pod] * dist


def validate(state):
    seens = DefaultDict(lambda: 0)
    for i in range(5):
        h = state[i]
        for c in h:
            seens[c] += 1
    for c in "ABCD":
        assert seens[c] == 2 # ('BA', 'CD', 'BC', '  ', '   D     A ', 6003)

def is_blocked(corridor, dx, hx):
    if dx > hx:
        path = corridor[hx + 1:dx + 1]
    else:
        path = corridor[dx:hx]
    blocked = any(pc != " " for pc in path)


def receiver_y(pod, room):
    if room[1] == " ":
        return 2
    elif room[1] == pod and room[0] == " ":
        return 1
    else:
        return 0
        

def moves(state):
    ms = []
    # If won, return
    if state[0] == "AA" and state[1] == "BB" and state[2] == "CC" and state[3] == "DD":
        return [state[5]]
    
    corridor = state[4]
    # Move things in corridor into their right room
    for x, c in enumerate(corridor):
        if c != " ":
            hi, hx = HOMES[c]
            homearr = state[hi]
            if homearr[1] not in [" ", c] or homearr[0] not in [" ", c]:
                continue
            if hx > x:
                path = corridor[x +1:hx + 1]
            else:
                path = corridor[hx:x]
            blocked = any(pc != " " for pc in path)
            if blocked:
                continue

            hy = 2 if homearr[1] == " " else 1
            newcorr = corridor[:x] + " " + corridor[x + 1:]
            newhome = " " + c if hy == 2 else c + c
            next = []
            for i in range(4):
                if i == hi:
                    next.append(newhome)
                else:
                    next.append(state[i])
            next.append(newcorr)

            newcost = state[5] + move_cost(c, (x, 0), (hx, hy))
            next.append(newcost)

            validate(next)
            ms.append(tuple(next))

    # Move things in starting room into cooridor
    for hi in range(4):
        expected_pod = HOME_FOR[hi]
        _, hx = HOMES[expected_pod]
        homearr = state[hi]
        top_ok = homearr[0] in [" ", expected_pod]
        bot_ok = homearr[1] in [" ", expected_pod]
        if top_ok and bot_ok:
            continue
        if not top_ok:
            hy = 1
            move = homearr[0]
        elif not bot_ok:
            if homearr[0] == " ":
                hy = 2
                move = homearr[1]
            else:
                hy = 1
                move = homearr[0]
        else:
            assert False

        # mi, mx = HOMES[move]
        # rec = receiver_y(move, state[mi])
        # if rec != 0:
            
               
        for dx in range(len(corridor)):
            if dx in [2, 4, 6, 8]:
                continue # can't block room entrance
            if corridor[dx] != " ":
                continue # something there
            if dx > hx:
                path = corridor[hx + 1:dx + 1]
            else:
                path = corridor[dx:hx]
            blocked = any(pc != " " for pc in path)
            if blocked:
                continue
            
            newcorr = corridor[:dx] + move + corridor[dx + 1:]
            newhome = " " + homearr[1] if hy == 1 else "  "
            next = []
            for i in range(4):
                if i == hi:
                    next.append(newhome)
                else:
                    next.append(state[i])
            next.append(newcorr)

            newcost = state[5] + move_cost(move, (dx, 0), (hx, hy))
            next.append(newcost)

            validate(next)
            ms.append(tuple(next))

    return ms

moves(('AA', 'BB', 'CC', 'DD', '           ', 12521))


def best_possible_cost(state):
    corr = state[4]
    ret = 0
    for x, pod in enumerate(corr):
        if pod == " ":
            continue
        _, hx = HOMES[pod]
        ret += move_cost(pod, (x, 0), (hx, 0))

    for ri in range(4):
        _, hx = HOMES[HOME_FOR[ri]]
        for hy in range(2):
            actual_pod = state[ri][hy]
            expected_pod = HOME_FOR[ri]
            if actual_pod != expected_pod:
                ret += (hy + 1) * COSTS[expected_pod]
                if actual_pod != " ":
                    ret += (hy + 1) * COSTS[actual_pod]
                    _, ax = HOMES[actual_pod]
                    ret += COSTS[actual_pod] * abs(ax - hx)

    return ret

def solve(state):
    ret = None
    q = deque()
    q.append(state)
    d = 0
    while len(q) != 0:
        # print(len(q))
        state = q.popleft()
        best_cost = best_possible_cost(state) + state[5]
        if ret != None and best_cost >= ret:
            continue

        d += 1
        if d % 100000 == 0:
            print(state, ret, len(q))

        for m in moves(state):
            if type(m) == int:
                if ret == None or m < ret:
                    ret = m
            else:
                q.appendleft(m)
                # q.append(m)

    return ret

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
