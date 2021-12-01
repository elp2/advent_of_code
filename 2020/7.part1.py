from collections import defaultdict

def return_default():
    return 0

def dd():
    return defaultdict(return_default)


CHALLENGE_DAY = "7"
REAL = open(CHALLENGE_DAY + ".txt").read()
SAMPLE = open(CHALLENGE_DAY + ".sample.txt").read()
SAMPLE_EXPECTED = 4
# SAMPLE_EXPECTED = 


def parse_lines(raw):
    # Groups.
    # split = raw.split("\n\n")
    # return list(map(lambda group: group.split("\n"), split))

    split = raw.split("\n")
    ret = {}
    for l in split:
        ls = l.split(" contain ")
        name = ls[0].replace(" bags", "")

        if ls[1] == "no other bags.":
            ret[name] = None
            continue
        bags = ls[1].split(",")
        here = {}
        for bag in bags:
            bag = bag.strip()
            qty, n1, n2, _ = bag.split(" ")
            nh = n1 + " " + n2
            here[nh] = int(qty)
        ret[name] = here
        
    return ret        


    # return split
    # return list(map(int, lines))
    # return list(map(lambda l: l.strip(), split)) # beware leading / trailing WS


def contains(target, bags, at):
    if at == target:
        return True
    if bags[at] == None:
        return False
    for k in bags[at].keys():
        if contains(target, bags, k):
            return True
    return False

def solve(raw):
    parsed = parse_lines(raw)
    # Debug here to make sure parsing is good.
    ret = 0

    SHINY = "shiny gold"
    for k in parsed.keys():
        seen = set()
        if k == SHINY:
            continue
        if contains(SHINY, parsed, k):
            ret += 1

    return ret

sample = solve(SAMPLE)
if SAMPLE_EXPECTED is None:
    print("*** SKIPPING SAMPLE! ***")
else:
    assert sample == SAMPLE_EXPECTED
    print("*** SAMPLE PASSED ***")

solved = solve(REAL)
print("SOLUTION: ", solved)
# assert solved
