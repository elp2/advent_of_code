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


  #D#C#B#A#
  #D#B#A#C#

REAL = ("BDDC", "ACBD", "BBAD", "CACA", "           ", 0)

VALIDATE=False
print("Validating: ", VALIDATE)

SAMPLE_EXPECTED = 44169
if SAMPLE_EXPECTED:
    SAMPLE = ("BDDA", "CCBD", "BBAC", "DACA", "           ", 0)


HOMES = {"A": (0, 2), "B": (1, 4), "C": (2, 6), "D": (3, 8)}
HOME_FOR = ["A", "B", "C", "D"]
COSTS = {"A": 1, "B": 10, "C": 100, "D": 1000}

def home_x(pod):
    return HOMES[HOME_FOR[pod]][1]


def move_cost(pod, f, to):
    fx, fy = f
    tx, ty = to
    dist = abs(fx - tx) + abs(fy - ty)
    return COSTS[pod] * dist


def validate(state):
    if not VALIDATE:
        return True
    seens = DefaultDict(lambda: 0)
    for i in range(5):
        h = state[i]
        if i < 4:
            assert len(h) == 4
            # for i in range(len(h)):
            #     if " " != h[i]:
            #         for j in range(i+1, len(h)):
            #             assert h[i] != " "
        else:
            assert len(h) == 11
        for c in h:
            seens[c] += 1
    for c in "ABCD":
        assert seens[c] == 4

def is_blocked(corridor, dx, hx):
    if dx > hx:
        path = corridor[hx + 1:dx + 1]
    else:
        path = corridor[dx:hx]
    blocked = any(pc != " " for pc in path)


# def state_for(changes, coor)


# def corridor_moves(state):
#     ret = []
#     corridor = state[4]
#     for x, pod in enumerate(corridor):
#         if pod == " ":
#             continue

#         desti, destx = HOMES[pod]

#         placey = None
#         for ry in range(3, -1, -1):
#             if state[desti][ry] == " ":
#                 placey = ry
#                 break
#         if placey == None:
#             continue

#         if destx > x:
#             path = path[x + 1:destx]
#         else:
#             path = path[destx + 1:x]
        
#         blocked = False
#         for o in path:
#             if o != " ":
#                 blocked = True
#                 break
#         if blocked:
#             continue
    
    


# def room_moves(state):


def moves(state):
    ms = []
    # If won, return
    if state[0] == "AAAA" and state[1] == "BBBB" and state[2] == "CCCC" and state[3] == "DDDD":
        return [state[5]]
    
    corridor = state[4]
    # Move things in corridor into their right room
    for x, c in enumerate(corridor):
        if c == " ":
            continue
        hi, hx = HOMES[c]
        if hx > x:
            path = corridor[x +1:hx + 1]
        else:
            path = corridor[hx:x]
        blocked = any(pc != " " for pc in path)
        if blocked:
            continue

        can_place = False
        homearr = list(state[hi])
        # if state[hi] == "    ":
        #     print("!")
        for hy in range(3, -1, -1):
            if homearr[hy] != c:
                if homearr[hy] == " ":
                    homearr[hy] = c
                    can_place = True
                    break
                else:
                    break
        if not can_place:
            continue
        newhome = "".join(homearr)
        next = []
        for i in range(4):
            if i == hi:
                next.append(newhome)
            else:
                next.append(state[i])
        newcorr = corridor[:x] + " " + corridor[x + 1:]

        # OPTIMIZE
        assert newcorr != corridor

        next.append(newcorr)

        newcost = state[5] + move_cost(c, (x, 0), (hx, hy + 1))
        next.append(newcost)

        validate(next)
        return [next]
        ms.append(tuple(next))

    # Move things in starting room into cooridor
    for hi in range(4):
        expected_pod = HOME_FOR[hi]
        _, hx = HOMES[expected_pod]
        movey = None
        homearr = state[hi]
        dirty = any([p not in [" ", expected_pod] for p in homearr])
        if not dirty:
            continue
        for movey in range(4):
            if homearr[movey] != " ":
                move = homearr[movey]
                break

        homearr = list(state[hi])
        homearr[movey] = " "
        newhome = "".join(homearr)
                           
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
            next = []
            for i in range(4):
                if i == hi:
                    next.append(newhome)
                else:
                    next.append(state[i])
            next.append(newcorr)

            newcost = state[5] + move_cost(move, (dx, 0), (hx, movey + 1))
            next.append(newcost)

            validate(next)
            ms.append(tuple(next))

    # if len(ms) == 0:
    #     print("!")
    return ms

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
        for hy in range(4):
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
    validate(state)
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
