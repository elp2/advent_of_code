from collections import defaultdict

def return_default():
    return 0

REAL=open("13.txt").readlines()
SAMPLE=open("13.sample2").readlines()

def parse_lines(lines):
    return list(map(list, lines))

CARTS = "^>v<"
DIRS = [(0, -1), (1, 0), (0, 1), (-1, 0)]



def cart_positions(start, facing, board):
    poses = []
    pos = start
    corners = 0
    fidx = DIRS.index(facing)

    while True:
        poses.append(pos)
        x, y = pos
        here = board[y][x]
        delta = 0
        if here == "\\":
            delta = [-1, 1, -1, 1][fidx]
        elif here == "/":
            delta = [1, -1, 1, -1][fidx]
        elif here == "+":
            cmod = corners % 3
            if cmod == 0:
                delta = -1
            elif cmod == 1:
                delta = 0
            elif cmod == 2:
                delta = 1
            corners += 1
        else:
            assert here in CARTS or here in "|-+"

        fidx = (fidx + len(DIRS) + delta) % len(DIRS)
        facing = DIRS[fidx]

        dx, dy = facing
        x += dx
        y += dy
        pos = (x, y)
        if pos == start:
            break
    return poses

def solve(lines):
    carts = []
    parsed = parse_lines(lines)

    ats = {}

    for y in range(len(lines)):
        for x in range(len(lines[y])):
            here = parsed[y][x]
            if here in CARTS:
                facing = DIRS[CARTS.index(here)]
                pos = (x, y)
                carts.append(cart_positions(pos, facing, parsed))
                ats[pos] = len(carts) - 1
    t = 0
    dead_carts = set()
    while True:
        moved = set()
        for y in range(len(parsed)):
            for x in range(len(parsed[y])):
                pos = (x, y)
                if pos not in ats:
                    continue
                cidx = ats[pos]
                if cidx in moved:
                    continue
                moved.add(cidx)
                cart = carts[cidx]
                cart_next = cart[(t + 1) % len(cart)]
                if cart_next in ats:
                    dead_carts.add(cidx)
                    dead2 = ats[cart_next]
                    dead_carts.add(dead2)
                    print("Crash at ", cart_next, " from ", pos, cidx, dead2)
                    del ats[cart_next]
                    del ats[pos]
                    if len(ats) == 1:
                        at = list(ats.keys())[0]
                        print("EARLY: " + str(at[0]) + "," + str(at[1]))
                else:
                    ats[cart_next] = cidx
                    del ats[pos]
        # assert len(ats) + len(dead_carts) == len(carts)
        # assert len(set(ats.keys()).intersection(dead_carts)) == 0
        if len(ats) == 1:
            at = list(ats.keys())[0]
            return str(at[0]) + "," + str(at[1])
        t += 1


sample = solve(SAMPLE)
assert sample == "6,4"
print("*** SAMPLE PASSED ***")

print(solve(REAL)) # not 93,59
