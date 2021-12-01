from collections import defaultdict, deque
import re

CHALLENGE_DAY = "23"
REAL = "467528193"
SAMPLE = "389125467"
# SAMPLE_EXPECTED = None
SAMPLE_EXPECTED = "67384529"



def solve(cups):
    cups = list(cups)
    cups = list(map(int, cups))
    i = 0

    def print_cups(c, i):
        line = ""
        for idx, n in enumerate(c):
            if i == idx:
                line += " (" + str(n) + ")"
            else:
                line += " " + str(n)
        print("Cups: ", line)
    for move in range(1, 101):
        current = cups[i]
        print("Move: ", move)
        print_cups(cups, i)
        three = []
        if i + 3 >= len(cups):
            rem = (i + 3) % len(cups)
            three = cups[i + 1:]
            three += cups[0:rem + 1]
            cups = cups[rem + 1:i + 1]
        else:
            three = cups[i + 1:i + 4]
            cups = cups[0:i + 1] + cups[i+4:]
        assert len(three) == 3
        print(three)
        destination = current - 1
        while destination in three or destination < 1:
            destination -= 1
            if destination < 1:
                destination = max(cups)
        
        di = cups.index(destination)
        print("Dest = ", destination, "idx: ", di)
        cups = cups[:di +1] + three + cups[di + 1:]
        print(cups, i, cups[i])

        i = cups.index(current)
        i = (i + 1) % len(cups)
        for chk in range(9):
            assert chk + 1 in cups
        assert len(cups) == 9
    ret = ""
    ri = cups.index(1)
    for _ in range(8):
        ri += 1
        if ri >= len(cups):
            ri = 0
        ret += str(cups[ri])
    return ret


sample = solve(SAMPLE)
if sample != SAMPLE_EXPECTED:
    print("SAMPLE FAILED: ", sample, " != ", SAMPLE_EXPECTED)
assert sample == SAMPLE_EXPECTED
print("\n*** SAMPLE PASSED ***\n")

solved = solve(REAL)
print("SOLUTION: ", solved)
import pandas as pd
df=pd.DataFrame([str(solved)])
df.to_clipboard(index=False,header=False)
print("COPIED TO CLIPBOARD")
