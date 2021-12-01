from collections import defaultdict, deque
import re

CHALLENGE_DAY = "11"


def meets(password):
    three_increasing = False
    for i in range(len(password) - 3):
        if password[i] + 2 == password[i+2] and password[i] + 1 == password[i + 1]:
            three_increasing = True

    if not three_increasing:
        return False
    
    double_alphas = set()
    for i in range(len(password) - 1):
        if password[i] == password[i + 1]:
            double_alphas.add(password[i])
    return len(double_alphas) >= 2
    
bad_digits = [ord(x) - ord('a') for x in 'iol']
def inc(password):
    def inc_digit(digit):
        digit += 1
        if digit in bad_digits:
            digit += 1
        digit %= 26
        return digit
    i = len(password) - 1
    while True:
        inced = inc_digit(password[i])
        password[i] = inced
        if inced != 0:
            return password
        else:
            i -= 1
    return password

def solve(parsed):
    password = list(map(lambda c: ord(c) - ord('a'), parsed))
    while True:
        password = inc(password)
        if meets(password):
            break


    alpha = "".join(map(lambda c: chr(c + ord('a')), password))
    return alpha

solved = solve("hxbxwxba")
print("SOLUTION: ", solved) # hxbxxyzz
solved = solve(solved)
print("Part2: ", solved) # hxbxxyzz

import pandas as pd
df=pd.DataFrame([str(solved)])
df.to_clipboard(index=False,header=False)
print("COPIED TO CLIPBOARD")
