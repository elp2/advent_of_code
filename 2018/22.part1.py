from collections import defaultdict

def return_default():
    return 0



def geologic_index(gis, x, y, depth):
    key = (x, y)
    if key in gis:
        return gis[key]
    val = erosion_level(gis, x - 1, y, depth) * erosion_level(gis, x, y - 1, depth)
    gis[key] = val
    print("Set: ", key, " = ", val)
    return val


def erosion_level(gis, x, y, depth):
    key = ("e", x, y)
    if key in gis:
        return gis[key]
    level = (geologic_index(gis, x, y, depth) + depth) % 20183
    gis[key] = level
    return level % 3



def default_gis(tx, ty):
    gis = {}
    gis[(0, 0)] = 0
    for x in range(tx + 1):
        gis[(x, 0)] = x * 16807
    for y in range(ty + 1):
        gis[(0, y)] = y * 48271
    gis[(tx, ty)] = 0
    return gis

def solve(depth, tx, ty):
    ret = 0

    gis = default_gis(tx, ty)
    for y in range(ty + 1):
        for x in range(tx + 1):
            print(x, y)
            el = erosion_level(gis, x, y, depth)
            ret += (el % 3)

    return ret

sample = solve(510, 10, 10)
assert sample == 114
print("*** SAMPLE PASSED ***")


print(solve(8103, 9, 758))
