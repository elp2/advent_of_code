from collections import defaultdict, deque
import re

CHALLENGE_DAY = "15"
REAL = open(CHALLENGE_DAY + ".txt").read()
SAMPLE = open(CHALLENGE_DAY + ".sample.txt").read()
SAMPLE_EXPECTED = 62842880

def parse_lines(raw):
    # Groups.
    # groups = raw.split("\n\n")
    # return list(map(lambda group: group.split("\n"), groups))
    
    # Sugar: capacity -1, durability 0, flavor 0, texture 2, calories 8
    lines = raw.split("\n")
    ret = []
    for l in lines:
        l = l.replace(",", "")
        name, _, cap, _, dur, _, fla, _, tex, _, cal = l.split(" ")
        ret.append([name, int(cap), int(dur), int(fla), int(tex), int(cal)])

    return ret

def solve(raw):
    parsed = parse_lines(raw)
    # Debug here to make sure parsing is good.
    ret = 0

    # remain = 100
    # for i in range(len(parsed)):
    #     if i == len(parsed) - 1:
        
    #     else:
    #       for a in range(0, remain + 1):

    max_score = 0
    total = 100
    for a in range(0, total + 1):
        remain = total - a
        for b in range(0, remain + 1):
            remain = total - a - b
            for c in range(0, remain + 1):
                remain = total - a - b - c
                d = remain
                assert d >= 0
                calories = parsed[0][5] * a + parsed[1][5] * b + parsed[2][5] * c + parsed[3][5] * d
                if calories != 500:
                    continue

                cap = parsed[0][1] * a + parsed[1][1] * b + parsed[2][1] * c + parsed[3][1] * d
                if cap < 0:
                    continue
                dur = parsed[0][2] * a + parsed[1][2] * b + parsed[2][2] * c + parsed[3][2] * d
                if dur < 0:
                    continue
                fla = parsed[0][3] * a + parsed[1][3] * b + parsed[2][3] * c + parsed[3][3] * d
                if fla < 0:
                    continue
                tex = parsed[0][4] * a + parsed[1][4] * b + parsed[2][4] * c + parsed[3][4] * d
                if tex < 0:
                    continue
                score = cap * dur * fla * tex
                max_score = max(score, max_score)


    return max_score

# sample = solve(SAMPLE)
# if sample != SAMPLE_EXPECTED:
#     print("SAMPLE FAILED: ", sample, " != ", SAMPLE_EXPECTED)
# assert sample == SAMPLE_EXPECTED
# print("\n*** SAMPLE PASSED ***\n")

solved = solve(REAL)
print("SOLUTION: ", solved)
