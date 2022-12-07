from collections import defaultdict, deque, Counter
from itertools import combinations, combinations_with_replacement, permutations
from functools import reduce
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


CHALLENGE_DAY = "7"
REAL = open(CHALLENGE_DAY + ".txt").read()

SAMPLE_EXPECTED = 24933642
if SAMPLE_EXPECTED:
    SAMPLE = open(CHALLENGE_DAY + ".s.txt").read()


def parse_lines(raw):
    ret = []
    cmd = None
    files = {}
    dirs = []
    for l in raw.split("\n"):
        if l[0] == "$":
            if cmd:
                ret.append((cmd, arg, files, dirs))
                files = {}
                dirs = []
            exec = l.split(" ")
            cmd = exec[1]
            if cmd == "cd":
                arg = exec[2]
            else:
                arg = None
        else:
            dl = l.split(" ")
            if dl[0] == "dir":
                dirs.append(dl[1])
            else:
                files[dl[1]] = int(dl[0])

    if cmd:
        ret.append((cmd, arg, files, dirs))

    return ret


        
    # Groups.
    # groups = raw.split("\n\n")
    # return list(map(lambda group: group.split("\n"), groups))
    # lines = raw.split("\n")
    # return lines # raw
    # return list(map(lambda l: l.split(" "), lines)) # words.
    # return list(map(int, lines))
    # return list(map(lambda l: l.strip(), lines)) # beware leading / trailing WS

HERE_SIZE = "***HERE"
TOTAL_SIZE = "***TOTAL"

def rec_size(dir):
    ret = dir[HERE_SIZE]
    for d in dir.keys():
        if d in [HERE_SIZE, TOTAL_SIZE]:
            continue
        ret += rec_size(dir[d])
    dir[TOTAL_SIZE] = ret
    return ret


def part2size(dir, to_del):
    ret = to_del * 100
    if dir[TOTAL_SIZE] >= to_del:
        ret = dir[TOTAL_SIZE]
    for d in dir.keys():
        if d in [HERE_SIZE, TOTAL_SIZE]:
            continue
        rec = part2size(dir[d], to_del)
        if rec < ret:
            ret = rec

    return ret

def solve(raw):
    parsed = parse_lines(raw)
    # Debug here to make sure parsing is good.
    ret = 0

    pwd = []

    disk = {}
    for (cmd, arg, files, dirs) in parsed:
        if cmd == "cd":
            if arg == "..":
                pwd.pop()
            elif arg == "/":
                pwd = []
            else:
                pwd.append(arg)
        else:
            assert cmd == "ls"
            cwd = {HERE_SIZE: 0}
            here = 0
            for f, s in files.items():
                cwd[HERE_SIZE] += s
            for d in dirs:
                cwd[d] = {}
            if pwd == []:
                disk = cwd
            else:
                parent = disk
                for d in pwd[:-1]:
                    parent = parent[d]
                parent[pwd[-1]] = cwd

    print(disk)

    rec_size(disk)

    print("----", disk)

    total_disk = 70000000
    needed = 30000000
    can_keep = total_disk - needed
    to_del = disk[TOTAL_SIZE] - can_keep
    print("TO DEL", to_del)

    return part2size(disk, to_del)



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

