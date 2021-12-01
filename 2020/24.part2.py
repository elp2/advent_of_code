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
    

def route_from_str(line):
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
    return r

def parse_lines(raw):
    # Groups.
    # groups = raw.split("\n\n")
    # return list(map(lambda group: group.split("\n"), groups))

    routes = []    
    lines = raw.split("\n")
    
    for line in lines:
        r = route_from_str(line)
        routes.append(r)

    return routes


def route_dirs(route):
    dirs = defaultdict(lambda: 0)

    for r in route:
        dirs[r] += 1

    changed = True
    # print(dirs)

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

def route_key(route):
    route.sort()
    dirs = route_dirs(route)        
    # print("-------------")
    key = ""
    for k in ["e", "w", "ne", "nw", "se", "sw"]:
        v = dirs[k]
        while v != 0:
            key += k
            v -= 1
    # print(",".join(route), "-> ", key)
    return key


def get_tiles(routes):
    # Debug here to make sure parsing is good.
    tiles = defaultdict(lambda: 0)
    
    for route in routes:
        key = route_key(route)
        tiles[key] += 1
    return tiles

def solve1(raw):
    routes = parse_lines(raw)

    tiles = get_tiles(routes)
    ret = 0
    for tv in tiles.values():
        if tv % 2 == 1:
            ret += 1
    return ret

assert solve1(SAMPLE) == SAMPLE_EXPECTED
assert solve1(REAL) == 434

def adj_tiles(key):
    at = []
    for adj in  ["e", "w", "ne", "nw", "se", "sw"]:
        route = route_from_str(adj + key)
        rk = route_key(route)
        at.append(rk)
    return at

def mutate_tiles(key, tiles, new_tiles):
    if key in new_tiles:
        return

    adj_blacks = 0
    for ak in adj_tiles(key):
        if ak in tiles and tiles[ak] % 2 == 1:
            adj_blacks += 1
    
    if key in tiles and tiles[key] % 2 == 1:
        # Black tile might cause white not in list to flip.
        for ak in adj_tiles(key):
            if not ak in tiles or tiles[ak] % 2 == 0:
                mutate_tiles(ak, tiles, new_tiles)
        if adj_blacks == 0 or adj_blacks > 2:
            new_tiles[key] = 0
        else:
            new_tiles[key] = 1
    else:
        if adj_blacks == 2:
            new_tiles[key] = 1
        else:
            new_tiles[key] = 0
    
    assert key in new_tiles

def solve2(raw):
    routes = parse_lines(raw)
    tiles = get_tiles(routes)


    for day in range(1, 101):
        new_tiles = {}
        for tk in tiles.keys():
            mutate_tiles(tk, tiles, new_tiles)

        tiles = new_tiles
        ret = 0
        for tv in tiles.values():
            if tv % 2 == 1:
                ret += 1
        print("Day ", day, ": ", ret)

    ret = 0
    for tv in tiles.values():
        if tv % 2 == 1:
            ret += 1
    return ret

#assert solve2(SAMPLE) == 2208
print("P2: ", solve2(REAL))

# print("SOLUTION: ", solved)
# import pandas as pd
# df=pd.DataFrame([str(solved)])
# df.to_clipboard(index=False,header=False)
# print("COPIED TO CLIPBOARD")
