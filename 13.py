from collections import defaultdict, deque
import re
from itertools import permutations

CHALLENGE_DAY = "13"
REAL = open(CHALLENGE_DAY + ".txt").read()
SAMPLE = open(CHALLENGE_DAY + ".sample.txt").read()
SAMPLE_EXPECTED = 330

def parse_lines(raw):
    # Groups.
    # groups = raw.split("\n\n")
    # return list(map(lambda group: group.split("\n"), groups))
    
    lines = raw.split("\n")
    ret = {}
    keys = set()
    for line in lines:
        line = line[0:-1]
        a, _, gainlose, num, _, _, _, _, _, _, b = line.split(" ")
        if gainlose == "gain":
            num = int(num)
        elif gainlose == "lose":
            num = -int(num)
        else:
            assert False
        
        ret[(a, b)] = num
        keys.add(a)
        keys.add(b)
    return ret, keys


def solve(raw, add_me=False):
    parsed, keys = parse_lines(raw)
    # Debug here to make sure parsing is good.
    ret = 0

    keys = list(keys)
    if add_me:
        for k in keys:
            parsed[("me", k)] = 0
            parsed[(k, "me")] = 0
        keys.append("me")

    rets = []
    for perm in permutations(keys):
        ret = 0
        for i in range(len(perm)):
            a = perm[i]
            b = perm[(i + 1) % len(perm)]
            ret += parsed[(a, b)]
            ret += parsed[(b, a)]
        rets.append(ret)


    return max(rets)

sample = solve(SAMPLE)
if sample != SAMPLE_EXPECTED:
    print("SAMPLE FAILED: ", sample, " != ", SAMPLE_EXPECTED)
assert sample == SAMPLE_EXPECTED
print("\n*** SAMPLE PASSED ***\n")

solved = solve(REAL) # 664.
print("SOLUTION: ", solved)

solved = solve(REAL, True) # 664.
print("SOLUTION2: ", solved)
