from collections import defaultdict

def return_default():
    return 0

def dd():
    return defaultdict(return_default)


CHALLENGE_DAY = "13"
REAL = open(CHALLENGE_DAY + ".txt").read()
SAMPLE = open(CHALLENGE_DAY + ".sample.txt").read()
SAMPLE_EXPECTED = 295
# SAMPLE_EXPECTED = 


def parse_lines(raw):
    # Groups.
    # split = raw.split("\n\n")
    # return list(map(lambda group: group.split("\n"), split))

    split = raw.split("\n")
    earliest_timestamp = int(split[0])
    ids = split[1].split(",")
    return (earliest_timestamp, ids)

    # return split # raw
    # return list(map(lambda l: l.split(" "), split)) # words.
    # return list(map(int, split))
    # return list(map(lambda l: l.strip(), split)) # beware leading / trailing WS

def solve(raw):
    et, ids = parse_lines(raw)
    # Debug here to make sure parsing is good.
    ret = 0
    afters = []
    busids = []
    min_id = 1000000000000
    for busid in ids:
        if "x" == busid:
            continue
        busid = int(busid)
        times = busid
        times = int(times)
        while times < et:
            times += busid
        if times < min_id:
            min_bus = busid
            min_id = times
        afters.append(times)


    return min_bus * (min_id - et)

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
