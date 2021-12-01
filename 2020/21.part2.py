from collections import defaultdict, deque
import re

CHALLENGE_DAY = "21"
REAL = open(CHALLENGE_DAY + ".txt").read()
SAMPLE = open(CHALLENGE_DAY + ".sample.txt").read()
SAMPLE_EXPECTED = "mxmxvkd,sqjhc,fvjkl"
# SAMPLE_EXPECTED = 


def parse_lines(raw):
    allergens = defaultdict(set)
    all_words = defaultdict(lambda: 0)

    lines = raw.split("\n")
    for line in lines:
        istr, astr = line.split(" (contains")
        ingredients = set(re.findall(r"\w+", istr))
        for i in ingredients:
            all_words[i] += 1

        for a in re.findall(r"\w+", astr):
            if a in allergens:
                allergens[a] &= ingredients
            else:
                allergens[a] |= ingredients
        print(line, allergens)

    return allergens, all_words

def solve(raw):
    allergens, all_words = parse_lines(raw)

    solved = {}
    changed = True
    while changed:
        changed = False
        for ak, aw in allergens.items():
            if len(aw) == 1:
                solved[ak] = list(aw)[0]
                changed = True
                del(allergens[ak])
                for rk in allergens.keys():
                    allergens[rk] -= aw
                break

    sk = list(solved.keys())
    sk.sort()
    ret = []
    for k in sk:
        ret.append(solved[k])
    return ",".join(ret)

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
