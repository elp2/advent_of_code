from collections import defaultdict

def return_default():
    return 0

def dd():
    return defaultdict(return_default)


CHALLENGE_DAY = "13"
REAL = open(CHALLENGE_DAY + ".txt").read()
SAMPLE = open(CHALLENGE_DAY + ".sample.txt").read()
SAMPLE_EXPECTED = 1068781
# SAMPLE_EXPECTED = 


def parse_lines(raw):
    # Groups.
    # split = raw.split("\n\n")
    # return list(map(lambda group: group.split("\n"), split))

    split = raw.split("\n")
    earliest_timestamp = int(split[0])
    raw_ids = split[1].split(",")

    ids = []
    deltas = []
    skips = []
    delta = 0
    for i in raw_ids:
        if i == "x":
            delta += 1
            continue
        ids.append(int(i))
        deltas.append(delta)
        skips.append(None)
        delta += 1

    return ids, deltas, skips


    # return split # raw
    # return list(map(lambda l: l.split(" "), split)) # words.
    # return list(map(int, split))
    # return list(map(lambda l: l.strip(), split)) # beware leading / trailing WS


# def test():
#     starts = [11, 50]
#     deltas = []
#     a = 7
#     for i in range(100):



def first_skips(a, b, delta):
    pairs = []
    for i in range(1000):
        for j in range(1000):
            if i * a + delta == j * b:
                pairs.append((i, j))
    return(pairs)


def match(a, jump, b, target_delta):
    while a < b:
        a += jump
    while True:
        c = a % b
        delta = b - c
        while delta < target_delta:
            delta += b
        if delta == target_delta:
            return a
        a += jump


def solve(raw):
    ids, deltas, skips = parse_lines(raw)
    # Debug here to make sure parsing is good.

    m = ids[0]
    jump = m
    for i in range(1, len(ids)):
        b = ids[i]
        mnew = match(m, jump, b, deltas[i])
        print(i, len(ids), "@ ", m, "->", mnew)
        jump *= b
        m = mnew
    return m


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
