from collections import defaultdict

def return_default():
    return 0

def dd():
    return defaultdict(return_default)


CHALLENGE_DAY = "14"
REAL = open(CHALLENGE_DAY + ".txt").read()
SAMPLE = open(CHALLENGE_DAY + ".sample.txt").read()
SAMPLE_EXPECTED = 165
# SAMPLE_EXPECTED = 


def read_mask(line):
    line = line.strip()
    maskstr = line.split(" = ")[1]
    andstr = maskstr.replace("X", "1")
    orstr = maskstr.replace("X", "0")
    print("Mask -> ", andstr, orstr)
    return (int(andstr, 2), int(orstr, 2))

def parse_lines(raw):
    # Groups.
    # split = raw.split("\n\n")
    # return list(map(lambda group: group.split("\n"), split))

    split = raw.split("\n")
    return split


    # return split # raw
    # return list(map(lambda l: l.split(" "), split)) # words.
    # return list(map(int, split))
    # return list(map(lambda l: l.strip(), split)) # beware leading / trailing WS

def parse_mem(line):
    line = line.strip()
    val = int(line.split(" = ")[1])
    loc = line[line.index("[") + 1:line.index("]")]
    return int(loc), val

def solve(raw):
    parsed = parse_lines(raw)
    # Debug here to make sure parsing is good.
    memory = {}
    andi, ori = None, None
    for line in parsed:
        if line.startswith("mask"):
            andi, ori = read_mask(line)
        else:
            loc, val = parse_mem(line)

            anded = val & andi
            ored = anded | ori
            print(bin(val), bin(anded), bin(ored), ored)
            memory[loc] = ored

    return sum(memory.values())

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
import pandas as pd
df=pd.DataFrame([str(solved)])
df.to_clipboard(index=False,header=False)
print("COPIED TO CLIPBOARD")
# assert solved
