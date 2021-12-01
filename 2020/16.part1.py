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
    for ot in other_tickets:
        iff = invalid_fields(ot, rules)
        print(ot, iff)
        if iff != None:
            ret += iff


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

sample = solve(SAMPLE)
if SAMPLE_EXPECTED is None:
    print("*** SKIPPING SAMPLE! ***")
else:
    assert sample == SAMPLE_EXPECTED
    print("*** SAMPLE PASSED ***")

solved = solve(REAL)
print("SOLUTION: ", solved)
import pandas as pd
df=pd.DataFrame([str(solved)])
df.to_clipboard(index=False,header=False)
print("COPIED TO CLIPBOARD")
# assert solved
