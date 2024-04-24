from collections import defaultdict, deque, Counter
from itertools import combinations, combinations_with_replacement, permutations
from functools import reduce, cmp_to_key
import math
# import numpy as np
from operator import add, mul, itemgetter, attrgetter
import os
import re
from sys import argv

def flatten(t):
    return [item for sublist in t for item in sublist]

# Sorts with cmp. cmp < 0 for a < b, == 0 for a==b, > 0 for a > b.
def elpsort(array, cmp):
    return sorted(array, key=cmp_to_key(cmp))

ON_TEXT = '\u2588'
OFF_TEXT = '\u2592'

LEFT = 0
UP = 1
RIGHT = 2
DOWN = 3
CHAR_TO_DS = {"^": UP, ">": RIGHT, "<": LEFT, "v": DOWN}
DS = [(-1, 0), (0, -1), (1, 0), (0, 1)]
DS8 = DS + [(-1, -1), (1, -1), (-1, 1), (1, 1)]

def arounds(x, y, diagonals):
    ret = []
    for dx, dy in DS8 if diagonals else DS:
        ret.append((x + dx, y + dy))
    return ret

CHALLENGE_DAY = argv[0].split("/")[-1].replace(".py", "").replace("p2.py", "")
AOC_DIR = os.path.dirname(argv[0])

print("Day: ", CHALLENGE_DAY)

######################
SAMPLE_EXPECTED = 154
######################
assert SAMPLE_EXPECTED != None

try:
    SAMPLE = open(os.path.join(AOC_DIR, CHALLENGE_DAY + ".s.txt")).read()
except:
    print("Did you create the sample file?")

try:
    REAL = open(os.path.join(AOC_DIR, CHALLENGE_DAY + ".txt")).read()
except:
    print("Did you create the solutions file?")


def parse_lines(raw):
    lines = raw.split("\n")
    return lines


def solve(raw):
    world = parse_lines(raw)
    print(world)

    def wat(x, y):
        if 0 > y or y >= len(world):
            return None
        if 0 <= x < len(world[0]):
            return world[y][x]
        return None

    sx = 1
    sy = 0
    ex = len(world[0]) - 2
    ey = len(world) - 1

    q = deque()
    q.append((sx, sy, set([(sx, sy)]), None, ""))
    longest = 0
    longest_path = set()
    has_options = set()
    best_to = defaultdict(lambda: 0)

    has_options_ids = {"XXXXX": 0}
    while len(q):
        x, y, path, from_option, visited_has_options = q.popleft()
        path.add((x, y))
        if (from_option):
            if len(path) < best_to[(from_option, "visited_has_options")]-150: #HACCCCKKKK
                continue

        while True:
            
            if x == ex and y == ey:
                if len(path) > len(longest_path):
                    longest_path = path
                
                print("Longest: ", len(path), len(q), len(longest_path))
                break
            options = []
            for dchar in "^<v>":
                dx, dy = DS[CHAR_TO_DS[dchar]]
                nx, ny = x + dx, y + dy
                nchar = wat(nx, ny)
                if None == nchar or (nx, ny) in path or nchar == "#":
                    continue
                options.append((nx, ny))
            if len(options) > 1:
                has_options.add((x, y))
                hok = str((x, y))
                if hok not in has_options_ids:
                    has_options_ids[hok] = max(has_options_ids.values()) + 1
                hokid = has_options_ids[hok]
                visited_has_options_copy = visited_has_options[:]
                visited_has_options += "_" + str(hokid)

                btk = ((x, y), "visited_has_options")
                best_to[btk] = max(len(path), best_to[btk])
                for (ox, oy) in options:
                    path_copy = path.copy()
                    # path_copy.add((ox, oy))
                    q.append((ox, oy, path_copy, (x, y), visited_has_options_copy))
                break
            elif len(options) == 1:
                x, y = options[0]
                path.add((x, y))
            else:
                # got into a dead end
                break
                
    removing_ends = longest_path - set([sx, sy])
    removing_ends -= set([ex, ey])
    return len(removing_ends) - 1 # 5306, 5662 too low

def solve3(raw):
    world = parse_lines(raw)
    print(world)

    def wat(x, y):
        if 0 > y or y >= len(world):
            return None
        if 0 <= x < len(world[0]):
            return world[y][x]
        return None

    def options_for(x, y):
        options = []
        for di in range(4):
            dx, dy = DS[di]
            nx, ny = x + dx, y + dy
            if wat(nx, ny) in [None, "#"]:
                continue
            options.append((nx, ny))
        return options

    sx = 1
    sy = 0
    ex = len(world[0]) - 2
    ey = len(world) - 1

    # Find all choicepoints
    choicepoints = [(sx, sy), (ex, ey)]
    q = deque()
    q.append((sx, sy))
    seen = set()
    while len(q) > 0:
        x, y = q.popleft()
        if (x, y) in seen:
            continue
        seen.add((x, y))

        options = options_for(x, y)
        if len(options) >= 3:
            choicepoints.append((x, y))
        for (ox, oy) in options:
            q.append((ox, oy))
    
    print(choicepoints)

    def paths_to_cps(x, y, path_here_orig):
        ret = []
        q = deque()

        for ax, ay in options_for(x, y):
            q.append((ax, ay, path_here_orig))
        while len(q):
            x, y, path_here = q.popleft()
            if (x, y) in choicepoints:
                ret.append(((x, y), set(path_here)))
            else:
                for ax, ay in options_for(x, y):
                    if (ax, ay) in path_here:
                        continue
                    phc = path_here.copy()
                    phc.append((x, y))
                    q.append((ax, ay, phc))
        return ret
            

    paths = defaultdict(lambda: [])
    for (x, y) in choicepoints:
        paths[(x, y)] = paths_to_cps(x, y, [(x, y)])

    # for k in paths.keys():
    #     print(k, "->", paths[k])

    def max_recurse(at, target, pathset):
        ret = 0
        if at == target:
            return len(pathset)
        for cp, path_to_cp in paths[at]:
            if not path_to_cp.isdisjoint(pathset):
                continue
            newpath = path_to_cp.union(pathset)
            ret = max(ret, max_recurse(cp, target, newpath))

        return ret

    def pathsto(at, target, seen):
        ret = 0
        if at in seen:
            return 0
        if at == target:
            return 1
        for cp, path_to_cp in paths[at]:
            seencopy = seen.copy()
            seencopy.add(at)
            ret += pathsto(cp, target, seencopy)

        return ret


    print("pathsto", pathsto((sx, sy), (ex, ey), set()))
    return max_recurse((sx, sy), (ex, ey), set())


    # Do a search from each choicepoint to another choicepoint, getting the path there
    # Find all paths from start to end, that go through these without repeating path parts


sample = solve(SAMPLE)
if sample != SAMPLE_EXPECTED:
    print("SAMPLE FAILED: ", sample, " != ", SAMPLE_EXPECTED)
assert sample == SAMPLE_EXPECTED
print("\n*** SAMPLE PASSED ***\n")

solved = solve(REAL)
print("SOLUTION: ", solved)