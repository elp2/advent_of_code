from collections import defaultdict, deque
import re
from itertools import combinations

CHALLENGE_DAY = "17"
REAL = open(CHALLENGE_DAY + ".txt").read()

def parse_lines(raw):
    # Groups.
    # groups = raw.split("\n\n")
    # return list(map(lambda group: group.split("\n"), groups))
    
    lines = raw.split("\n")
    # return lines # raw
    # return list(map(lambda l: l.split(" "), lines)) # words.
    return list(map(int, lines))
    # return list(map(lambda l: l.strip(), lines)) # beware leading / trailing WS

def solve(raw):
    parsed = parse_lines(raw)
    # Debug here to make sure parsing is good.
    ret = 0
    TARGET = 150
    part2 = 0
    for num in range(3, len(parsed)):
        here = 0
        for com in combinations(parsed, num):
            if sum(com) == TARGET:
                here += 1
        if part2 == 0 and here != 0:
            part2 = here
        ret += here
        print(num, here)
    return ret, part2


solved1, solved2 = solve(REAL)
print("SOLUTION: ", solved1, solved2) # 4372 4
