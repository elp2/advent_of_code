from collections import defaultdict, deque, Counter
from itertools import combinations, combinations_with_replacement, permutations
from functools import reduce
import math
# import numpy as np
from operator import add, mul, itemgetter, attrgetter
import re

DS = [[-1, 0], [1, 0], [0, 1], [0, -1]]
DS8 = DS + [[-1, -1], [1, -1], [-1, 1], [1, 1]]
def arounds_inside(x, y, diagonals, w, h):
    ret = []
    for dx, dy in DS8 if diagonals else DS:
        ret.append((x + dx, y + dy))


CHALLENGE_DAY = "22"
REAL = open(CHALLENGE_DAY + ".txt").read()

SAMPLE_EXPECTED = 2758514936282235
if SAMPLE_EXPECTED:
    SAMPLE = open(CHALLENGE_DAY + ".s.txt").read()


def parse_lines(raw):
    ret = []
    for l in raw.split("\n"):
        state, ranges = l.split(" ")
        x1, x2, y1, y2, z1, z2 = [int(a) for a in re.findall(r"-?\d+", l)]
        ret.append((state, ( x1, x2, y1, y2, z1, z2)))

    return ret

def intersect(a, b):
    (ax1, ax2, ay1, ay2, az1, az2) = a
    (bx1, bx2, by1, by2, bz1, bz2) = b
    if ax1 > bx2 or ax2 < bx1:
        return None
    if ay1 > by2 or ay2 < by1:
        return None
    if az1 > bz2 or az2 < bz1:
        return None
    x1 = max(ax1, bx1)
    x2 = min(ax2, bx2)
    y1 = max(ay1, by1)
    y2 = min(ay2, by2)
    z1 = max(az1, bz1)
    z2 = min(az2, bz2)

    return (x1, x2, y1, y2, z1, z2)


assert (0, 3, 2, 5, 3, 9) == intersect((-1, 3, -100, 5, 3, 9), (0, 5, 2, 10, 1, 10))
assert (0, 2, 0, 2, 0, 2) == intersect((0, 2, 0, 2, 0, 2), (-10, 10, -100, 10, -20, 10))


def contains(parent, child):
    (x1, x2, y1, y2, z1, z2) = child
    (sx1, sx2, sy1, sy2, sz1, sz2) = parent
    return sx1 <= x1 <= x2 <= sx2 and sy1 <= y1 <= y2 <= sy2 and sz1 <= z1 <= z2 <= sz2


def cube_size(cube):
    (x1, x2, y1, y2, z1, z2) = cube
    return (x2 - x1 + 1) * (y2 - y1 + 1) * (z2 - z1 + 1)

assert cube_size((1, 1, 1, 1, 1, 1)) == 1
assert cube_size((10, 12, 10, 12, 10, 12)) == 27


def valid_cube(cube):
    (x1, x2, y1, y2, z1, z2) = cube
    return x1 <= x2 and y1 <= y2 and z1 <= z2


def subtract(on_cube, off_cube):

    if contains(off_cube, on_cube):
        return []
    off_cube = intersect(on_cube, off_cube)
    if not off_cube:
        return [on_cube]

    (x1, x2, y1, y2, z1, z2) = on_cube
    (sx1, sx2, sy1, sy2, sz1, sz2) = off_cube


    ret = []
    ret.append((x1, sx1-1, y1, y2, z1, z2))
    ret.append((sx2 + 1, x2, y1, y2, z1, z2))
    ret.append((sx1, sx2, y1, sy1-1, z1, z2))
    ret.append((sx1, sx2, sy2+1, y2, z1, z2))
    ret.append((sx1, sx2, sy1, sy2, z1, sz1 - 1))
    ret.append((sx1, sx2, sy1, sy2, sz2 + 1, z2))

    ret = [r for r in ret if valid_cube(r)]
    return ret

# def subtract_old(on_cube, off_cube):
#     ret = []
#     (x1, x2, y1, y2, z1, z2) = on_cube
#     (sx1, sx2, sy1, sy2, sz1, sz2) = off_cube

#     xs = sorted(dict.fromkeys([x1, x2, sx1, sx2]))
#     ys = sorted(dict.fromkeys([y1, y2, sy1, sy2]))
#     zs = sorted(dict.fromkeys([z1, z2, sz1, sz2]))

#     xs2 = [(xs[i], xs[i+1] - 1) for i in range(len(xs) - 1)]

#     ret = []
#     for i in range(len(xs) - 1):
#         for j in range(len(ys) - 1):
#             for k in range(len(zs) - 1):
#                 cube = (xs[i], xs[i+1] - 1, ys[j], ys[j+1] - 1, zs[k], zs[k+1] - 1)
#                 print(cube)
#                 if contains(off_cube, cube) or not contains(on_cube, cube):
#                     print(cube, "skip")

#                     continue
#                 else:
#                     print(cube, "keep")                 
#                     ret.append(cube)
#     return ret

s1 = subtract((0, 2, 0, 2, 0, 2), (1, 1, 1, 1, 1, 1))
print(s1, sum(map(cube_size, s1)))

def subtract_list(cubes, tosub):
    ret = []
    for c in cubes:
        ret += subtract(c, tosub)
    return ret


def add(cubes, toadd):
    ret = [toadd]
    for c in cubes:
        i = intersect(c, toadd)
        if i:
            ret += subtract(c, i)
        else:
            ret.append(c)

    return ret

def part1(raw):
    parsed = parse_lines(raw)
    # Debug here to make sure parsing is good.
    ret = 0

    squares = set()
    for (state, ( x1, x2, y1, y2, z1, z2)) in parsed:
        for x in range(max(-50, x1), min(50 + 1, x2 + 1)):
            for y in range(max(-50, y1), min(50 + 1, y2 + 1)):
                for z in range(max(-50, z1), min(50 + 1, z2 + 1)):
                    if state == "on":
                        squares.add((x, y, z))
                    else:
                        if (x, y, z) in squares:
                            squares.remove((x, y, z))
    return len(squares)

def solve(raw):
    parsed = parse_lines(raw)

    cubes = []
    for state, cube in parsed:
        if state == "on":
            cubes = add(cubes, cube)
        else:
            cubes = subtract_list(cubes, cube)

        # print(cubes)
        print(state, len(cubes))

    return sum([cube_size(c) for c in cubes])

def test(i):
    raw = "\n".join(REAL.split("\n")[i-1:i + 1])

    p1 = part1(raw)
    p2 = solve(raw)
    assert p1 == p2
test(12)
for i in range(1, 20):
    test(i)


if SAMPLE_EXPECTED != None:
    sample = solve(SAMPLE)
    if sample != SAMPLE_EXPECTED:
        print("SAMPLE FAILED: ", sample, " != ", SAMPLE_EXPECTED)
    assert sample == SAMPLE_EXPECTED
    print("\n*** SAMPLE PASSED ***\n")
else:
    print("Skipping sample")

solved = solve(REAL)
print("SOLUTION: ", solved)
