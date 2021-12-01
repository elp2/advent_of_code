from collections import defaultdict, deque, Counter
from itertools import combinations, combinations_with_replacement, permutations
import hashlib
import math
import numpy as np
from operator import add, mul, itemgetter, attrgetter
import re
import sys
sys.setrecursionlimit(1500)
assert 1500 == sys.getrecursionlimit()

def directions_for(passcode, path):
    h = (passcode + path).encode()
    h = hashlib.md5(h).hexdigest()

    return map(lambda d: d in "bcdef", h[:4])

def flatten(t):
    return [item for sublist in t for item in sublist]

ON_TEXT = '\u2588'
OFF_TEXT = '\u2592'

DAY = "17"
REAL = "pslxynzg"

SAMPLE_EXPECTED = "DDRRRD"

DIRS = [(0, -1, "U"), (0, 1, "D"), (-1, 0, "L"), (1, 0, "R")]

def solve(passcode, longest_path=False):
    q = deque()
    q.append((0, 0, ""))
    longest_path_len = 0
    while q:
        x, y, path = q.popleft()
        if x == 3 and y == 3:
            if longest_path:
                old = longest_path_len
                longest_path_len = max(len(path), longest_path_len)
                if old != longest_path_len:
                    print(longest_path_len)
                continue
            else:
                return path
        for i, d in enumerate(directions_for(passcode, path)):
            if not d:
                continue
            dx, dy, pathchar = DIRS[i]
            nx = x + dx
            ny = y + dy
            if nx in range(4) and ny in range(4):
                q.append((nx, ny, path + pathchar))

    return longest_path_len

def solve_dfs(passcode, x, y, path):
    # print(x, y, path)
    depth = 0
    for i, d in enumerate(directions_for(passcode, path)):
        if not d:
            continue
        dx, dy, pathchar = DIRS[i]
        nx = x + dx
        ny = y + dy
        if nx in range(4) and ny in range(4):
            depth = max(depth, solve_dfs(passcode, nx, ny, path + pathchar))
    return depth

    

if SAMPLE_EXPECTED != None:
    SAMPLE = "ihgpwlah"
    sample = solve(SAMPLE)
    if sample != SAMPLE_EXPECTED:
        print("SAMPLE FAILED: ", sample, " != ", SAMPLE_EXPECTED)
    assert sample == SAMPLE_EXPECTED
    print("\n*** SAMPLE PASSED ***\n")
else:
    print("Skipping sample")

part1 = solve(REAL)
print("Part 1: ", part1)

part2 = solve(REAL, True)
print("Part 2: ", part2)

try:
    import pandas as pd
    df=pd.DataFrame([str(solved)])
    df.to_clipboard(index=False,header=False)
    print("COPIED TO CLIPBOARD")
except ModuleNotFoundError:
    print("Pandas not installed.")
