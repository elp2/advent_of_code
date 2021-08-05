from collections import defaultdict, deque, Counter
from itertools import combinations, combinations_with_replacement, permutations
import math
import numpy as np
from operator import add, mul, itemgetter, attrgetter
import re

def flatten(t):
    return [item for sublist in t for item in sublist]

ON_TEXT = '\u2588'
OFF_TEXT = '\u2592'

DAY = "21"
REAL = open(DAY + ".in").read().split("\n")

SAMPLE_EXPECTED = None

def solve(lines, password, reverse=False):
    if reverse:
        lines.reverse()
    password = np.array(list(password))
    # print(password)
    for line in lines:
        before = np.copy(password)
        ls = line.split(" ")
        if ls[0] == "swap":
            # swap position X with position Y means that the letters at indexes X and Y (counting from 0) should be swapped.
            if ls[1] == "position":
                x = int(ls[2])
                y = int(ls[5])
                password[x], password[y] = password[y], password[x]
            else:
                assert ls[1] == "letter"
                # swap letter X with letter Y means that the letters X and Y should be swapped (regardless of where they appear in the string).
                x = ls[2]
                y = ls[5]
                xidx = np.where(password == x)
                yidx = np.where(password == y)
                password[xidx] = y
                password[yidx] = x
        elif ls[0] == "rotate":
            # rotate left/right X steps means that the whole string should be rotated; for example, one right rotation would turn abcd into dabc.
            if ls[1] == "right":
                steps = int(ls[2])
            elif ls[1] == "left":
                steps = -int(ls[2])
            else:
                assert ls[1] == "based"
                # rotate based on position of letter X means that the whole string should be rotated to the right based on the index of letter X (counting from 0) as determined before this instruction does any rotations. Once the index is determined, rotate the string to the right one time, plus a number of times equal to that index, plus one additional time if the index was at least 4.
                steps = np.where(password == ls[6])[0][0]
                if steps >= 4:
                    steps += 1
                steps += 1
            password = np.roll(password, -1 * steps if reverse else steps)
        elif ls[0] == "reverse":
            # reverse positions X through Y means that the span of letters at indexes X through Y (including the letters at X and Y) should be reversed in order.
            x = int(ls[2])
            y = int(ls[4])
            password[x:y+1] = password[x:y+1][::-1]
        elif ls[0] == "move":
            # move position X to position Y means that the letter which is at index X should be removed from the string, then inserted such that it ends up at index Y.
            x = int(ls[2])
            y = int(ls[5])
            if reverse:
                fa = password[y]
                t = x
            else:
                fa = password[x]
                t = y
            password = np.delete(password, np.where(password == fa))
            password = np.insert(password, t, fa)
        else:
            print(line)
            assert False

        # print(line)
        # print(before)
        # print(password)
        # if np.array_equal(before, password):
        #     print("----EQUAL----")
        assert set(before) == set(password)

    return "".join(list(password))

if SAMPLE_EXPECTED != None:
    SAMPLE = open(DAY + ".sample").read()
    sample = solve(SAMPLE)
    if sample != SAMPLE_EXPECTED:
        print("SAMPLE FAILED: ", sample, " != ", SAMPLE_EXPECTED)
    assert sample == SAMPLE_EXPECTED
    print("\n*** SAMPLE PASSED ***\n")
else:
    print("Skipping sample")

part1 = solve(REAL, "abcdefgh")
assert "bdfhgeca" == part1
print("Part 1: ", part1)

# for i in range(len(REAL)):
#     print("-----Reverse Test-----", i - 1)
#     forward = solve(REAL[:i], "abcdefgh")
#     reversed = solve(REAL[:i], forward, True)
#     if reversed != "abcdefgh":
#         print("FAIL: @ ", i - 1, REAL[i-1])
#     assert reversed == "abcdefgh"

PART2 = "fbgdceah"
for perm in permutations("abcdefgh"):
    if solve(REAL, perm) == PART2:
        print("part2: ", perm)

try:
    import pandas as pd
    df=pd.DataFrame([str(solved)])
    df.to_clipboard(index=False,header=False)
    print("COPIED TO CLIPBOARD")
except ModuleNotFoundError:
    print("Pandas not installed.")