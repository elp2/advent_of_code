from collections import defaultdict, deque
import re
import hashlib

CHALLENGE_DAY = "4"
REAL = open(CHALLENGE_DAY + ".txt").read()
SAMPLE = open(CHALLENGE_DAY + ".sample.txt").read()
SAMPLE_EXPECTED = 1048970

def parse_lines(raw):
    # Groups.
    # groups = raw.split("\n\n")
    # return list(map(lambda group: group.split("\n"), groups))
    
    lines = raw.split("\n")
    return lines[0] # raw
    # return list(map(lambda l: l.split(" "), lines)) # words.
    # return list(map(int, lines))
    # return list(map(lambda l: l.strip(), lines)) # beware leading / trailing WS

def five0s(key, code):
    h = key + str(code)
    h = h.encode()
    mdd = hashlib.md5(h).hexdigest()
    return mdd[:6] == '000000'

def solve(raw):
    parsed = parse_lines(raw)
    # Debug here to make sure parsing is good.
    ret = 0
    while True:
        if five0s(parsed, ret):
            return ret
        if ret % 10000 == 0:
            print(ret)
        ret += 1

    return ret

# sample = solve(SAMPLE)
# if sample != SAMPLE_EXPECTED:
#     print("SAMPLE FAILED: ", sample, " != ", SAMPLE_EXPECTED)
# assert sample == SAMPLE_EXPECTED
# print("\n*** SAMPLE PASSED ***\n")

solved = solve(REAL)
print("SOLUTION: ", solved)
import pandas as pd
df=pd.DataFrame([str(solved)])
df.to_clipboard(index=False,header=False)
print("COPIED TO CLIPBOARD")
