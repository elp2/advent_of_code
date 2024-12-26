from collections import defaultdict, deque, Counter
from itertools import combinations, combinations_with_replacement, permutations, product
from functools import reduce, cmp_to_key
from operator import add, mul, itemgetter, attrgetter
import os
from parse import parse
import sys

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, root_dir)
from aoc_elp import *

######################
SAMPLE_EXPECTED = "co,de,ka,ta"
######################
assert SAMPLE_EXPECTED != None, "Must enter sample value"


def parse_lines(raw):
    connections = defaultdict(lambda: set())
    names = set()
    for line in raw.split("\n"):
        a, b = line.split("-")
        connections[a].add(b)
        connections[b].add(a)
        names.add(a)
        names.add(b)
    return names, connections

def get_three_groups(raw):
    names, connections = parse_lines(raw)
    
    ret = 0
    three_groups = set()
    for n in names:
        q = deque()
        q.append([n])
        while q:
            path = q.popleft()
            if len(path) == 3:
                if path[0] in connections[path[-1]]:
                    three_groups.add(tuple(sorted(path)))
                continue
            for around in connections[path[-1]]:
                if around not in path:
                    q.append(path + [around])
    t_three_groups = [tg for tg in three_groups if tg[0][0] == "t" or tg[1][0] == "t" or tg[2][0] == "t"]
    assert len(t_three_groups) in [1512, 7]

    return three_groups

def solve(raw):
    _, connections = parse_lines(raw)

    groups = [set(g) for g in get_three_groups(raw)]
    while True:
        updated = 0
        for i in range(len(groups)):
            a = groups[i]
            if not a:
                continue
            for j in range(i + 1, len(groups)):
                b = groups[j]
                if b == None:
                    continue
                overlapping = a.intersection(b)
                extra = a.union(b) - overlapping
                for e in extra:
                    if overlapping.issubset(connections[e]):
                        overlapping.add(e)
                if extra.issubset(overlapping):
                    a = overlapping
                    groups[i] = a
                    groups[j] = None
                    updated += 1
        if not updated:
            break
        groups = [g for g in groups if g]
    longest = max(groups, key=len)
    return ",".join(sorted(longest))


if __name__ == "__main__":
    SAMPLE, REAL = get_raw_inputs(sys.argv)

    sample = solve(SAMPLE)
    assert sample == SAMPLE_EXPECTED, "Sample Result %s != %s expected" % (sample, SAMPLE_EXPECTED)
    print("\n*** SAMPLE PASSED ***\n")

    solved = solve(REAL)
    print("SOLUTION: ", solved)
