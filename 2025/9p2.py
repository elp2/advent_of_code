from collections import defaultdict, deque, Counter
from itertools import combinations, combinations_with_replacement, permutations, product
from functools import reduce, cmp_to_key
from operator import add, mul, itemgetter, attrgetter
import os
import sys
import multiprocessing as mp

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, root_dir)
from aoc_elp import *

######################
SAMPLE_EXPECTED = 24
######################
assert SAMPLE_EXPECTED != None, "Must enter sample value"

def parse_group(group):
    lines = group.split("\n")
    ret = []
    for y, line in enumerate(lines):
        line = line.strip()
        assert len(line) != 0

        split = line.split(",")

        assert len(split) != 0
        ret.append((int(split[0]), int(split[1])))

    return ret


def parse_lines(raw):
    # Groups.
    # groups = raw.split("\n\n")
    # Do something with the groups.

    return parse_group(raw)

def get_lines(points):
    h = defaultdict(lambda: [])
    v = defaultdict(lambda: [])
    prev = points[0]
    points.append(prev)
    for to in points[1:]:
        px, py = prev
        tx, ty = to
        if px == tx:
            v[px].append((min(py, ty), max(py, ty)))
        elif py == ty:
            h[py].append((min(px, tx), max(px, tx)))
        else:
            assert px == tx or py == ty
        prev = to
    
    for k, l in h.items():
        h[k] = sorted(l)
    for k, l in v.items():
        v[k] = sorted(l)
    
    return h, v

def inbox(h, v, tx, ty):
    def inline(hv, axis, num):
        if axis not in hv:
            return False
        a, b = hv[axis][0]
        return a <= num <= b
        
    # along a line
    if inline(h, ty, tx):
        return True

    # Ends in a line
    if inline(v, tx, ty):
        return True

    # If odd number, it's in, even it's out.
    crosses = 0
    for x in range(tx + 1):
        print(x, inline(v, x, ty))
        if inline(v, x, ty):
            crosses += 1
    
    return crosses % 2 == 1

def inline(minx, maxx, y, h, v):
    if y in h:
        ah, bh = h[y][0]
    else:
        ah, bh = -1, -1
    wasonline = False
    online = False
    crosses = 0
    inside = False
    for x in range(0, maxx + 1):
        if x in v:
            av, bv = v[x][0]
            if av <= y <= bv:
                online = True
        elif ah <= x <= bh:
            online = True
        
        if online != wasonline:
            inside = not inside
        
        if x >= minx and not inside:
            return False
        wasonline = online
    
    return True

def filterout(goods, bads, stepsize, h, v):
    considered = 0
    newgoods = []
    for ((minx, miny), (maxx, maxy)) in goods:
        considered += 1
        if considered % 100 == 0:
            print(len(newgoods), len(goods), len(bads))

        wasbad = False
        for i, b in enumerate(bads):
            (bxa, bya), (bxb, byb) = b
            if minx <= bxa <= maxx and minx <= bxb <= maxx and miny <= bya <= maxy and miny <= byb <= maxy:
                bads[i] = ((minx, miny), (maxx, maxy))
                wasbad = True
                break
        if wasbad:
            continue

        valid = True

        quickstep = (maxy - miny) // stepsize
        if quickstep:
            for y in range(miny, maxy + 1, quickstep):
                if not inline(minx, maxx, y, h, v):
                    valid = False
                    break
        # if valid:
        #     print("qs pass")
        # for y in range(miny, maxy + 1):
        #     if not inline(minx, maxx, y, h, v):
        #         valid = False
        #         break
        if valid:
            newgoods.append(((minx, miny), (maxx, maxy)))
        else:
            print("Bad!!!")
            bads.append(((minx, miny), (maxx, maxy)))
    return newgoods

def hvfor(minx, miny, maxx, maxy, h, v):
    nv = {}
    for vx, [(ay, by)] in v.items():
        if vx <= minx or vx >= maxx:
            continue
        if ay <= miny <= by or ay <= maxy <= by or miny <= ay <= maxy or miny <= by <= maxy:
            proposed = (max(ay, miny), min(maxy, by))
            if proposed != (miny, miny) and proposed != (maxy, maxy):
                nv[vx] = proposed
                # print(minx, vx, maxx, (ay, by))
    
    nh = {}
    for vy, [(ax, bx)] in h.items():
        if vy <= miny or vy >= maxy:
            continue
        if ax <= minx <= bx or ax <= maxx <= bx or minx <= ax <= maxx or minx <= bx <= maxx:
            proposed = (max(ax, minx), min(maxx, bx))
            if proposed != (minx, minx) and proposed != (maxx, maxx):
                nh[vy] = proposed
    for x in nv.keys():
        assert minx <= x <= maxx

    for y in nh.keys():
        assert miny <= y <= maxy

    return nh, nv

def solveab(ret, ax, ay, bx, by, h, v):
    # ax, ay = (2, 3)
    # bx, by = (9, 7)
    minx = min(ax, bx)
    maxx = max(ax, bx)
    miny = min(ay, by)
    maxy = max(ay, by)

    potential = (abs(minx - maxx) + 1) * (abs(miny - maxy) + 1)
    print("INVESTIGATING: ", potential, (ax, ay), (bx, by))
    if potential == 24:
        print("!!!!24!!!!", [(minx, miny), (maxx, miny), (minx, maxy), (maxx, maxy)])
    # if potential >= 2326670509:
    #     continue
    if ret >= potential:
        return 0


    nh, nv = hvfor(minx, miny, maxx, maxy, h, v)
    if len(nh) == 0 and len(nv) == 0:
        print(potential, " 00000")
    if potential == 24:
        print((minx, miny), (maxx, maxy), "24: ", "\nnv: ", nv, "\nnh: ", nh)
    if potential == 40:
        print((minx, miny), (maxx, maxy), "40: ", "\nnv: ", nv, "\nnh: ", nh)

    bad = False
    for x, yrange in nv.items():
        # if x + 1 in nv:
        #     print((minx, miny), (maxx, maxy), x, x + 1, "nvnext", nv[x], nv[x + 1], potential)
        # assert x+1 not in nv
        # print("x", x, yrange)
        if bad:
            break
        if x == minx or x == maxx:
            continue
        ay, by = yrange
        if by > miny or ay < maxy:
        # if miny + 1 <= ay < maxy or miny + 1 <= by < maxy:
            # print(badcount)
            bad = True
            break

    for y, xrange in nh.items():
        if y+1 in nh:
            print("nhnext", nh[y], nh[y + 1], potential)
        # print("Y:", y, xrange)
        if bad:
            break
        if y == miny or y == maxy:
            continue
        ax, bx = xrange
        if bx > minx or ax < maxx:
            # print(badcount)
            bad = True
            break

    if bad:
        return 0
    else:
        topbot = [inline(minx, maxx, miny, h, v), inline(minx, maxx, maxy, h, v)]
        # corners = [inbox(h, v, tx, ty) for (tx, ty) in [(minx, miny), (maxx, miny), (minx, maxy), (maxx, maxy)]]
        if all(topbot):
            print("PASS TOPBOT: ", potential, [(minx, miny), (maxx, miny), (minx, maxy), (maxx, maxy)])
            ret = potential
            return potential
        else:
            if potential == 24:
                print("?")
            print(potential, "failed corner check!!")
            return 0
        # print("GOOD: ", (minx, miny), (maxx, maxy), potential, "\nnv: ", nv, "\nnh: ", nh)
        # print("GOOD: ", ret, )
            # print("bad")
    # if len(nh) <= 2:
    #     print(potential, len(nh), len(nv))

def solve(raw):
    parsed = parse_lines(raw)
    h, v = get_lines(parsed)

    # assert inline(2, 9, 3, h, v)
    # assert inline(2, 9, 5, h, v)
    # assert inbox(h,v,9,3)
    # assert inbox(h,v,2,3)
    # assert inbox(h,v,2,5)
    # assert inbox(h,v,9,5)


    inrange = 0
    ret = 0
    linelens = 0

    bads = []
    goods = []
    badcount =0 
    # print(parsed)
    for i, (ax, ay) in enumerate(parsed):
        for (bx, by) in parsed[i + 1:]:
            ret = max(ret, solveab(ret, ax, ay, bx, by, h, v))
    

    return ret

if __name__ == "__main__":
    SAMPLE, REAL = get_raw_inputs(sys.argv)

    sample = solve(SAMPLE)
    assert sample == SAMPLE_EXPECTED, "Sample Result %s != %s expected" % (sample, SAMPLE_EXPECTED)
    print("\n*** SAMPLE PASSED ***\n")

    solved = solve(REAL)
    print("SOLUTION: ", solved)
    assert solved > 66055515
    assert solved < 2326670509
    assert solved != 1605595152
    


# for k in range(max(v.keys())):
#     if k in v and k + 1 in v:
#         print(v[k], v[k+1])
# [(53339, 54524)] [(40118, 41220)]
# for k in range(max(h.keys())):
#     if k in h and k + 1 in h:
#         print(h[k], h[k+1])
# Nothing, probably don't need to account for cases where it's next to each other