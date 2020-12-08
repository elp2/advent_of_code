from collections import defaultdict

def return_default():
    return 0

def dd():
    return defaultdict(return_default)


CHALLENGE_DAY = "8"
REAL = open(CHALLENGE_DAY + ".txt").read()
SAMPLE = open(CHALLENGE_DAY + ".sample.txt").read()
SAMPLE_EXPECTED = 8
# SAMPLE_EXPECTED = 


def parse_lines(raw):
    # Groups.
    # split = raw.split("\n\n")
    # return list(map(lambda group: group.split("\n"), split))

    split = raw.split("\n")
    return list(map(lambda l: l.split(" "), split))

    # return split
    # return list(map(int, lines))
    # return list(map(lambda l: l.strip(), split)) # beware leading / trailing WS

import copy

def try_fix(instructions, line):
    instructions = copy.deepcopy(instructions)
    lfix = instructions[line]
    if lfix[0] == "jmp":
        instructions[line][0] = "nop"
    elif lfix[1] == "nop":
        instructions[line][0] = "jmp"
    else:
        return None

    pc = 0
    acc = 0
    states = set()
    ticks = 0
    while pc < len(instructions):
        ticks += 1
        if ticks > 10000:
            print("ticks")
            return None
        state = (pc, acc)
        if state in states:
            return None
        states.add(state)
        ins = instructions[pc]
        var = int(ins[1])
        if ins[0] == "nop":
            pc += 1
        elif "acc" == ins[0]:
            pc += 1
            acc += var
        elif "jmp" == ins[0]:
            pc += var

    return acc


def solve(raw):
    instructions = parse_lines(raw)
    # Debug here to make sure parsing is good.
    ret = 0
    for i in range(len(instructions)):
        print("I: ", i)
        fixed = try_fix(instructions, i)
        if fixed is not None:
            print("!!!")
            return fixed
    assert False    

def test_parsing(lines):
    if isinstance(lines, list):
        for i in range(min(5, len(lines))):
            print(lines[i])
    elif isinstance(lines, dict) or isinstance(lines, defaultdict):
        nd = {}
        for k in list(lines.keys())[0: 5]:
            print("\"" + k + "\": " + str(lines[k]))
test_parsing(parse_lines(SAMPLE))
print("^^^^^^^^^PARSED SAMPLE SAMPLE^^^^^^^^^")

sample = solve(SAMPLE)
if SAMPLE_EXPECTED is None:
    print("*** SKIPPING SAMPLE! ***")
else:
    assert sample == SAMPLE_EXPECTED
    print("*** SAMPLE PASSED ***")

solved = solve(REAL)
print("SOLUTION: ", solved)
# assert solved
