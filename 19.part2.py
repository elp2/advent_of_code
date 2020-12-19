from collections import defaultdict

def return_default():
    return 0

def dd():
    return defaultdict(return_default)


CHALLENGE_DAY = "19"
REAL = open(CHALLENGE_DAY + ".txt").read()
SAMPLE = open(CHALLENGE_DAY + ".sample2.txt").read()
SAMPLE_EXPECTED = 12
# SAMPLE_EXPECTED = 

import re

def parse_lines(raw):
    # Groups.
    split = raw.split("\n\n")
    rlines = split[0].split("\n")
    rules = {}
    for rline in rlines:
        num, pattern = rline.split(":")
        rules[num] = pattern

    messages = split[1].split("\n")
    return rules, messages



def regexize_rules(rules):
    # Special cases.
    elevens = []
    for times in range(1, 10):
        elevens.append(" ".join(["42"] * times) + " " + " ".join(["31"] * times))
    rules["11"] = " | ".join(elevens)

    rules["8"] = " (42)+ "

    while len(rules) != 1:
        rnew = rules.copy()
        print(rules)
        for rule, pattern in rules.items():
            if re.findall(r"\b(\d+)\b", pattern):
                continue

            # if embeddable, embed it everywhere
            for rrep, prep in rnew.items():
                sub_rex = r"\b(" + rule + r")\b"
                rnew[rrep] = re.sub(sub_rex, "(" + pattern + ")", prep)

            # No longer needed since it's embedded.
            del(rnew[rule])
            break

        rules = rnew

    top = rules["0"]
    for c in "\" ":
        top = top.replace(c, "")
    top = "^" + top + "$"

    return top


def solve(raw):
    rules, messages = parse_lines(raw)
    reg = regexize_rules(rules)
    ret = 0
    for m in messages:
        if re.match(reg, m):
            ret += 1
    return ret

sample = solve(SAMPLE)
assert sample == SAMPLE_EXPECTED
print("*** SAMPLE PASSED ***")

solved = solve(REAL)
print("SOLUTION: ", solved)
import pandas as pd
df=pd.DataFrame([str(solved)])
df.to_clipboard(index=False,header=False)
print("COPIED TO CLIPBOARD")
# assert solved
