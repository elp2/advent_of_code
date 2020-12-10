from collections import defaultdict

def return_default():
    return 0

def dd():
    return defaultdict(return_default)


CHALLENGE_DAY = "10"
REAL = open(CHALLENGE_DAY + ".txt").read()
SAMPLE = open(CHALLENGE_DAY + ".sample").read()
SAMPLE_EXPECTED = 8
# SAMPLE_EXPECTED = 


def parse_lines(raw):
    # Groups.
    # split = raw.split("\n\n")
    # return list(map(lambda group: group.split("\n"), split))

    split = raw.split("\n")

    # return split # raw
    # return list(map(lambda l: l.split(" "), split)) # words.
    return list(map(int, split))
    # return list(map(lambda l: l.strip(), split)) # beware leading / trailing WS

#123 less and is OK
# it's device is 3 + max of my adapters
# My seat has jolt of 0

SEEN={}

def has_path(adapters, target, prev, i):
    ret = 0
    if i >= len(adapters):
        return 0
    here = adapters[i]
    if target - here == 3:
        ret = 1

    diff = here - prev
    print(here, i , diff)
    if diff > 3:
        # Invalid jump
        return 0
    if diff <= 3:
        key = here
        if key in SEEN:
            return SEEN[key]

        # Valid jump from prev
        j = i + 1
        nexts = []
        while True:
            nxt = has_path(adapters, target, here, j)
            if nxt == 0:
                break
            else:
                nexts.append(nxt)
                j += 1
        SEEN[key] = sum(nexts) + ret
        return SEEN[key]
    assert False


def solve(raw):
    assert len(SEEN) == 0
    parsed = parse_lines(raw)
    # Debug here to make sure parsing is good.
    ret = 0
    max_joltage = max(parsed) + 3
    parsed.sort()

    ret = 0
    for i in range(len(parsed)):
        if parsed[i] <= 3:
            ret += has_path(parsed, max_joltage, 0, i)
    
    print(SEEN)
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

SEEN={}
sample2 = solve(open("10.sample2.txt").read())
assert sample2 == 19208

SEEN={}
solved = solve(REAL)
print("SOLUTION: ", solved)
import pandas as pd
df=pd.DataFrame([str(solved)])
df.to_clipboard(index=False,header=False)
print("COPIED TO CLIPBOARD")
# assert solved
