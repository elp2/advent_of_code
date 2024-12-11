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

class Node:
    def __init__(self, num):
        self.num = num
        self.next = None
        self.prev = None
    
    def blink(self):
        # If the stone is engraved with the number 0, it is replaced by a stone engraved with the number 1.
        if self.num == 0:
            self.num = 1
        elif len(str(self.num)) % 2 == 0:
            s = str(self.num)
            # If the stone is engraved with a number that has an even number of digits, it is replaced by two stones. The left half of the digits are engraved on the new left stone, and the right half of the digits are engraved on the new right stone. (The new numbers don't keep extra leading zeroes: 1000 would become stones 10 and 0.)
            
            left = int(s[:len(s) // 2])
            self.num = left
            right = int(s[len(s)//2:])
            newright = Node(right)
            newright.next = self.next
            if newright.next != None:
                newright.next.prev = newright
            self.next = newright
            newright.prev = self
            return newright.next
        else:
            # If none of the other rules apply, the stone is replaced by a new stone; the old stone's number multiplied by 2024 is engraved on the new stone.
            self.num *= 2024
        return self.next

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
    for i in ret[0]:
        node = Node(i)
        if prev != None:
            prev.next = node
            node.prev = prev
        else:
            head = node
        prev = node

    return head

def count_nodes(head):
    ret = 0
    while head:
        ret += 1
        head = head.next
    return ret

def print_nodes(head):
    vals = []
    while head:
        vals.append(head.num)
        head = head.next
    print(" ".join(map(str, vals)))



def parse_lines(raw):
    # Groups.
    # groups = raw.split("\n\n")
    # Do something with the groups.

    return parse_group(raw)


def blink_nodes(head):
    while head:
        head = head.blink()


def solve(raw):
    head = parse_lines(raw)
    print(head)

    for blink in range(25):
        print("blink", blink)
        blink_nodes(head)
        # print_nodes(head)

    return count_nodes(head)

if __name__ == "__main__":
    SAMPLE, REAL = get_raw_inputs(sys.argv)

    sample = solve(SAMPLE)
    assert sample == SAMPLE_EXPECTED, "Sample Result %s != %s expected" % (sample, SAMPLE_EXPECTED)
    print("\n*** SAMPLE PASSED ***\n")

    solved = solve(REAL)
    print("SOLUTION: ", solved)
