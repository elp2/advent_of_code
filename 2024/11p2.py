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
SAMPLE_EXPECTED = 55312
######################
assert SAMPLE_EXPECTED != None, "Must enter sample value"

def blink(num):
    # If the stone is engraved with the number 0, it is replaced by a stone engraved with the number 1.
    if num == 0:
        num = 1
        return Counter({num: 1})
    elif len(str(num)) % 2 == 0:
        s = str(num)
        # If the stone is engraved with a number that has an even number of digits, it is replaced by two stones. The left half of the digits are engraved on the new left stone, and the right half of the digits are engraved on the new right stone. (The new numbers don't keep extra leading zeroes: 1000 would become stones 10 and 0.)        
        left = int(s[:len(s) // 2])
        right = int(s[len(s)//2:])
        if left == right:
            return Counter({left: 2})
        else:
            return Counter({left: 1, right: 1})
    else:
        # If none of the other rules apply, the stone is replaced by a new stone; the old stone's number multiplied by 2024 is engraved on the new stone.
        num *= 2024
        return Counter({num: 1})

def parse_group(group):
    lines = group.split("\n")
    ret = []
    for line in lines:
        line = line.strip()
        assert len(line) != 0

        split = list(map(int, line.split(" ")))

        assert len(split) != 0
        ret.append(split)

    head = None
    prev = None
    nodes = Counter()
    for i in ret[0]:
        nodes[i] += 1

    return nodes

def parse_lines(raw):
    # Groups.
    # groups = raw.split("\n\n")
    # Do something with the groups.

    return parse_group(raw)


def blink_nodes(head):
    while head:
        head = head.blink()


def solve(raw):
    nodes = parse_lines(raw)
    cache = {}

    for bnum in range(75):
        print("blink", bnum)
        newnodes = Counter()
        for num, count in nodes.items():
            if num not in cache:
                cache[num] = blink(num)

            # Dictionary comprehension is significantly slower.            
            # newnodes += Counter({key: value * count for key, value in cache[num].items()})

            for cn, cc in cache[num].items():
                newnodes[cn] += cc * count
            
        nodes = newnodes
        print(sum(nodes.values()))

    return sum(nodes.values())


if __name__ == "__main__":
    SAMPLE, REAL = get_raw_inputs(sys.argv)

    # sample = solve(SAMPLE)
    # assert sample == SAMPLE_EXPECTED, "Sample Result %s != %s expected" % (sample, SAMPLE_EXPECTED)
    # print("\n*** SAMPLE PASSED ***\n")

    solved = solve(REAL)
    print("SOLUTION: ", solved)
