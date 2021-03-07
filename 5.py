from collections import defaultdict, deque
import re

CHALLENGE_DAY = "5"
REAL = open(CHALLENGE_DAY + ".txt").read()
SAMPLE = open(CHALLENGE_DAY + ".sample.txt").read()
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

def is_nice(word):
    vowels = "aeiou"
    num_vowels = 0
    for v in vowels:
        if v in word:
            num_vowels += word.count(v)
    if num_vowels < 3:
        print("Not Enough vowels: ", num_vowels)
        return False
    letters = "abcdefghijklmnopqrstuvwxyz"
    num_doubles = 0
    for l in letters:
        dob = l + l
        if dob in word:
            num_doubles += 1
    if num_doubles < 1:
        print("No double")
        return False
    naughties = ["ab", "cd", "pq", "xy"]
    for n in naughties:
        if n in word:
            print("naughty: ", n)
            return False
    return True

    

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
