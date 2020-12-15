from collections import defaultdict

def return_default():
    return 0

def dd():
    return defaultdict(return_default)


CHALLENGE_DAY = "15"
REAL = "16,11,15,0,1,7"
SAMPLE ="0,3,6"
SAMPLE_EXPECTED = 436
# SAMPLE_EXPECTED = 


def parse_lines(raw):
    return list(map(int, raw.split(",")))
    # Groups.
    # split = raw.split("\n\n")
    # return list(map(lambda group: group.split("\n"), split))

    # split = raw.split("\n")

    # return split # raw
    # return list(map(lambda l: l.split(" "), split)) # words.
    # return list(map(int, split))
    # return list(map(lambda l: l.strip(), split)) # beware leading / trailing WS

HISTORY_LEN = 2020
def solve(raw):
    history = parse_lines(raw)
    while len(history) != HISTORY_LEN:
        prev = history[-1]
        times = history.count(prev)
        if times == 1:
            here = 0
        elif times > 1:
            recent = len(history) - 1
            while history[recent] != prev:
                recent -= 1
            before = recent - 1
            while history[before] != prev:
                before -= 1
            here = recent - before
        history.append(here)
        print(len(history), here)
    return history[-1]

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
