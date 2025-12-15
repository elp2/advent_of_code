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
SAMPLE_EXPECTED = 2
######################
assert SAMPLE_EXPECTED != None, "Must enter sample value"

def parse_group(group):
    lines = group.split("\n")
    ret = {}
    for y, line in enumerate(lines):
        line = line.strip()
        assert len(line) != 0

        split = line.split(":")
        f = split[0]
        tos = [s for s in split[1].split(" ") if len(s) > 0]
        ret[f] = tos
    return ret


def parse_lines(raw):
    # Groups.
    # groups = raw.split("\n\n")
    # Do something with the groups.

    return parse_group(raw)


def sort_vert(graph):
    indeg = {v: 0 for v in graph.keys()}
    indeg["out"] = 0
    for u, vs in graph.items():
        for v in vs:
            indeg[v] += 1


    order = []
    q = deque([v for v in graph.keys() if indeg[v] == 0])

    while len(q):
        here = q.popleft()
        order.append(here)
        if here == "out":
            continue
        for v in graph[here]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)
    
    print(len(order), len(graph))
    print("DIFF: ", set(order) - set(graph.keys()))
    return order

def numpaths(graph, f, to, allowed):
    ret = 0
    q = deque([f])
    while len(q):
        at = q.popleft()
        if at == to:
            ret += 1
            continue
        for n in graph[at]:
            if n in allowed:
                q.append(n)
    return ret


def solve(raw):
    graph = parse_lines(raw)
    order = sort_vert(graph)
    # print(order)

    ffti = order.index("fft")
    daci = order.index("dac")
    assert ffti < daci
    first = set(order[:ffti + 1])
    second = set(order[ffti:daci + 1])
    third = set(order[daci:])

    fret = numpaths(graph, "svr", "fft", first)
    print(fret)
    sret = numpaths(graph, "fft", "dac", second)
    print(sret)
    tret = numpaths(graph, "dac", "out", third)
    print(tret)

    print(fret, sret, tret)
    return fret * sret * tret

if __name__ == "__main__":
    SAMPLE, REAL = get_raw_inputs(sys.argv)
    SAMPLE="""svr: aaa bbb
aaa: fft
fft: ccc
bbb: tty
tty: ccc
ccc: ddd eee
ddd: hub
hub: fff
eee: dac
dac: fff
fff: ggg hhh
ggg: out
hhh: out"""

    sample = solve(SAMPLE)
    assert sample == SAMPLE_EXPECTED, "Sample Result %s != %s expected" % (sample, SAMPLE_EXPECTED)
    print("\n*** SAMPLE PASSED ***\n")

    solved = solve(REAL)
    assert solved > 3420
    print("SOLUTION: ", solved)
