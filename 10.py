from collections import defaultdict, deque
from itertools import combinations, combinations_with_replacement, permutations
import math
import numpy as np
from operator import add, mul, itemgetter, attrgetter
import re
def flatten(t):
    return [item for sublist in t for item in sublist]
ON_TEXT = '\u2588'
OFF_TEXT = '\u2592'

DAY = "10"
REAL = open(DAY + ".in").read()

SAMPLE_EXPECTED = None


def solve(raw, pair):
    lines = raw.split("\n")
    ret = 0

    bots = defaultdict(lambda: [])
    outs = defaultdict(lambda: [])

    part1 = None

    while len(lines):
        before = len(lines)
        for line in lines:
            split = line.split(" ")
            if "goes" in split:
                value = int(split[1])
                botnum = int(split[5])
                bots[botnum].append(value)
                bots[botnum] = sorted(bots[botnum])
                lines.remove(line)
                print(botnum, "<-", value)
                break
            elif "gives" in split:
                gbot = int(split[1])

                if len(bots[gbot]) == 2:
                    lines.remove(line)
                else:
                    continue
                    
                high = bots[gbot][-1]
                low = bots[gbot][0]
                bots[gbot] = bots[gbot][1:-1]
                if (high, low) == pair:
                    part1 = gbot

                low_dest = int(split[6])
                high_dest = int(split[11])
                if split[5] == "output":
                    outs[low_dest].append(low)
                    outs[low_dest] = sorted(outs[low_dest])
                else:
                    bots[low_dest].append(low)
                    bots[low_dest] = sorted(bots[low_dest])            
                if split[10] == "output":
                    outs[high_dest].append(high)
                    outs[high_dest] = sorted(outs[high_dest])
                else:
                    bots[high_dest].append(high)
                    bots[high_dest] = sorted(bots[high_dest])            
                break
            else:
                assert False
        print(len(lines))
        if len(lines) == before:
            print("not moving")
        if len(outs[0] + outs[1] + outs[2]) == 3:
            return part1, outs[0][0] * outs[1][0] * outs[2][0]

    assert False
    return ret

if SAMPLE_EXPECTED != None:
    SAMPLE = open(DAY + ".sample").read()
    sample = solve(SAMPLE)
    if sample != SAMPLE_EXPECTED:
        print("SAMPLE FAILED: ", sample, " != ", SAMPLE_EXPECTED)
    assert sample == SAMPLE_EXPECTED
    print("\n*** SAMPLE PASSED ***\n")
else:
    print("Skipping sample")

solved = solve(REAL, (61, 17))
print("SOLUTION: ", solved)

try:
    import pandas as pd
    df=pd.DataFrame([str(solved)])
    df.to_clipboard(index=False,header=False)
    print("COPIED TO CLIPBOARD")
except ModuleNotFoundError:
    print("Pandas not installed.")