from collections import defaultdict, deque
import re
from itertools import combinations

CHALLENGE_DAY = "1"
REAL = open(CHALLENGE_DAY + ".txt").read()

PACKAGES="""1
2
3
7
11
13
17
19
23
31
37
41
43
47
53
59
61
67
71
73
79
83
89
97
101
103
107
109
113"""
PACKAGES = list(map(int, PACKAGES.split("\n")))




def quantum_entanglement(l):
    ret = l[0]
    for i in range(1, len(l)):
        ret *= ret[i]
    return ret


def solve():
    third = int(sum(PACKAGES) / 3)

    all = set()

    num = 3
    while num < len(PACKAGES):
        tot = 0
        num += 1
        for it in combinations(PACKAGES, num):
            if sum(it) == third:
                tot += 1
                all.add(it)
        print(num, tot)

    best = 100000000
    for a in all:
        bc = PACKAGES - a
        


    return best


solved = solve()
print("SOLUTION: ", solved)
