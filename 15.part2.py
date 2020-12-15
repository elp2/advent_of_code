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

def add_say(turn, to_say, history):
    if to_say in history:
        near, far = history[to_say]
        history[to_say] = (turn, near)
    else:
        history[to_say] = (turn, None)

def say(turn, last, history):
    near, far = history[last]
    if far == None:
        to_say = 0
    else:
        to_say = near - far
    add_say(turn, to_say, history)

    # print(turn, to_say)
    return to_say


HISTORY_LEN = 30000000
def solve(raw):
    inp = parse_lines(raw)
    history = {}
    for round in range(len(inp)):
        add_say(round + 1, inp[round], history)
    last = inp[-1]

    for turn in range(len(inp) + 1, HISTORY_LEN + 1):
        if turn % 100000 == 0:
            print(turn)
        last = say(turn, last, history)
    return last


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

# sample = solve(SAMPLE)
# if SAMPLE_EXPECTED is None:
#     print("*** SKIPPING SAMPLE! ***")
# else:
#     assert sample == SAMPLE_EXPECTED
#     print("*** SAMPLE PASSED ***")

solved = solve(REAL)
print("SOLUTION: ", solved)
import pandas as pd
df=pd.DataFrame([str(solved)])
df.to_clipboard(index=False,header=False)
print("COPIED TO CLIPBOARD")
# assert solved
