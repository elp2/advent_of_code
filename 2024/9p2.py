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
SAMPLE_EXPECTED = 2858
######################
assert SAMPLE_EXPECTED != None, "Must enter sample value"

def parse_group(group):
    lines = group.split("\n")
    ret = []
    for line in lines:
        line = line.strip()
        assert len(line) != 0

        split = list(map(int, list(line)))
        assert len(split) != 0
        ret.append(split)

    return ret


def parse_lines(raw):
    # Groups.
    # groups = raw.split("\n\n")
    # Do something with the groups.

    return parse_group(raw)

def checksum(fs):
    print(fs)
    ret = 0
    idx = 0
    for i, (blocknum, blocksize) in enumerate(fs):
        for _ in range(blocksize):
            if blocknum != None:
                ret += idx * blocknum
            idx += 1
    return ret

def expand(fs):
    expanded = []
    fsi = 0

    blocknum = 0
    while fsi < len(fs):
        here = fs[fsi:fsi + 2]
        if len(here) == 1:
            here.append(None)
        
        block, empty = here
        expanded.append((blocknum, block))

        print(blocknum, block)
        blocknum += 1
        if empty != None:
            expanded.append((None, empty))

        fsi += 2

    return expanded
        
def pprint(e):
    line = ""
    for (blocknum, blocksize) in e:
        for _ in range(blocksize):
            if None == blocknum:
                line += "."
            else:
                line += str(blocknum)
    return line


def compress(e):
    right = len(e) - 1

    biggest_moved = None
    while right > 0:
        move_blocknum, move_blocksize = e[right]
        # print("Noving ", right, ": ", move_blocksize, "x of ", move_blocknum)

        if move_blocknum == None:
            # It is empty, move left
            right -= 1
            continue

        # Find the leftmost block this could fit.
        moved = False
        for i in range(len(e)):
            target_blocknum, target_blocksize = e[i]
            assert target_blocksize >= 0
            if target_blocknum != None:
                continue # Not empty
            if target_blocksize < move_blocksize:
                continue # Wouldn't fit
            if i >= right:
                break # too far, can't move here

            # Will fit.
            moved = True
            remain = target_blocksize - move_blocksize
            e[i] = (move_blocknum, move_blocksize)
            e[right] = (None, move_blocksize)
            if remain > 0:
                e.insert(i + 1, (None, remain))
            else:
                right -= 1
            break
        if moved:
            pass
            print("Move!")
            # print(pprint(e))
        else:
            right -= 1



    return e



def solve(raw):
    parsed = parse_lines(raw)[0]
    print(parsed)
    e = expand(parsed)
    print("exp: ", e)
    c = compress(e)
    print(c)

    return(checksum(e))

if __name__ == "__main__":
    SAMPLE, REAL = get_raw_inputs(sys.argv)

    sample = solve(SAMPLE)
    assert sample == SAMPLE_EXPECTED, "Sample Result %s != %s expected" % (sample, SAMPLE_EXPECTED)
    print("\n*** SAMPLE PASSED ***\n")

    solved = solve(REAL)
    print("SOLUTION: ", solved)
