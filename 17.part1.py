from collections import defaultdict

def return_default():
    return 0

def dd():
    return defaultdict(return_default)


CHALLENGE_DAY = "17"
REAL = open(CHALLENGE_DAY + ".txt").read()
SAMPLE = open(CHALLENGE_DAY + ".sample.txt").read()
SAMPLE_EXPECTED = 112
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


def active_neighbors(x, y, z, space):
    deltas = [-1, 0, 1]
    actives = 0
    for dz in deltas:
        for dx in deltas:
            for dy in deltas:
                if dz == dx and dx == dy and dx == 0:
                    continue
                nx = x + dx
                ny = y + dy
                nz = z + dz

                key = (nx, ny, nz)
                if key in space:
                    actives += space[key]
    return actives


STEPS=6
def solve(raw):
    parsed = parse_lines(raw)
    # Debug here to make sure parsing is good.

    space = {}
    z = 0
    for y in range(len(parsed)):
        for x in range(len(parsed[y])):
            here = parsed[y][x]
            if here == "#":
                active = 1
            else:
                active = 0
            space[(x, y, z)] = active
    
    for z in range(-10, 20):
        for y in range(-10, 20):
            for x in range(-10, 20):
                key = (x, y, z)
                if key not in space:
                    space[key] = 0

    for times in range(6):
        new_space = {}
        for (x, y, z), active in space.items():
            ans = active_neighbors(x, y, z, space)
            if active == 1:
                if ans in [2,3]:
                    nact = 1
                else:
                    nact = 0
            else:
                if ans == 3:
                    nact = 1
                else:
                    nact = 0
            new_space[(x, y, z)] = nact

        space = new_space


    ret = sum(space.values())

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
