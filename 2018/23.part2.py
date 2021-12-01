import heapq
import re

def subdivide(d1, d2, split):
    dn = max(1, int((d2 - d1) / split))
    n1 = d1
    divs = []
    while True:
        n2 = min(n1 + dn, d2)
        if n1 >= d2 or n1 == n2:
            break
        divs.append((n1, n2))
        n1 = n2
    assert divs
    return divs

print(subdivide(0, 4, 2))
print(subdivide(-4, 4, 2))



class Region:
    def __init__(self, x1, x2, y1, y2, z1, z2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.z1 = z1
        self.z2 = z2
        self.bots = []
        self.manhattan_origin = abs(min((abs(x1), abs(x2)))) + abs(min((abs(y1), abs(y2)))) + abs(min((abs(z1), abs(z2)))) 
    
    def center(self):
        return (
            int((self.x1 + self.x2) / 2),
            int((self.y1 + self.y2) / 2),
            int((self.z1 + self.z2) / 2),
        )

    def unit_cube(self):
        return self.x1 == self.x2 - 1 and self.y1 == self.y2 - 1 and self.z1 == self.z2 - 1

    def num_bots(self):
        return len(self.bots)

    def intersect_with(self, bot):
        def axis_distance(a1, a2, to):
            if to < a1:
                return a1 - to
            elif to > a2:
                return to - a2 + 1
            else:
                # Don't need to move at all on this axis to intersect.
                return 0
        xa = axis_distance(self.x1, self.x2, bot.x)
        ya = axis_distance(self.y1, self.y2, bot.y)
        za = axis_distance(self.z1, self.z2, bot.z)
        assert xa >= 0 and ya >= 0 and za >= 0
        if xa + ya + za <= bot.r:
            self.bots.append(bot)

    def area(self):
        return (self.x2 - self.x1) * (self.y2 - self.y1) * (self.z2 - self.z1)

    def __lt__(self, other):
        # Intentionally flipped since heapq is a min heap.
        return self.num_bots() > other.num_bots()
        # if self.num_bots() > other.num_bots():
        #     return True
        # return self.manhattan_origin < other.manhattan_origin
    def __eq__(self, other):
        return len(self.bots) == len(other.bots) and self.manhattan_origin == other.manhattan_origin

    def __str__(self):
        return " ".join(map(str, ["area:", self.area(), "bots:", self.num_bots(), "(", self.x1, self.x2, self.y1, self.y2, self.z1, self.z2, ")"]))


    def subregions(self):
        """Returns |split| subregions of this region."""
        
        subs = []
        for (x1, x2) in subdivide(self.x1, self.x2, 2):
            for (y1, y2) in subdivide(self.y1, self.y2, 2):
                for (z1, z2) in subdivide(self.z1, self.z2, 2):
                    # print((x1, x2, y1, y2, z1, z2))
                    subregion = Region(x1, x2, y1, y2, z1, z2)
                    for b in self.bots:
                        subregion.intersect_with(b)
                    
                    subs.append(subregion)

        assert len(subs) == 8
        return subs


class Bot:
    def __init__(self, line):
        self.x, self.y, self.z, self.r = map(int, re.findall("\d+", line))


    def contains_point(self, point):
        px, py, pz = point
        return abs(px - self.x) + abs(py - self.y) + abs(pz - self.z) <= self.r


def parse_lines(raw):
    lines = raw.split("\n")
    bots = list(map(Bot, lines))
    return bots


def solve(raw):
    bots = parse_lines(raw)

    x1 = min(map(lambda b: b.x - b.r, bots))
    y1 = min(map(lambda b: b.y - b.r, bots))
    z1 = min(map(lambda b: b.z - b.r, bots))

    x2 = max(map(lambda b: b.x + b.r, bots))
    y2 = max(map(lambda b: b.y + b.r, bots))
    z2 = max(map(lambda b: b.z + b.r, bots))

    mdim = max([abs(x1), abs(x2), abs(y1), abs(y2), abs(z1), abs(z2)])
    ptwo = 1
    while ptwo < mdim:
        ptwo *= 2



    start = Region(-ptwo, ptwo, -ptwo, ptwo, -ptwo, ptwo)
    for bot in bots:
        start.intersect_with(bot)

    regions = [start]

    best_bots = 0
    best_distance = 0

    while True:
        if not regions:
            return best_distance
        
        region = heapq.heappop(regions)
        print(region)
        if region.num_bots() < best_bots:
            # Recursing into worse territory.
            return best_distance

        if region.unit_cube():
            bdist = None
            bbots = None
            for x in range(region.x1-2, region.x2 + 1):
                for y in range(region.y1-2, region.y2 + 1):
                    for z in range(region.z1-2, region.z2 + 1):
                        herebots = 0
                        for b in bots:
                            if b.contains_point((x, y, z)):
                                herebots += 1
                        dist = abs(x) + abs(y) + abs(z)
                        if not bbots or herebots > bbots:
                            bdist = dist
                            bbots = herebots
                        elif herebots == bbots and dist < bdist:
                            bdist = dist
            print("BEST DIST: ", bdist, bbots)
            
            if best_bots < bbots:
                best_bots = bbots
                best_distance = bdist
            elif best_bots == bbots and best_distance > bdist:
                best_distance = bdist
        
        else:
            for subregion in region.subregions():
                if subregion.num_bots() >= best_bots:
                    heapq.heappush(regions, subregion)


sample = solve(open("23.sample").read())
assert sample == 36

ansmin = 34079730
ansmax = 105191924

real = solve(open("23.txt").read())
assert (real > ansmin and real < ansmax)
print("REAL: ", real)
# BEST DIST:  105191924 492
# REAL:  105191924 <- too high

# BEST DIST:  34079728 33 # too low
# REAL:  34079728

# too low
# area: 35184372088832 bots: 30 ( 4685824 4718592 11206656 11239424 -17104896 -17072128 )
# REAL:  34079730

# 105191907 JUUUUST RIGHT!