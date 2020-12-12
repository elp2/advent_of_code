from collections import defaultdict

def return_default():
    return 0

def dd():
    return defaultdict(return_default)


CHALLENGE_DAY = "12"
REAL = open(CHALLENGE_DAY + ".txt").read()
SAMPLE = open(CHALLENGE_DAY + ".sample.txt").read()

SAMPLE_EXPECTED = 25
# SAMPLE_EXPECTED = 
def parse_lines(raw):
    # Groups.
    # split = raw.split("\n\n")
    # return list(map(lambda group: group.split("\n"), split))

    split = raw.split("\n")

    return split # raw
    # return list(map(lambda l: l.split(" "), split)) # words.
    # return list(map(int, split))
    # return list(map(lambda l: l.strip(), split)) # beware leading / trailing WS

DIRS = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def solve(raw):
    parsed = parse_lines(raw)
    dir = 0
    x = y = 0
    for line in parsed:
        action = line[0]
        num = int(line[1:])
        print(action, num)
        move_dir = None
        if action == "N":
            move_dir = 3
        elif action == "S":
            move_dir = 1
        elif action == "E":
            move_dir = 0
        elif action == "W":
            move_dir = 2
        elif action == "L":
            times = int(num / 90)
            dir = (dir + (4000 - times)) % 4
        elif action == "R":
            times = int(num / 90)
            dir = (dir + (4000 + times)) % 4
        elif action == "F":
            move_dir = dir
        if move_dir != None:
            dx, dy = DIRS[move_dir]
            x += dx * num
            y += dy * num
    return abs(x) + abs(y)

    # Debug here to make sure parsing is good.
    ret = 0

    return ret

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
