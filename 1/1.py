from collections import defaultdict, deque
from itertools import combinations, combinations_with_replacement, permutations
import math
import re

REAL = open("1/in").read()

def parse_lines(raw):
    # Groups.
    # groups = raw.split("\n\n")
    # return list(map(lambda group: group.split("\n"), groups))
    
    lines = raw.split("\n")
    # return lines # raw
    return lines[0].split(", ")
    # return list(map(int, lines))
    # return list(map(lambda l: l.strip(), lines)) # beware leading / trailing WS

def part1(parsed):
    pos = complex(0, 0)
    d = complex(1, 0)
    print(d, pos)
    for p in parsed:
        d *= {"L": complex(0, 1), "R": complex(0, -1)}[p[0]]
        pos += d * int(p[1:])
        print(d, pos)
    return int(abs(pos.imag) + abs(pos.real))

assert 5 == part1(["R2", "L3"])
assert 2 == part1(["R2", "R2", "R2"])
assert 12 == part1(["R5", "L5", "R5", "R3"])

print(part1(parse_lines(REAL)))

def part2(parsed):
    seens = set((0, 0))
    pos = complex(0, 0)
    d = complex(1, 0)
    print(d, pos)

    for p in parsed:
        d *= {"L": complex(0, 1), "R": complex(0, -1)}[p[0]]
        for i in range(int(p[1:])):
            pos += d
            here = (int(pos.real), int(pos.imag))
            if here in seens:
                return abs(here[0]) + abs(here[1])
            seens.add(here)

    assert False

assert 4 == part2(["R8", "R4", "R4", "R8"]) 
print(part2(parse_lines(REAL)))
