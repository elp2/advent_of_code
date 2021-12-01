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


def try_fix(instructions, line):
    pc = 0
    seen = set()
    acc = 0
    ticks = 0
    while pc < len(instructions):
        ticks += 1
        if ticks > 10000:
            return None
        if (pc, acc) in seen:
            return None
        seen.add((pc, acc))
        ins, var = instructions[pc]
        if ins == "nop" and pc == line:
            ins = "jmp"
        elif ins == "jmp" and pc == line:
            ins = "nop"
        var = int(var)
        if ins == "nop":
            pc += 1
        elif "acc" == ins:
            pc += 1
            acc += var
        elif "jmp" == ins:
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
