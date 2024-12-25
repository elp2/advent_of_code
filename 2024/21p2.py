from collections import defaultdict, deque, Counter
from itertools import combinations, combinations_with_replacement, permutations, product
from functools import reduce, cmp_to_key
from operator import add, mul, itemgetter, attrgetter
import os
from parse import parse
import sys

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, root_dir)
from aoc_elp import *

######################
SAMPLE_EXPECTED = 126384
######################
assert SAMPLE_EXPECTED != None, "Must enter sample value"

def parse_group(group):
    lines = group.split("\n")
    ret = []
    for y, line in enumerate(lines):
        line = line.strip()
        assert len(line) != 0

        split = line.split(" ")

        for x, xc in enumerate(split):
            pass

        assert len(split) != 0
        ret.append(split)

    return ret


def parse_lines(raw):
    # Groups.
    # groups = raw.split("\n\n")
    # Do something with the groups.

    return raw.split("\n")

def buttonify(s):
    split = s.split("\n")
    ret = {}
    for y, row in enumerate(split):
        for x, xc in enumerate(row):
            if xc != " ":
                nexts = {}
                for dx, dy, char in [(0, 1, "v"), (0, -1, "^"), (1, 0, ">"), (-1, 0, "<")]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < len(row) and 0 <= ny < len(split) and split[ny][nx] != " ":
                        nexts[char] = split[ny][nx]
                    ret[xc] = nexts

    return ret


# +---+---+---+
# | 7 | 8 | 9 |
# +---+---+---+
# | 4 | 5 | 6 |
# +---+---+---+
# | 1 | 2 | 3 |
# +---+---+---+
#     | 0 | A |
#     +---+---+
# When the robot arrives at the numeric keypad, its robotic arm is pointed at the A button in the bottom right corner.
NUMERIC = buttonify("""789
456
123
 0A""")

#     +---+---+
#     | ^ | A |
# +---+---+---+
# | < | v | > |
# +---+---+---+
DIRECTIONAL = buttonify(""" ^A
<v>""")


lencache = {}
def best_len(start, end, depth, maxdepth = 25):
    # if start == end and depth == maxdepth - 1:
    #     return 0
    if depth >= maxdepth:
        return 1
    global lencache
    if depth == 0:
        keys = NUMERIC
    else:
        keys = DIRECTIONAL
    
    if (start, end, depth) in lencache:
        return lencache[(start, end, depth)]
    
    best = defaultdict(lambda: float('inf'))
    q = deque()
    q.append((start, 0, "A"))
    visited = set()

    while q:
        at, cost, path = q.popleft()
        visited.add(at)
        # print(" * " * (depth), "[",at, "] cost: ", cost, "D:", depth, path)

        # if cost > best[at]:
        #     continue
        if at == end:
            prevdir = path[-1]
            best[at] = min(best[at], cost + best_len(prevdir, "A", depth + 1, maxdepth))
            # if depth == 0: print("BEST", at, best[at], path)
            continue
        else:
            best[at] = min(cost, best[at])

        for dir, next in keys[at].items():
            prevdir = path[-1]
            nextpath = path + dir
            nextcost = best_len(prevdir, dir, depth + 1, maxdepth)
            # if best[next] < nextcost: continue
            if next in visited:
                continue
                # if best[next] <= nextcost:
                #     continue
            q.append((next, cost + nextcost, nextpath))
    
    ret = best[end]
    lencache[(start, end, depth)] = ret

    if depth == 0:
        print("d0")
        pass
    return ret


def solve(raw, maxdepth):
    global lencache
    lencache = {}

    parsed = parse_lines(raw)
    print(parsed)

    ret = 0

    for code in parsed:
        minlen = 0
        codey = "A" + code
        for ci in range(len(codey) - 1):
            f, t = codey[ci], codey[ci + 1]
            bl = best_len(f, t, 0, maxdepth)

            minlen += bl
            print("!!!", f, t, bl, minlen)
        
        a, b = minlen, int(code[:3])
        print(code, a, b)
        ret += a * b


    return ret


# s1 = solve("379A", 3)
# assert s1 == 64 * 379, "Sample Result %s != %s expected" % (s1, 64 * 379)
# print("\n*** SAMPLE PASSED ***\n")

print(f"Checking transitions from '4': {NUMERIC['4']}")
bl22 = best_len("4", "0", 0, 3)
#bl22 = best_len("4", "0", 0, 3)
print("BL22: ", bl22)

for d in range(3):
    print("------")
    for k, v in lencache.items():
        if k[2] == d:
            print(k, v)

assert bl22 == 22

# s540a = solve("540A", 3)
# if s540a != 72 * 540:



if __name__ == "__main__":
    SAMPLE, REAL = get_raw_inputs(sys.argv)

    s1 = solve("379A", 3)
    assert s1 == 64 * 379, "Sample Result %s != %s expected" % (s1, 64 * 379)
    print("\n*** SAMPLE PASSED ***\n")

    sample = solve(SAMPLE, 3)
    assert sample == SAMPLE_EXPECTED, "Sample Result %s != %s expected" % (sample, SAMPLE_EXPECTED)
    print("\n*** SAMPLE PASSED ***\n")


    SOLVES="""279A 72 279
341A 72 341
459A 74 459
540A 72 540
085A 66 85"""
    for line in SOLVES.split("\n"):
        code, l, cnum = line.split(" ")
        expected = int(l) * int(cnum)
        actual = solve(code, 3)
        if expected != actual:
            assert expected == actual
            print(code, "OK")


    solved = solve(REAL, 3)
    print("SOLUTION 1: ", solved)
    assert solved == 123096

    lencache = {}
    solved = solve(REAL, 26)
    assert solved > 65032594029834
    print("SOLUTION 2: ", solved)
