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


CHALLENGE_DAY = "18"
REAL = open(CHALLENGE_DAY + ".txt").read()

SAMPLE_EXPECTED = 4140
if SAMPLE_EXPECTED:
    SAMPLE = open(CHALLENGE_DAY + ".s.txt").read()


def parse_lines(raw):
    lines = raw.split("\n")
    ret = []
    for l in lines:
        l = l.replace(",", "")
        l = [int(x) if x in "0123456789" else x for x in l]
        ret.append(l)
    return ret # raw



def split(x):
    return ["[", x // 2, x - x // 2, "]"]

assert split(10) == ["[", 5, 5, "]"]
assert split(11) == ["[", 5, 6, "]"]
assert split(12) == ["[", 6, 6, "]"]


def add(x, y):
    return ["["] + x + y + ["]"]



def mag(x):
    if type(x) == int:
        return x
    a, b = x
    return 3 * mag(a) + 2 * mag(b)



assert mag(eval("[[1,2],[[3,4],5]]")) == 143
assert mag(eval("[[[[5,0],[7,4]],[5,5]],[6,6]]")) == 1137


def prettyp(x):
    ret = ""
    for i, c in enumerate(x):
        if c == "[":
            ret += "["
        elif c == "]":
            ret += "]"
            if i < len(x) - 1 and x[i + 1] != "]":
                ret += ","
        elif type(c) == int:
            ret += str(c)
            if x[i + 1] != "]":
                ret +=","

    return ret

def reduce(x):
    reduced = False

    depth = 0
    for i, c in enumerate(x):
        if c == "[":
            depth += 1
        elif c == "]":
            depth -= 1
    assert depth == 0


    for i, c in enumerate(x):
        if c == "[":
            depth += 1
        elif c == "]":
            depth -= 1
        else:
            if depth >= 5:
                l = x[i]
                r = x[i + 1]

                bef = x[:i - 1]
                for il in range(len(bef) - 1, -1, -1):
                    if type(bef[il]) == int:
                        bef[il] += l
                        break

                aft = x[i + 3:]
                for ir in range(len(aft)):
                    if type(aft[ir]) == int:
                        aft[ir] += r
                        break

                #print("Explode!")
                ret = bef + [0] + aft
                assert len(ret) == len(x) + 1 - 4
                return ret, True

    for i, c in enumerate(x):
        if c == "[":
            depth += 1
        elif c == "]":
            depth -= 1
        else:
            if c >= 10:
                ret = x[:i] + split(c) + x[i + 1:]
                assert len(ret) == len(x) - 1 + 4
                # print("split!")
                return ret, True

    assert depth == 0
    return x, False

def full_reduce(raw):
    # print("Full Reduce!")
    nums = parse_lines(raw)

    ret = nums[0]
    # print("0:", prettyp(ret))
    for num in nums[1:]:
        ret = add(ret, num)
        # print("------\n", prettyp(ret))
        while True:
            ret, reduced = reduce(ret)
            # print(prettyp(ret), reduced)
            if not reduced:
                break
        # print("DONE => ", prettyp(ret))

    line = prettyp(ret)
    return line


assert "[[[[5,0],[7,4]],[5,5]],[6,6]]" == full_reduce("""[1,1]
[2,2]
[3,3]
[4,4]
[5,5]
[6,6]""")

assert "[[[[0,7],4],[[7,8],[6,0]]],[8,1]]" == full_reduce("""[[[[4,3],4],4],[7,[[8,4],9]]]
[1,1]""")

assert "[[[[4,0],[5,4]],[[7,7],[6,0]]],[[8,[7,7]],[[7,9],[5,0]]]]" == full_reduce("""[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]
[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]""")

assert "[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]" == full_reduce("""[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]
[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]
[[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]
[[[[2,4],7],[6,[0,5]]],[[[6,8],[2,8]],[[2,1],[4,5]]]]
[7,[5,[[3,8],[1,4]]]]
[[2,[2,2]],[8,[8,1]]]
[2,9]
[1,[[[9,3],9],[[9,0],[0,7]]]]
[[[5,[7,4]],7],1]
[[[[4,2],2],6],[8,7]]""")


def solve(raw):
    line = full_reduce(raw)
    return mag(eval(line))

if SAMPLE_EXPECTED != None:
    sample = solve(SAMPLE)
    if sample != SAMPLE_EXPECTED:
        print("SAMPLE FAILED: ", sample, " != ", SAMPLE_EXPECTED)
    assert sample == SAMPLE_EXPECTED
    print("\n*** SAMPLE PASSED ***\n")
else:
    print("Skipping sample")

def solve2(raw):
    lines = raw.split("\n")

    maxmag = 0
    for a, b in permutations(range(len(lines)), 2):
        r2 = lines[a] + "\n" + lines[b]
        maghere = mag(eval(full_reduce(r2)))
        maxmag = max(maxmag, maghere)
    print("max mag!", maxmag)
    return maxmag

assert 3993 == solve2("""[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]
[[[5,[2,8]],4],[5,[[9,9],0]]]
[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]
[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]
[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]
[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]
[[[[5,4],[7,7]],8],[[8,3],8]]
[[9,3],[[9,9],[6,[4,9]]]]
[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]
[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]""")

print("Part 2", solve2(REAL)) #4705 low

# solved = solve(REAL)
# print("SOLUTION: ", solved)
import pandas as pd
df=pd.DataFrame([str(solved)])
df.to_clipboard(index=False,header=False)
print("COPIED TO CLIPBOARD")
