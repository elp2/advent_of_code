from collections import defaultdict, deque
import re

SAMPLE_EXPECTED = 14897079
# SAMPLE_EXPECTED = 

def transform(subject_num, loop_size):
    val = 1
    for loop in range(loop_size):
        val *= subject_num
        val = val % 20201227
    return val


def find_loop_size(expected):
    subject_num = 7
    ls = 0
    val = 1
    while True:
        ls += 1
        if ls % 1000 == 0:
            print(ls)
        val *= subject_num
        if val >= 20201227:
            val = val % 20201227
        if val == expected:
            return ls


def solve(true_card_public, true_door_public):
    card_loop_size = find_loop_size(true_card_public)
    print("cls", card_loop_size)
    door_loop_size = find_loop_size(true_door_public)
    print(door_loop_size)
    card_ek = transform(true_door_public, card_loop_size)
    # door_ek = transform(card_public, door_loop_size)


    return card_ek

sample = solve(5764801, 17807724)
if sample != SAMPLE_EXPECTED:
    print("SAMPLE FAILED: ", sample, " != ", SAMPLE_EXPECTED)
assert sample == SAMPLE_EXPECTED
print("\n*** SAMPLE PASSED ***\n")

solved = solve(12232269, 19452773)
print("SOLUTION: ", solved)
import pandas as pd
df=pd.DataFrame([str(solved)])
df.to_clipboard(index=False,header=False)
print("COPIED TO CLIPBOARD")
