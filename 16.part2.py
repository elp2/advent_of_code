from collections import defaultdict

def return_default():
    return 0

def dd():
    return defaultdict(return_default)


CHALLENGE_DAY = "16"
REAL = open(CHALLENGE_DAY + ".txt").read()
SAMPLE = open(CHALLENGE_DAY + ".sample.txt").read()
SAMPLE_EXPECTED = 71
# SAMPLE_EXPECTED = 

def invalid_fields(ticket, rules):
    ticket = list(map(int, ticket))

    invalid = 0
    for f in ticket:
        found = False
        for (amin, amax), (bmin, bmax) in rules.values():
            if amin <= f <= amax or bmin <= f <= bmax:
                found = True
        if not found:
            return f

    if not found:
        return f
    return None


def match_rules(ticket, rules):
    ticket = list(map(int, ticket))
    poss = []

    for i in range(len(ticket)):
        f = ticket[i]
        found = False
        good = set()
        for rule_name, rv in rules.items():
            (amin, amax), (bmin, bmax) = rv
            if amin <= f <= amax or bmin <= f <= bmax:
                found = True
                good.add(rule_name)
        poss.append(good)

    return poss

def parse_lines(raw):
    # Groups.
    split = raw.split("\n\n")
    rules_str = split[0].split("\n")
    rules = {}
    for rs in rules_str:
        name, nums = rs.split(": ")
        a, b = nums.split(" or ")
        a1, a2 = list(map(int, a.split("-")))
        b1, b2 = list(map(int, b.split("-")))
        rules[name] = [(a1, a2), (b1, b2)]

    yt = list(map(int, split[1].split("\n")[1].split(",")))

    otlines = split[2].split("\n")[1:]
    other_tickets = list(map(lambda x: x.strip().split(","), otlines))


    return rules, yt, other_tickets


    # return list(map(lambda group: group.split("\n"), split))

    # split = raw.split("\n")

    # return split # raw
    # return list(map(lambda l: l.split(" "), split)) # words.
    # return list(map(int, split))
    # return list(map(lambda l: l.strip(), split)) # beware leading / trailing WS

def solve(raw):
    rules, yt, other_tickets = parse_lines(raw)
    ret = 0
    good = []
    for ot in other_tickets:
        ot = list(map(int, ot))        
        iff = invalid_fields(ot, rules)
        print(ot, iff)
        if iff == None:
            good.append(ot)

    keys = set(list(rules.keys()))
    poss = [keys for i in range(len(yt))]
    for g in good:
        matched = match_rules(g, rules)
        for i in range(len(poss)):
            here = poss[i]
            m = matched[i]
            poss[i] = here.intersection(m)
            if len(poss[i]) != len(here):
                print(len(poss[i]), len(here))

    updated = True
    removed = []
    while updated:
        updated = False
        for i in range(len(poss)):
            here = poss[i]
            if len(here) == 1:
                sing = list(here)[0]
                if sing in removed:
                    continue
                singleton = sing
                removed.append(sing)
                updated = True
        
        if updated:
            print(singleton)
            for i in range(len(poss)):
                here = poss[i]
                if len(here) != 1 and singleton in poss[i]:
                    poss[i].remove(singleton)


    for p in poss:
        print(p)

    ret = 1
    for i in range(len(poss)):
        p = list(poss[i])[0]
        if p.startswith("departure"):
            ret *= yt[i]



    return ret

def test_parsing(lines):
    if isinstance(lines, list):
        for i in range(min(5, len(lines))):
            print(lines[i])
    elif isinstance(lines, dict) or isinstance(lines, defaultdict):
        nd = {}
        for k in list(lines.keys())[0: 5]:
            print("\"" + k + "\": " + str(lines[k]))
test_parsing(parse_lines(SAMPLE))
print("^^^^^^^^^PARSED SAMPLE SAMPLE^^^^^^^^^")

# sample = solve(SAMPLE)
# if SAMPLE_EXPECTED is None:
#     print("*** SKIPPING SAMPLE! ***")
# else:
#     assert sample == SAMPLE_EXPECTED
#     print("*** SAMPLE PASSED ***")

solved = solve(REAL)
print("SOLUTION: ", solved)
import pandas as pd
df=pd.DataFrame([str(solved)])
df.to_clipboard(index=False,header=False)
print("COPIED TO CLIPBOARD")
# assert solved
