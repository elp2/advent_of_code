from collections import defaultdict, deque
import re

CHALLENGE_DAY = "24"
REAL = open(CHALLENGE_DAY + ".txt").read()
SAMPLE = open(CHALLENGE_DAY + ".sample.txt").read()
SAMPLE_EXPECTED = 10
# SAMPLE_EXPECTED = 


# class Tile:
#     def __init__(self):
#         self.ne = None
#         self.nw = None
#         self.sw = None
#         self.se = None
#         self.w = None
#         self.e = None
    


def parse_lines(raw):
    # Groups.
    # groups = raw.split("\n\n")
    # return list(map(lambda group: group.split("\n"), groups))

    routes = []    
    lines = raw.split("\n")
    
    for line in lines:
        line = line.strip()
        r = []
        i = 0
        while i < len(line):
            c = line[i]
            if c == "s" or c == "n":
                r.append(line[i:i+2])
                i += 2
            else:
                r.append(line[i])
                i += 1
        routes.append(r)

    return routes


def route_dirs(route):
    dirs = defaultdict(lambda: 0)

    for r in route:
        dirs[r] += 1

    changed = True
    print(dirs)

    offsets = {
        ("e", "w"): None,
        ("ne", "sw"): None,
        ("nw", "se"): None,
        ("ne", "se"): "e",
        ("nw", "sw"): "w",
        ("w", "se"): "sw",
        ("w", "ne"): "nw",
        ("e", "nw"): "ne",
        ("e", "sw"): "se",
    }

    while changed:
        changed = False
        for (ka, kb), replace_key in offsets.items():
            if dirs[ka] and dirs[kb]:
                changed = True
                mink = min(dirs[ka], dirs[kb])
                dirs[ka] -= mink
                dirs[kb] -= mink
                if replace_key != None:
                    dirs[replace_key] += mink
    return dirs


def solve(raw):
    routes = parse_lines(raw)
    # Debug here to make sure parsing is good.
    tiles = defaultdict(lambda: 0)
    
    for route in routes:
        route.sort()
        dirs = route_dirs(route)        
        print("-------------")
        key = ""
        for k in ["e", "w", "ne", "nw", "se", "sw"]:
            v = dirs[k]
            if v != 0:
                key += k + str(v)
        print(",".join(route), "-> ", key)

        tiles[key] += 1


    ret = 0
    for tk, tv in tiles.items():
        if tv % 2 == 1:
            ret += 1
    return ret

sample = solve(SAMPLE)
if sample != SAMPLE_EXPECTED:
    print("SAMPLE FAILED: ", sample, " != ", SAMPLE_EXPECTED)
assert sample == SAMPLE_EXPECTED
print("\n*** SAMPLE PASSED ***\n")

solved = solve(REAL)
print("SOLUTION: ", solved)
import pandas as pd
df=pd.DataFrame([str(solved)])
df.to_clipboard(index=False,header=False)
print("COPIED TO CLIPBOARD")
