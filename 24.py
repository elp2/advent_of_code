from collections import defaultdict, deque, Counter
from itertools import combinations, combinations_with_replacement, permutations
import math
import numpy as np
from operator import add, mul, itemgetter, attrgetter
import re

def flatten(t):
    return [item for sublist in t for item in sublist]

ON_TEXT = '\u2588'
OFF_TEXT = '\u2592'

DAY = "24"
REAL = open(DAY + ".in").read()

SAMPLE_EXPECTED = None

def parse(raw):
    board = raw.split("\n")
    poses = {}
    for y in range(len(board)):
        for x in range(len(board[y])):
            if board[y][x] in "0123456789":
                poses[board[y][x]] = (y, x)
    
    all_bests = {}
    for num in poses.keys():
        bests = {}
        q = deque()
        q.append((poses[num], 0))
        visited = set()
        while q:
            (y, x), dist = q.popleft()
            if (y, x) in visited or not (0 <= x < len(board[0])) or not (0 <= y < len(board)):
                continue
            visited.add((y, x))
            here = board[y][x]
            if here == "#":
                continue
            if here in poses.keys() and here not in bests:
                bests[here] = dist
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx = x + dx
                ny = y + dy
                q.append(((ny, nx), dist + 1))
        
        print(bests)
        all_bests[num] = bests
    return all_bests


def solve(raw):
    ret = 0
    bests = parse(raw)
    shortest_path = 10000000000
    shortest_path_back = 10000000000
    for perm in permutations(bests.keys()):
        if perm[0] != "0":
            continue
        path = 0
        for i in range(len(perm) - 1):
            a, b = perm[i: i + 2]
            path += bests[a][b]
        shortest_path = min(path, shortest_path)
        path += bests[b]['0']
        shortest_path_back = min(path, shortest_path_back)

    return shortest_path, shortest_path_back

if SAMPLE_EXPECTED != None:
    SAMPLE = open(DAY + ".sample").read()
    sample = solve(SAMPLE)
    if sample != SAMPLE_EXPECTED:
        print("SAMPLE FAILED: ", sample, " != ", SAMPLE_EXPECTED)
    assert sample == SAMPLE_EXPECTED
    print("\n*** SAMPLE PASSED ***\n")
else:
    print("Skipping sample")

sol = solve(REAL)
print("Part 1, 2: ", sol)

try:
    import pandas as pd
    df=pd.DataFrame([str(solved)])
    df.to_clipboard(index=False,header=False)
    print("COPIED TO CLIPBOARD")
except ModuleNotFoundError:
    print("Pandas not installed.")