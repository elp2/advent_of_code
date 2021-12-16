from collections import defaultdict, deque, Counter
from itertools import combinations, combinations_with_replacement, permutations
import math
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

SAMPLE_EXPECTED = 16
if SAMPLE_EXPECTED:
    SAMPLE = open(CHALLENGE_DAY + ".s.txt").read()


def parse_lines(raw):
    ret = []
    for c in raw.strip():
        binned = bin(int(c, 16)).replace("0b", "")
        while len(binned) < 4:
            binned = "0" + binned
        ret.append(binned)
    return "".join(ret)

def parse_literal(packet, i):
    num = ""
    while True:
        five = packet[i:i+5]
        assert len(five) == 5
        i += 5
        num += five[1:]
        if "0" == five[0]:
            break
    return (int(num, 2), i)


def depacket(packet, pstart=0):
    version = int(packet[pstart + 0:pstart + 3], 2)
    id = int(packet[pstart + 3:pstart + 6], 2)
    num = ""
    data_start = pstart + 6
    if id == 4:
        num, at = parse_literal(packet, data_start)
        print("literal: ", (version, id, num, at))
        return (version, id, num, at)
    else:
        len_type_id = packet[data_start]
        if len_type_id == "0":
            subpacket_len = packet[data_start + 1:data_start + 16]
            assert 15 == len(subpacket_len)
            spl = int(subpacket_len, 2)
            endlen = data_start + 1 + 15 + spl
            pat = data_start + 1 + 15
            sp = []
            while True:
                v, pid, p, pat = depacket(packet, pat)
                sp.append((v, pid, p, pat))
                if endlen == pat:
                    break
                elif endlen < pat:
                    assert False
            print("packet_by_len: @", pstart, (version, id, sp, pat))
            return (version, id, sp, pat)
        elif len_type_id == "1":
            num_subpackets = packet[data_start + 1:data_start + 12]
            assert 11 == len(num_subpackets)
            num_subpackets = int(num_subpackets, 2)
            sp = []
            pat = data_start + 1 + 11
            while len(sp) != num_subpackets:
                v, pid, p, pat = depacket(packet, pat)
                sp.append((v, pid, p, pat))
            print("packet_by_num_sp: @", pstart, (version, id, sp, pat))
            return (version, id, sp, pat)
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


def solve(raw):
    parsed = parse_lines(raw)
    # Debug here to make sure parsing is good.
    ret = 0
    dp = depacket(parsed)

    return part1(dp)

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
