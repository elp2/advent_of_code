from collections import defaultdict, deque, Counter
from itertools import combinations, combinations_with_replacement, permutations
from functools import reduce
import math
# import numpy as np
from operator import add, mul, itemgetter, attrgetter
import re
from typing import DefaultDict

DS = [[-1, 0], [1, 0], [0, 1], [0, -1]]
DS8 = DS + [[-1, -1], [1, -1], [-1, 1], [1, 1]]
def arounds_inside(x, y, diagonals, w, h):
    ret = []
    for dx, dy in DS8 if diagonals else DS:
        ret.append((x + dx, y + dy))


CHALLENGE_DAY = "19"
REAL = open(CHALLENGE_DAY + ".txt").read()

SAMPLE_EXPECTED = None
if SAMPLE_EXPECTED:
    SAMPLE = open(CHALLENGE_DAY + ".s.txt").read()


def abmatchabledelta(a, b):
    return tuple(sorted((abs(a[0] - b[0]), abs(a[1] - b[1]), abs(a[2] - b[2]))))


def parse_lines(raw):
    scanners = []
    groups = raw.split("\n\n")

    for bg in groups:
        lines = bg.split("\n")[1:]
        scanner = []
        for l in lines:
            x, y, z = [int(a) for a in l.split(",")]
            scanner.append((x, y, z))
        scanners.append(scanner)

    return scanners


def offset_ab(a, b):
    return((b[0] - a[0], b[1] - a[1], b[2] - a[2]))


def mapping_given(a1, a2, b1, b2):
    """Returns function to translate b's coords to a's coords, assuming a1=b1 and a2=b2."""

    # How do we translate the line between b1->b2 into a1->a2 style?
    adiff = [y - x for x, y in zip(a1, a2)]
    bdiff = [y - x for x, y in zip(b1, b2)]
    if 3 != len(set([abs(ad) for ad in adiff])) or 3 != len(set([abs(bd) for bd in bdiff])):
        return None
    for a in adiff:
        if a not in bdiff and -1 * a not in bdiff:
            return None

    btoa = []
    for i in range(3):
        here = bdiff[i]
        if here in adiff:
            btoa.append((adiff.index(here), 1))
        else:
            btoa.append((adiff.index(-1 * here), -1))
    
    # Back out b1 from a1, to see where the scanner for b is located in a's frame.

    def transform_to_a(o):
        oa = [None] * 3
        for i in range(3):
            ai, flip = btoa[i]
            oa[ai] = flip * o[i]
        assert None not in oa
        return oa

    # b is located backwards from a1, along b1's 
    bina = [j - i for i, j in zip(transform_to_a(b1), a1)]

    def mapping(to_map):
        # Start at bina, then add the right offsets
        return tuple([j + k for j, k in zip(bina, transform_to_a(to_map))])

    assert mapping(b1) == a1
    assert mapping(b2) == a2

    return mapping


mg = mapping_given((0, 0, 0), (1, 2, 3), (1, 1, 1), (2, 3, 4))
print(mg((1,2,3)))
# assert mg((3,3,3)) == (2, 2, 2)

def loop(scanners):
    def scanner_pairs(scanner):
        ret = DefaultDict(lambda: [])
        for i, j in combinations(range(len(scanner)), 2):
            a = scanner[i]
            b = scanner[j]
            ret[abmatchabledelta(a, b)].append((i, j))
        return ret

    sps = [scanner_pairs(x) for x in scanners]

    lens = list(map(lambda l: len(l), scanners))
    i = lens.index(min(lens))

    for j in range(len(scanners)):
        if i == j:
            continue
        a = scanners[i]
        b = scanners[j]

        for ad in sps[i].keys():
            if ad not in sps[j]:
                continue
            for ak, bk in zip(sps[i][ad], sps[j][ad]):
                mapping = mapping_given(a[ak[0]], a[ak[1]], b[bk[0]], b[bk[1]])
                if None == mapping:
                    continue
                bs = set(mapping(bg) for bg in b)
                alla = set(a)
                if len(alla.intersection(bs)) >= 12:
                    for bso in bs:
                        if bso not in scanners[i]:
                            scanners[i].append(bso)
                    scanners = [scanners[n] for n in range(len(scanners)) if n != j]

                    print("intersection!", len(scanners))
                    print(list(map(lambda l: len(l), scanners)))
                    return scanners
    assert False

def solve(raw):
    scanners = parse_lines(raw)

    while len(scanners) != 1:
        scanners = loop(scanners)


            # Pick an a beacon, and a potentially mapping b beacon.

            # Given these mappings, find the appropriate translations.

            # Translate all items in b into the perspective of a.
            # If >= 12, merge them into a, remove b, and then restart the combinations.

    ret = 0

    return len(scanners[0])

if SAMPLE_EXPECTED != None:
    sample = solve(SAMPLE)
    if sample != SAMPLE_EXPECTED:
        print("SAMPLE FAILED: ", sample, " != ", SAMPLE_EXPECTED)
    assert sample == SAMPLE_EXPECTED
    print("\n*** SAMPLE PASSED ***\n")
else:
    print("Skipping sample")

solved = solve(REAL) # 353 ? On a plane so can't check :/ !
print("SOLUTION: ", solved)
