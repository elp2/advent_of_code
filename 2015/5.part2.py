from collections import defaultdict, deque
import re

CHALLENGE_DAY = "5"
REAL = open(CHALLENGE_DAY + ".txt").read()
SAMPLE = open(CHALLENGE_DAY + ".sample2.txt").read()
SAMPLE_EXPECTED = 2

def parse_lines(raw):
    # Groups.
    # groups = raw.split("\n\n")
    # return list(map(lambda group: group.split("\n"), groups))
    
    lines = raw.split("\n")
    return lines # raw
    # return list(map(lambda l: l.split(" "), lines)) # words.
    # return list(map(int, lines))
    # return list(map(lambda l: l.strip(), lines)) # beware leading / trailing WS

def obeys_letter_rule(word):
    for i in range(len(word) - 2):
        if word[i] == word[i + 2]:
            return True
    return False

def repeat_twice_no_overlaps(word):
    for i in range(0, len(word) - 2):
        sub = word[i:i+2]
        assert len(sub) == 2
        if sub in word[i+2:]:
            return True
    return False

def is_nice(word):
    if not repeat_twice_no_overlaps(word):
        print("No RTNO")
        return False

    if obeys_letter_rule(word):
        return True
    else:
        print("disobeys letter rule")
        return False


    

def solve(raw):
    parsed = parse_lines(raw)
    ret = 0

    for word in parsed:
        print(word)
        if is_nice(word):
            ret += 1
        print("\n")
    return ret

sample = solve(SAMPLE)
if sample != SAMPLE_EXPECTED:
    print("SAMPLE FAILED: ", sample, " != ", SAMPLE_EXPECTED)
assert sample == SAMPLE_EXPECTED
print("\n*** SAMPLE PASSED ***\n")

solved = solve(REAL)
print("SOLUTION: ", solved) # 174 too low
import pandas as pd
df=pd.DataFrame([str(solved)])
df.to_clipboard(index=False,header=False)
print("COPIED TO CLIPBOARD")
