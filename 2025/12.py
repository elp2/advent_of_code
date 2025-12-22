from collections import defaultdict, deque, Counter
from itertools import combinations, combinations_with_replacement, permutations, product
from functools import reduce, cmp_to_key, lru_cache
from operator import add, mul, itemgetter, attrgetter
import os
import sys
import cProfile

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
                r[x][len(s)-1-y] = s[y][x]
        return r
        
    def flip(s):
        r = [[0] * len(s) for _ in range(len(s))]
        for y in range(len(s)):
            for x in range(len(s)):
                r[y][x] = s[y][len(s) - x - 1]
        return r

    def addnew(r, to):
        if r in to:
            return
        to.append(r)

    def binify(sha):
        return [int("".join(sh), 2) for sh in sha]

    for _ in range(4):
        flipped = flip(shape)
        shape = rotate(shape)
        addnew(flipped, ret)
        addnew(shape, ret)
    
    # # Ensure first item has a top left #
    # if ret[0][0][0] != True:
    #     for i in range(len(ret)):
    #         if ret[i][0][0]:
    #             ret[i], ret[0] = ret[0], ret[i]
    #             return ret

    return ret

def parse_lines(raw):
    # Groups.
    groups = raw.split("\n\n")

    shapes = []
    for sraw in groups[:-1]:
        shapelines = sraw.split("\n")[1:]
        shape = []
        for sl in shapelines:
            shape.append([c == "#" for c in sl])
        
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
    shapedim = len(shapes[0][0])
    ret = []
    for shape in shapes:
        # print("---------", shape)
        ints = []
        for shapeperm in shape:
            for gx in range(w - len(shapeperm) + 1):
                for gy in range(h - len(shapeperm) + 1):
                    grid = 0
                    for y in range(shapedim):
                        for x in range(shapedim):
                            if shapeperm[y][x]:
                                bit = 1 << (gx + x + (gy + y) * w)
                                grid |= bit
                    if False:
                        gbin = bin(grid)[2:]
                        gbin = "0" * ((w * h) - len(gbin)) + gbin
                        for py in range(h):
                            print(gbin[py * w:(py + 1) * w])
                        print("-------")
                    ints.append((grid, gx, gy))
        ret.append(ints)
    return ret


def solve1(shapes, grid):
    w, h, base_counts = grid
    ret = 0
    slides = slide_across(w, h, shapes)

    shapecounts = [str(s[0]).count("T") for s in shapes]
    shapesize = len(shapes[0][0])

    @lru_cache(maxsize=None)
    def dfs(grid, counts):
        if sum(counts) == 0:
            return 1
        needs = [c * counts[i] for i, c in enumerate(shapecounts)]
        needed = sum(needs)
        used = grid.bit_count()
        if w * h < used + needed:
            return 0

        best_fits = None
        best_i = None

        for i, c in enumerate(counts):
            if c == 0:
                continue
            fits = []
            for (cand, _, _) in slides[i]:
                if cand & grid == 0:
                    fits.append(cand)
                    if best_fits is not None and len(best_fits) < len(fits):
                        break
            
            if best_fits is None or len(fits) < len(best_fits):
                best_fits = fits
                best_i = i

        if best_fits is None:
            return 0
        
        new_counts = list(counts)
        new_counts[best_i] -= 1
        new_counts = tuple(new_counts)
        for cand in best_fits:
            if dfs(cand | grid, new_counts):
                return 1
        
        return 0    

    return dfs(0, tuple(base_counts))


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
