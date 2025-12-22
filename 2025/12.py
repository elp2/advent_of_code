from collections import defaultdict, deque, Counter
from itertools import combinations, combinations_with_replacement, permutations, product
from functools import reduce, cmp_to_key
from operator import add, mul, itemgetter, attrgetter
import os
import sys

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, root_dir)
from aoc_elp import *

######################
SAMPLE_EXPECTED = 2
######################
assert SAMPLE_EXPECTED != None, "Must enter sample value"

def parse_group(group):
    lines = group.split("\n")
    ret = []
    for y, line in enumerate(lines):
        line = line.strip()
        assert len(line) != 0

        split = line.split(" ")

        for x, xc in enumerate(split):
            pass

        assert len(split) != 0
        ret.append(split)

    return ret


def shape_perms(shape):
    ret = []
    def rotate(s):
        r = [[0] * len(s) for _ in range(len(s))]
        for y in range(len(s)):
            for x in range(len(s)):
                r[x][y] = s[y][x]
        return r
        
    def flip(s):
        r = [[0] * len(s) for _ in range(len(s))]
        for y in range(len(s)):
            for x in range(len(s)):
                r[y][x] = s[y][len(s) - x - 1]
        return r

    def addnew(r, to):
        equals = [str(o) == str(r) for o in to]
        if any(equals):
            return
        to.append(r)

    for _ in range(4):
        flipped = flip(shape)
        shape = rotate(shape)
        addnew(flipped, ret)
        addnew(shape, ret)
    
    # Ensure first item has a top left #
    if ret[0][0][0] != True:
        for i in range(len(ret)):
            if ret[i][0][0]:
                ret[i], ret[0] = ret[0], ret[i]
                return ret

    return ret

def parse_lines(raw):
    # Groups.
    groups = raw.split("\n\n")

    shapes = []
    for sraw in groups[:-1]:
        shapelines = sraw.split("\n")[1:]
        shape = []
        for sl in shapelines:
            shape.append(list("1" if c == "#" else "0" for c in sl))
        
        shapes.append(shape_perms(shape))
        
    grid_lines = groups[-1].split("\n")
    grids = []
    for gr in grid_lines:
        dim, craw = gr.split(":")
        x, y = dim.split("x")
        cnts = []
        for c in craw.strip().split(" "):
            cnts.append(int(c))
        grids.append((int(x), int(y), cnts))

    return shapes, grids


def slide_across(w, h, shapes):
    ret = []
    for shape in shapes:
        ints = []
        for shapeperm in shape:
            for gy in range(h - len(shapeperm) + 1):
                for gx in range(w - len(shapeperm) + 1):
                    grid = [["0"] * w for _ in range(h)]
                    for y in range(len(shapeperm)):
                        for x in range(len(shapeperm)):
                            grid[gy + y][gx + x] = shapeperm[y][x]
                    gbin = "".join(["".join(g) for g in grid])
                    ints.append((int(gbin, 2), gx, gy))
        ret.append(ints)
    return ret


def solve1(shapes, grid):
    w, h, base_counts = grid
    ret = 0
    slides = slide_across(w, h, shapes)

    shapecounts = [str(s[0]).count("1") for s in shapes]
    bad = int("1" + "0" * (w - 1) + "1" + "0" * (w - 1) + "1" + "0" * (w - 1), 2)
    shapesize = len(shapes[0][0])

    def dfs(grid, counts, used, pgx, pgy):
        if sum(counts) == 0:
            return 1
        needs = [c * counts[i] for i, c in enumerate(shapecounts)]
        needed = sum(needs)
        # hremain = h - pgy - 1
        if w * h < used + needed: # or hremain * w < needed:
            # print(hremain * w)
            return 0
        if used and not bad & grid:
            return 0

        new_counts = list(counts)
        for i, c in enumerate(counts):
            if c == 0:
                continue
            for (cand, gx, gy) in slides[i]:
                if gy == pgy and gx - pgx > 2:
                    continue
                if cand & grid == 0:
                    new_counts[i] -= 1
                    if dfs(cand | grid, new_counts, used + shapecounts[i], gx, gy):
                        return 1
                    new_counts[i] += 1
        
        return 0    

    return dfs(0, base_counts, 0, -100, -100)


def solve(raw):
    shapes, grids = parse_lines(raw)

    ret = 0
    for g in grids:
        here = solve1(shapes, g)
        print(g, here)
        ret += here
    return ret

if __name__ == "__main__":
    SAMPLE, REAL = get_raw_inputs(sys.argv)

    sample = solve(SAMPLE)
    assert sample == SAMPLE_EXPECTED, "Sample Result %s != %s expected" % (sample, SAMPLE_EXPECTED)
    print("\n*** SAMPLE PASSED ***\n")

    solved = solve(REAL)
    print("SOLUTION: ", solved) # 524
