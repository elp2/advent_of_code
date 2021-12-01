from collections import defaultdict

def return_default():
    return 0

def dd():
    return defaultdict(return_default)


CHALLENGE_DAY = "17"
REAL = open(CHALLENGE_DAY + ".txt").read()
SAMPLE = open(CHALLENGE_DAY + ".sample.txt").read()
SAMPLE_EXPECTED = 848
# SAMPLE_EXPECTED = 


def parse_lines(raw):
    # Groups.
    # split = raw.split("\n\n")
    # return list(map(lambda group: group.split("\n"), split))

    split = raw.split("\n")

    # return split # raw
    # return list(map(lambda l: l.split(" "), split)) # words.
    # return list(map(int, split))
    return list(map(lambda l: l.strip(), split)) # beware leading / trailing WS



def active_neighbors(x, y, z, w, space):
    deltas = [-1, 0, 1]
    actives = 0
    for dz in deltas:
        for dx in deltas:
            for dy in deltas:
                for dw in deltas:
                    if dz == dx and dx == dy and dx == 0 and dx == dw:
                        continue
                    nx = x + dx
                    ny = y + dy
                    nz = z + dz
                    nw = w + dw

                    key = (nx, ny, nz, nw)
                    if key in space:
                        actives += space[key]
    return actives


STEPS=6
def solve(raw):
    parsed = parse_lines(raw)
    # Debug here to make sure parsing is good.

    space = set()
    for y in range(len(parsed)):
        for x in range(len(parsed[0])):
            if parsed[y][x] == "#":
                space.add((x, y, 0, 0))
    
    for t in range(6):
        print(t)
        dneg = -1 * t - 1
        dist = len(parsed[0]) + t + 1
        new_space = set()
        for w in range(dneg, dist):
            for y in range(dneg, dist):
                for x in range(dneg, dist):
                    for z in range(dneg, dist):
                        act = 0
                        key = (x, y, z, w)
                        for dw in [-1, 0, 1]:
                            for dz in [-1, 0, 1]:
                                for dy in [-1, 0, 1]:
                                    for dx in [-1, 0, 1]:
                                        ka = (x + dx, y + dy, z + dz, w + dw)
                                        if key == ka:
                                            continue
                                        if ka in space:
                                            act += 1
                        if key in space and act in [2, 3]:
                            new_space.add(key)
                        elif key not in space and act == 3:
                            new_space.add(key)
        space = new_space
    return len(space)


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
