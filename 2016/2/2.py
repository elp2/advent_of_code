from collections import defaultdict, deque
from itertools import combinations, combinations_with_replacement, permutations
import math
import re

REAL = open("2/in").read()
# SAMPLE = open("2/sample").read()

def parse_lines(raw):
    # Groups.
    # groups = raw.split("\n\n")
    # return list(map(lambda group: group.split("\n"), groups))
    
    lines = raw.split("\n")
    return lines # raw
    # return list(map(lambda l: l.split(" "), lines)) # words.
    # return list(map(int, lines))
    # return list(map(lambda l: l.strip(), lines)) # beware leading / trailing WS

def solve1(raw):
    parsed = parse_lines(raw)
    pad = ["123", "456", "789"]
    key = (1, 1)
    ret = ""
    for line in parsed:
        nx, ny = key
        for c in line:
            deltas = {"L": (-1, 0), "R": (1, 0), "D": (0, 1), "U": (0, -1)}[c]
            nx += deltas[0]
            ny += deltas[1]
            nx = min(2, max(0, nx))
            ny = min(2, max(0, ny))
            key = (nx, ny)
        ret += pad[ny][nx]

    return ret

# sample = solve(SAMPLE)
# if sample != SAMPLE_EXPECTED:
#     print("SAMPLE FAILED: ", sample, " != ", SAMPLE_EXPECTED)
# assert sample == SAMPLE_EXPECTED
# print("\n*** SAMPLE PASSED ***\n")

solved = solve1(REAL)
print("P1: ", solved)

PAD = """       
   1   
  234  
 56789 
  ABC  
   D   
       """.split("\n")

def solve2(raw):
    parsed = parse_lines(raw)
    key = (3, 3)
    ret = ""
    for line in parsed:
        for c in line:
            nx, ny = key
            deltas = {"L": (-1, 0), "R": (1, 0), "D": (0, 1), "U": (0, -1)}[c]
            nx += deltas[0]
            ny += deltas[1]
            if " " != PAD[ny][nx]:
                key = (nx, ny)
                assert PAD[ny][nx] in "ABCD123456789"
        ret += PAD[key[1]][key[0]]
  
    return ret

print("Part2: ", solve2(REAL))
