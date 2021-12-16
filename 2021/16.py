from collections import defaultdict, deque, Counter
from itertools import combinations, combinations_with_replacement, permutations
import math
from functools import reduce
# import numpy as np
from operator import add, mul, itemgetter, attrgetter
import re

DS = [[-1, 0], [1, 0], [0, 1], [0, -1]]
DS8 = DS + [[-1, -1], [1, -1], [-1, 1], [1, 1]]
def arounds_inside(x, y, diagonals, w, h):
    ret = []
    for dx, dy in DS8 if diagonals else DS:
        ret.append((x + dx, y + dy))


CHALLENGE_DAY = "16"
REAL = open(CHALLENGE_DAY + ".txt").read()

SAMPLE_EXPECTED = 3
if SAMPLE_EXPECTED:
    SAMPLE = open(CHALLENGE_DAY + ".s.txt").read()


def parse_lines(raw):
    ret = []
    for c in raw.strip():
        binned = bin(int(c, 16)).replace("0b", "")
        while len(binned) < 4:
            binned = "0" + binned
        ret.append(binned)
    d = deque()
    for r in "".join(ret):
        d.append(r)
    return d


def read_n(packet, n):
    ret = ""
    for _ in range(n):
        ret += packet.popleft()
    return ret

def parse_literal(packet):
    num = ""
    while True:
        five = read_n(packet, 5)
        assert len(five) == 5
        num += five[1:]
        if "0" == five[0]:
            break
    return int(num, 2)


def depacket(packet, pstart=0):
    version = int(read_n(packet, 3), 2)
    id = int(read_n(packet, 3), 2)
    if id == 4:
        num = parse_literal(packet)
        print("literal: ", (version, id, num))
        return (version, id, num)
    else:
        len_type_id = read_n(packet, 1)
        if len_type_id == "0":
            subpacket_len = read_n(packet, 15)
            assert 15 == len(subpacket_len)
            spl = int(subpacket_len, 2)
            sp = []

            subpacket = deque()
            for _ in range(spl):
                subpacket.append(read_n(packet, 1))
            while len(subpacket) != 0:
                v, pid, p = depacket(subpacket)
                sp.append((v, pid, p))

            print("packet_by_len: @", pstart, (version, id, sp))
            return (version, id, sp)
        elif len_type_id == "1":
            num_subpackets = read_n(packet, 11)
            assert 11 == len(num_subpackets)
            num_subpackets = int(num_subpackets, 2)
            sp = []
            while len(sp) != num_subpackets:
                v, pid, p = depacket(packet)
                sp.append((v, pid, p))
            print("packet_by_num_sp: @", pstart, (version, id, sp))
            return (version, id, sp)
        else:
            assert False

def part1(packets):
  version, id, contents, _ = packets
  if type(contents) == int:
      return version
  else:
      ret = version
      for c in contents:
          ret += part1(c)
      return ret

def part2(packets):
    version, id, contents = packets
    if id == 4:
        return contents
    
    vals = [part2(p) for p in contents]
    if id == 0:
        return reduce(add, vals)
    elif id == 1:
        return reduce(mul, vals)
    elif id == 2:
        return reduce(min, vals)
    elif id == 3:
        return reduce(max, vals)
    elif id == 5:
        assert len(vals) == 2
        return 1 if vals[0] > vals[1] else 0       
    elif id == 6:
        assert len(vals) == 2
        return 1 if vals[0] < vals[1] else 0       
    elif id == 7:
        assert 2 == len(vals)
        return 1 if vals[0] == vals[1] else 0       
    else:
        assert False


def solve(raw):
    parsed = parse_lines(raw)
    # Debug here to make sure parsing is good.
    ret = 0
    dp = depacket(parsed)

    return part2(dp)

if SAMPLE_EXPECTED != None:
    sample = solve(SAMPLE)
    if sample != SAMPLE_EXPECTED:
        print("SAMPLE FAILED: ", sample, " != ", SAMPLE_EXPECTED)
    assert sample == SAMPLE_EXPECTED
    print("\n*** SAMPLE PASSED ***\n")
else:
    print("Skipping sample")

solved = solve(REAL)
print("SOLUTION: ", solved)
import pandas as pd
df=pd.DataFrame([str(solved)])
df.to_clipboard(index=False,header=False)
print("COPIED TO CLIPBOARD")
