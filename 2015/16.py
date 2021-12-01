from collections import defaultdict, deque
import re

CHALLENGE_DAY = "16"
REAL = open(CHALLENGE_DAY + ".txt").read()

def parse_lines(raw):
    lines = raw.split("\n")
    ret = {}
    for l in lines:
        l = l.replace(",", "")
        s = l.split(" ")
        name = s[0] + s[1]
        keys = s[2:]
        here = {}
        for i in range(0, len(keys), 2):
            here[keys[i]] =int(keys[i + 1])
        ret[name] = here
    return ret

KNOWN = {
"children:": 3,
"cats:": 7,
"samoyeds:": 2,
"pomeranians:": 3,
"akitas:": 0,
"vizslas:": 0,
"goldfish:": 5,
"trees:": 3,
"cars:": 2,
"perfumes:": 1,
}
def solve(raw):
    parsed = parse_lines(raw)

    # Debug here to make sure parsing is good.
    ret = 0

    max_score = 0
    max_name = None
    for name, keys in parsed.items():
        score = 0
        print(KNOWN, keys)
        for k in keys:
            if k not in KNOWN:
                continue
            kval = KNOWN[k]
            sueval = keys[k]
            if k in ['cats:', 'trees:']:
                if sueval > kval:
                    score += 1
            elif k in ['pomeranians:', 'goldfish:']:
                if sueval < kval:
                    score += 1
            elif sueval == kval:
                score += 1
        if score > max_score:
            max_score = score
            max_name = name

    print(max_name, max_score)
    return max_name

solved = solve(REAL)
print("SOLUTION: ", solved)

