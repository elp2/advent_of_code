from collections import defaultdict, deque
import re

CHALLENGE_DAY = "23"
REAL = open(CHALLENGE_DAY + ".txt").read()
SAMPLE = open(CHALLENGE_DAY + ".sample.txt").read()
SAMPLE_EXPECTED = 2

def parse_lines(raw):
    lines = raw.split("\n")
    return lines

def solve(raw):
    a = b = 0
    pc = 0
    parsed = parse_lines(raw)
    while pc < len(parsed):
        line = parsed[pc].split(" ")
        ins = line[0]
        reg = line[1][0]
        val = None
        pc_delta = 1
        if reg == "a":
            val = a
        elif reg == "b":
            val = b
        else:
            assert ins == "jmp"
        if ins == "hlf":
            val = int(val / 2)
        elif ins == "tpl":
            val = int(val * 3)
        elif ins == "inc":
            val = val + 1
        elif ins == "jmp":
            pc_delta = int(line[1])
        elif ins == "jie":
            if val % 2 == 0:
                pc_delta = int(line[2])
        elif ins == "jio":
            if val == 1:
                pc_delta = int(line[2])
        else:
            assert False
        pc += pc_delta

        if reg == "a":
            a = val
        elif reg == "b":
            b = val
        else:
            assert ins == "jmp"

    return b

sample = solve(SAMPLE)
if sample != SAMPLE_EXPECTED:
    print("SAMPLE FAILED: ", sample, " != ", SAMPLE_EXPECTED)
assert sample == SAMPLE_EXPECTED
print("\n*** SAMPLE PASSED ***\n")

solved = solve(REAL)
print("SOLUTION: ", solved) # 170
