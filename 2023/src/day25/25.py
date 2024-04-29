from collections import defaultdict, deque, Counter
from itertools import combinations, combinations_with_replacement, permutations
from functools import reduce, cmp_to_key
import math
# import numpy as np
from operator import add, mul, itemgetter, attrgetter
import os
import random
import re
from sys import argv

def flatten(t):
    return [item for sublist in t for item in sublist]

# Sorts with cmp. cmp < 0 for a < b, == 0 for a==b, > 0 for a > b.
def elpsort(array, cmp):
    return sorted(array, key=cmp_to_key(cmp))

ON_TEXT = '\u2588'
OFF_TEXT = '\u2592'

LEFT = 0
UP = 1
RIGHT = 2
DOWN = 3
CHAR_TO_DS = {"^": UP, ">": RIGHT, "<": LEFT, "v": DOWN}
DS = [(-1, 0), (0, -1), (1, 0), (0, 1)]
DS8 = DS + [(-1, -1), (1, -1), (-1, 1), (1, 1)]

def arounds(x, y, diagonals):
    ret = []
    for dx, dy in DS8 if diagonals else DS:
        ret.append((x + dx, y + dy))
    return ret

CHALLENGE_DAY = argv[0].split("/")[-1].replace(".py", "").replace("p2.py", "")
AOC_DIR = os.path.dirname(argv[0])

print("Day: ", CHALLENGE_DAY)

######################
SAMPLE_EXPECTED = 54
######################
assert SAMPLE_EXPECTED != None

try:
    SAMPLE = open(os.path.join(AOC_DIR, CHALLENGE_DAY + ".s.txt")).read()
except:
    print("Did you create the sample file?")

try:
    REAL = open(os.path.join(AOC_DIR, CHALLENGE_DAY + ".txt")).read()
except:
    print("Did you create the solutions file?")

def makekey(k1, k2):
    if k1 < k2:
        return (k1, k2)
    return (k2, k1)

def parse_lines(raw):
    conns = defaultdict(lambda: [])
    lines = raw.split("\n")
    for l in lines:
        l = l.replace(":", "")
        c = l.split(" ")
        for i in range(1, len(c)):
            conns[c[i]].append(c[0])
            conns[c[0]].append(c[i])
        
    return conns

def shortest(a, b, conns):
    q = deque()
    q.append(([a]))
    i = 0
    while True:
        i += 1
        # if i % 100 == 0:
        #     print(a, "->", b, i, len(q))
        path = q.popleft()
        at = path[-1]
        if at == b:
            return path
        else:
            for n in conns[at]:
                if n in path:
                    continue
                pcopy = path.copy()
                pcopy.append(n)
                q.append(pcopy)
        

def find_candidates(raw):
    conns = parse_lines(raw)
    

    cnt = Counter()
    ckeys = list(conns.keys())
    shortests = []
    while True:
        a, b = random.choices(ckeys, k=2)

        sho = shortest(a, b, conns)
        shortests.append(sho)
        for si in range(len(sho) - 2):
            cnt[makekey(sho[si], sho[si + 1])] += 1
        
        if len(shortests) % 10 == 0:
            print("-----")
            for (nodea, nodeb), num_seen in cnt.most_common(10):
                present_in_paths = 0
                print((nodea, nodeb), num_seen, float(num_seen) / len(shortests))
    return ret

def solve(raw):
    conns = parse_lines(raw)
    excludes = {}
    ekeys = [('jct', 'rgv'), ('crg', 'krf'), ('fmr', 'zhg')]
    for (ea, eb) in ekeys:
        excludes[ea] = eb
        excludes[eb] = ea
    def group_size(start, excludes):
        seens = set()
        q = deque()
        q.append(start)
        while len(q):
            here = q.popleft()
            if here in seens:
                continue
            seens.add(here)
            for adj in conns[here]:
                if adj not in seens:
                    if here in excludes and adj in excludes[here]:
                        continue
                    q.append(adj)
        return len(seens)
    gsizes = set()
    for k in conns.keys():
        gsizes.add(group_size(k, excludes))
        print(gsizes)
    print("totoal", len(conns))
    return list(gsizes)[0] * list(gsizes)[1]


# ('jct', 'rgv') 301 0.188125
# ('crg', 'krf') 289 0.180625
# ('fmr', 'zhg') 222 0.13875
# ('ddr', 'krf') 168 0.105
# ('fmr', 'nnt') 113 0.070625
# ('crg', 'rxd') 80 0.05
# ('crg', 'zsh') 77 0.048125
# ('cdn', 'crg') 72 0.045
# ('rgv', 'xtx') 71 0.044375
# ('bvd', 'rgv') 70 0.04375


# sample = solve(SAMPLE)
# if sample != SAMPLE_EXPECTED:
#     print("SAMPLE FAILED: ", sample, " != ", SAMPLE_EXPECTED)
# assert sample == SAMPLE_EXPECTED
# print("\n*** SAMPLE PASSED ***\n")

solved = solve(REAL)
print("SOLUTION: ", solved)