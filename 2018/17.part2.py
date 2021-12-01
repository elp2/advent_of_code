from collections import defaultdict


REAL=open("17.txt").readlines()
SAMPLE=open("17.sample.txt").readlines()

CLAY="#"
SAND="."
SPRING="+"
FALLING_WATER="|"
STANDING_WATER="~"
def return_default():
    return SAND

def xsys(line):
    inputs = line.strip().split(", ")
    a, b = inputs
    if "x" in a:
        flat = "x"
    else:
        flat = "y"
    a = int(a.split("=")[1])
    bs = b.split("=")[1]
    bs = bs.split("..")
    bmin, bmax = int(bs[0]), int(bs[1])
    ret = []
    for b in range(bmin, bmax + 1):
        if flat == "x":
            ret.append((a, b))
        else:
            ret.append((b, a))
    return ret


class World:
    def __init__(self, lines):
        self.board = defaultdict(return_default)
        self.board[(500, 0)] = "+"
        self.maxy = self.maxx = 0
        self.minx = 10000000000
        self.miny = 10000000000
        for line in lines:
            clays = xsys(line)
            for hx, hy in clays:
                self.board[(hx, hy)] = CLAY
                self.maxy = max(self.maxy, hy)
                self.minx = min(self.minx, hx)
                self.miny = min(self.miny, hy)
                self.maxx = max(self.maxx, hx)
        self.minx -= 1
        self.maxx += 1

    def spread(self, x, y):
        print("Spread ", x, y)
        # print("\nSPREAD: ", self.as_string())
        falls = []
        spread_to = []
        for dx in [-1, 1]:
            at = x
            while self.board[(at, y)] != "#":
                under = self.board[(at, y + 1)]
                if under in "~#":
                    spread_to.append((at, y))
                elif under in ".|":
                    falls.append((at, y))
                    break
                at += dx
        spread_type = "~"
        if falls:
            spread_type = "|"
        for st in spread_to:
            self.board[st] = spread_type
        if falls:
            return falls
        else:
            return self.spread(x, y-1)

    def fall(self, x, y):
        print("Fall from ", x, y)
        # print("\nFALL: ", self.as_string())
        while True:
            here = self.board[(x, y)]
            if here == "#":
                return (x, y - 1)
            elif here == "|":
                return None
            elif here == ".":
                if y > self.maxy:
                    return None
                self.board[(x, y)] = "|"
                y += 1
            elif here == "~":
                return (x, y - 1)
            else:
                return None

    def run(self):
        spreads = [self.fall(500, 1)]
        falls = []
        while spreads or falls:
            falls = []
            for s in spreads:
                f = self.spread(s[0], s[1])
                if f:
                    falls = falls + f
            spreads = []
            for f in falls:
                s = self.fall(f[0], f[1])
                if s:
                    spreads.append(s)

    def as_string(self):
        ret = []
        for y in range(self.miny, self.maxy + 1):
            line = ""
            for x in range(self.minx, self.maxx + 1):
                line += self.board[(x, y)]
            ret.append(line)
        return "\n".join(ret)


    def water_count(self):
        waters = 0
        for y in range(self.miny, self.maxy + 1):
            for x in range(self.minx, self.maxx + 1):
                if self.board[(x, y)] in "~":
                    if y == 0:
                        print("WATER AT ", x)
                    waters += 1
        return waters


# CLAY="#"
# SAND="."
# SPRING="+"
# FALLING_WATER="|"
# STANDING_WATER="~"


def parse_lines(lines):
    w = World(lines)
    w.run()
    print(w.as_string())
    return w

def solve(lines):
    w = parse_lines(lines)
    return w.water_count()

sample = solve(SAMPLE)
assert sample == 29
print("*** SAMPLE PASSED ***")

print(solve(REAL)) # 36989 = high
