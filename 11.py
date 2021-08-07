from collections import defaultdict, deque
from copy import deepcopy
from itertools import combinations, combinations_with_replacement, permutations
import math
import numpy as np
from operator import add, mul, itemgetter, attrgetter
import re
def flatten(t):
    return [item for sublist in t for item in sublist]
ON_TEXT = '\u2588'
OFF_TEXT = '\u2592'

DAY = "11"

EXAMPLE="""F4 .  .  .  .  .
F3 .  .  .  LG .
F2 .  HG .  .  .
F1 E  .  HM .  LM
Then, to get everything up to the assembling machine on the fourth floor, the following steps could be taken:

Bring the Hydrogen-compatible Microchip to the second floor, which is safe because it can get power from the Hydrogen Generator:

F4 .  .  .  .  .
F3 .  .  .  LG .
F2 E  HG HM .  .
F1 .  .  .  .  LM
Bring both Hydrogen-related items to the third floor, which is safe because the Hydrogen-compatible microchip is getting power from its generator:

F4 .  .  .  .  .
F3 E  HG HM LG .
F2 .  .  .  .  .
F1 .  .  .  .  LM
Leave the Hydrogen Generator on floor three, but bring the Hydrogen-compatible Microchip back down with you so you can still use the elevator:

F4 .  .  .  .  .
F3 .  HG .  LG .
F2 E  .  HM .  .
F1 .  .  .  .  LM
At the first floor, grab the Lithium-compatible Microchip, which is safe because Microchips don't affect each other:

F4 .  .  .  .  .
F3 .  HG .  LG .
F2 .  .  .  .  .
F1 E  .  HM .  LM
Bring both Microchips up one floor, where there is nothing to fry them:

F4 .  .  .  .  .
F3 .  HG .  LG .
F2 E  .  HM .  LM
F1 .  .  .  .  .
Bring both Microchips up again to floor three, where they can be temporarily connected to their corresponding generators while the elevator recharges, preventing either of them from being fried:

F4 .  .  .  .  .
F3 E  HG HM LG LM
F2 .  .  .  .  .
F1 .  .  .  .  .
Bring both Microchips to the fourth floor:

F4 E  .  HM .  LM
F3 .  HG .  LG .
F2 .  .  .  .  .
F1 .  .  .  .  .
Leave the Lithium-compatible microchip on the fourth floor, but bring the Hydrogen-compatible one so you can still use the elevator; this is safe because although the Lithium Generator is on the destination floor, you can connect Hydrogen-compatible microchip to the Hydrogen Generator there:

F4 .  .  .  .  LM
F3 E  HG HM LG .
F2 .  .  .  .  .
F1 .  .  .  .  .
Bring both Generators up to the fourth floor, which is safe because you can connect the Lithium-compatible Microchip to the Lithium Generator upon arrival:

F4 E  HG .  LG LM
F3 .  .  HM .  .
F2 .  .  .  .  .
F1 .  .  .  .  .
Bring the Lithium Microchip with you to the third floor so you can use the elevator:

F4 .  HG .  LG .
F3 E  .  HM .  LM
F2 .  .  .  .  .
F1 .  .  .  .  .
Bring both Microchips to the fourth floor:

F4 E  HG HM LG LM
F3 .  .  .  .  .
F2 .  .  .  .  .
F1 .  .  .  .  . """


# The first floor contains a strontium generator, a strontium-compatible microchip,
#    a plutonium generator, and a plutonium-compatible microchip.
# The second floor contains a thulium generator, a ruthenium generator,
#    a ruthenium-compatible microchip, a curium generator, and a curium-compatible microchip.
# The third floor contains a thulium-compatible microchip.
# The fourth floor contains nothing relevant.
REAL = [set(["SG", "SM", "PG", "PM"]),
        set(["TG", "RG", "RM", "CG", "CM"]), set(["TM"]), set()]
# F4 .  .  .  .  .
# F3 .  .  .  LG .
# F2 .  HG .  .  .
# F1 E  .  HM .  LM

SAMPLE = [set(["HM", "LM"]), set(["HG"]), set(["LG"]), set()]
SAMPLE_EXPECTED = 11

def moves_for_state(state, floor):
    moves = []
    items_at = state[floor]

    # The elevator always stops on each floor to recharge, 
    # and this takes long enough that the items within it and the items on that floor
    # can irradiate each other.
    hgens = [g for g in items_at if g[1] == "G"]
    hchips = [c for c in items_at if c[1] == "M"]
    for c in hchips:
        if hgens and c[0] + "G" not in hgens:
            return []

    for i in [1, 2]:
        poss = combinations(items_at, i)
        for p in poss:
            p = set(p)
            valid = True
            after = items_at - p
            agens = [g for g in after if g[1] == "G"]
            achips = [c for c in after if c[1] == "M"]
            for c in achips:
                if agens and c[0] + "G" not in agens:
                    valid = False # Would leave a chip with wrong generator
                    break
            if valid:
                if floor > 0:
                    move = deepcopy(state)
                    move[floor] = after
                    move[floor - 1] |= p
                    moves.append((move, floor - 1))
                if floor < 3:
                    move = deepcopy(state)
                    move[floor] = after
                    move[floor + 1] |= p
                    moves.append((move, floor + 1))
            #if not valid:
            #     print(after, valid)
    return moves


def get_expecteds():
    """Extract expected path to see where I'm losing it."""
    i = 0
    states = []
    lines = EXAMPLE.split("\n")
    depth = 0
    while i < len(lines):
        if lines[i].startswith("F4"):
            state_lines = lines[i:i + 4]
            state_lines.reverse()
            state = []
            at = None
            for f in range(4):
                line = state_lines[f].split(" ")
                here = set()
                for item in line:
                    if item in ["F1", "F2", "F3", "F4", "."]:
                        continue
                    if not item:
                        continue
                    if "E" == item:
                        at = f
                    else:
                        here.add(item.strip())
                state.append(here)
            states.append((state, at))
            i += 4
        else:
            i += 1

    return states




def solve(raw, check_expecteds=False):
    ret = 0
    bests = set()

    depth = 0
    moves = [(raw, 0)]
    #moves = [([{'LM'}, {'HM'}, {'LG', 'HG'}, set()], 1)]

    target = len(flatten(raw))

    expected = get_expecteds()
    print("Expect: ", len(expected))

    while True:
        print("----- ", depth, "-----")
        if check_expecteds:
            if expected[depth] not in moves:
                print("Want: ", expected[depth])
                print("Fail depth=", depth)
                print("From: ", expected[depth-1], "\nto:")
                for m in moves:
                    if m[1] == 0:
                        print(m[0][0], m[0])
            assert expected[depth] in moves
        print(depth, len(moves))
        new_moves = []
        for m, floor in moves:
            assert len(flatten(m)) == target
            if len(m[3]) == target:
                print("Done at ", m, floor, depth)
                return depth
            if str(m) + str(floor) in bests:
                # print("Already seen: ", m)
                continue
            bests.add(str(m) + str(floor))
            new_moves += moves_for_state(m, floor)

        moves = new_moves
        depth += 1

    return ret

if SAMPLE_EXPECTED != None:
    sample = solve(SAMPLE, True)
    if sample != SAMPLE_EXPECTED:
        print("SAMPLE FAILED: ", sample, " != ", SAMPLE_EXPECTED)
    assert sample == SAMPLE_EXPECTED
    print("\n*** SAMPLE PASSED ***\n")
else:
    print("Skipping sample")

solved = solve(REAL)
print("SOLUTION: ", solved)

try:
    import pandas as pd
    df=pd.DataFrame([str(solved)])
    df.to_clipboard(index=False,header=False)
    print("COPIED TO CLIPBOARD")
except ModuleNotFoundError:
    print("Pandas not installed.")
