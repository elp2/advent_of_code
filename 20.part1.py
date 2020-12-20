from collections import defaultdict

def return_default():
    return []

def dd():
    return defaultdict(return_default)


CHALLENGE_DAY = "20"
REAL = open(CHALLENGE_DAY + ".txt").read()
SAMPLE = open(CHALLENGE_DAY + ".sample.txt").read()
# SAMPLE_EXPECTED = 

def parse_tile(tile):
    tile = tile.strip()
    lines = tile.split("\n")
    tile_id = int(lines[0].split(" ")[1].replace(":", ""))
    glines = lines[1:]
    grid = list(map(list, glines))
    edges = []
    edges.append("".join(grid[0]))
    edge = []
    for y in range(len(grid)):
        edge.append(grid[y][-1])
    edges.append("".join(edge))
    edges.append("".join(grid[-1]))

    edge = []
    for y in range(len(grid)):
        edge.append(grid[y][0])
    edges.append("".join(edge))

    return tile_id, edges

def parse_lines(raw):
    # Groups.
    split = raw.split("\n\n")


    return list(map(parse_tile, split))

SAMPLE_EXPECTED = None
def solve(raw):
    parsed = parse_lines(raw)

    num_edge_matches = {}
    for num, edges in parsed:
        edge_matches = []
        for e in edges:
            rev = e[::-1]
            here = []
            for k, ke in parsed:
                if k == num:
                    continue
                for kei in ke:                    
                    if e == kei or rev == kei:
                        here.append(k)
            edge_matches.append(here)
        num_edge_matches[num] = edge_matches

    # matches = defaultdict(return_default)
    # for num, edges in parsed:
    #     for e in edges:
    #         print(num, e)         
    #         matches[e].append(num)

    # def r0():
    #     return 0
    # by_num = defaultdict(r0)
    # for edge, paired in matches.items():
    #     if len(paired) == 1:
    #         continue
    #     elif len(paired) == 2:
    #         for p in paired:
    #             by_num[p] += 1
    #     else:
    #         assert False
    

    corners = set()
    for n, em in num_edge_matches.items():
        num_em = 0
        for ee in em:
            if ee:
                num_em += 1
        if num_em == 2:
            corners.add(n)


    ret = 1
    assert len(corners) == 4
    for c in corners:
        ret *= c


    return ret

def test_parsing(lines):
    if isinstance(lines, list):
        for i in range(min(5, len(lines))):
            print(lines[i])
    elif isinstance(lines, dict) or isinstance(lines, defaultdict):
        nd = {}
        for k in list(lines.keys())[0: 5]:
            print("\"" + k + "\": " + str(lines[k]))
test_parsing(parse_lines(SAMPLE))
print("^^^^^^^^^PARSED SAMPLE SAMPLE^^^^^^^^^")

sample = solve(SAMPLE)
if SAMPLE_EXPECTED is None:
    print("*** SKIPPING SAMPLE! ***")
else:
    assert sample == SAMPLE_EXPECTED
    print("*** SAMPLE PASSED ***")

solved = solve(REAL)
print("SOLUTION: ", solved)
import pandas as pd
df=pd.DataFrame([str(solved)])
df.to_clipboard(index=False,header=False)
print("COPIED TO CLIPBOARD")
# assert solved
