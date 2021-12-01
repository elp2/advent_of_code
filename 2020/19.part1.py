from collections import defaultdict

def return_default():
    return 0

def dd():
    return defaultdict(return_default)


CHALLENGE_DAY = "19"
REAL = open(CHALLENGE_DAY + ".txt").read()
SAMPLE = open(CHALLENGE_DAY + ".sample.txt").read()
SAMPLE_EXPECTED = 2
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
    while len(rules) != 1:
        rnew = rules.copy()
        for rule, pattern in rules.items():
            print(rule, pattern)
            if re.findall(r"\b(\d+)\b", pattern):
                continue

            # if embeddable, embed it everywhere
            for rrep, prep in rnew.items():
                sub_rex = r"\b(" + rule + r")\b"
                rnew[rrep] = re.sub(sub_rex, "(" + pattern + ")", prep, count=4)
            # No longer needed since it's embedded.
            del(rnew[rule])
            break

        rules = rnew
        print(rules)

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
# print("SOLUTION: ", solved)
import pandas as pd
df=pd.DataFrame([str(solved)])
df.to_clipboard(index=False,header=False)
# print("COPIED TO CLIPBOARD")
# assert solved



#### PROBABLY WORKS BUT WAAAAAAY TOO SLOW

def recurse2(rules, rmap):
    while True:
        if rules == rmap['0'][0]:
            return True

        # print(rules)

        round = []
        for i in range(0, len(rules), 2):
            here = tuple(rules[i:i+2])
            assert len(here) == 2
            if here not in rmap:
                # print("RET!", rules)

                return False
            round.append(rmap[here])
        rules = round
    assert False


def recurse(current, rmap, target):
    # print("REC: ", current)
    if current == target:
        return True
    if current == [] and target == []:
        return True
    
    if len(current) and target == []:
        return False
    if len(target) and current == []:
        return False

    if current[:1] == target[:1]:
        if recurse(current[1:], rmap, target[1:]):
            return True
    if current[:2] == target[:2]:
        if recurse(current[2:], rmap, target[2:]):
            return True
    

    for i in range(len(current) - 2):
        here = tuple(current[i:i+2])
        if here in rmap:
            rep = [rmap[here]]
            rec = current[:i] + rep + current[i + 2:]
            if recurse(rec, rmap, target):
                return True

    # print(current[:4], "not in map")
    return False

def matches2(line, rmap):
    a = rmap["a"]
    b = rmap["b"]

    rules = []
    for c in line:
        if c == "a":
            rules.append(a)
        elif c == "b":
            rules.append(b)
        else:
            assert False

    return recurse(rules, rmap, rmap['0'][0])