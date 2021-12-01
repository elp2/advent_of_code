from collections import defaultdict, deque
from itertools import combinations, combinations_with_replacement, permutations
import math
import re

REAL = open("3/in").read()
# SAMPLE = open("3/sample").read()
SAMPLE_EXPECTED = None

def parse_lines(raw):
    # Groups.
    # groups = raw.split("\n\n")
    # return list(map(lambda group: group.split("\n"), groups))
    
    lines = raw.split("\n")
    return [[int(x) for x in line.split(" ") if x] for line in lines]
    # return lines # raw
    # return list(map(lambda l: l.split(" "), lines)) # words.
    # return list(map(int, lines))
    # return list(map(lambda l: l.strip(), lines)) # beware leading / trailing WS

def part1(raw):
    parsed = parse_lines(raw)
    ret = 0
    for a, b, c in parsed:
        a, b, c = sorted([a, b, c])
        assert a <= b and b <= c
        if a + b > c:
            ret += 1
    return ret

part1d = part1(REAL)
print("SOLUTION: ", part1d)

def part2(raw):
    parsed = parse_lines(raw)
    ret = 0
    for i in range(3):
        for j in range(0, len(parsed), 3):
            tri = sorted([parsed[j][i], parsed[j + 1][i], parsed[j + 2][i]])
            if tri[0] + tri[1] > tri[2]:
                ret += 1
    return ret

print("Part 2: ", part2(REAL))
