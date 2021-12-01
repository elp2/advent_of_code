from collections import defaultdict

def return_default():
    return 0

REAL=open("25.txt").readlines()
SAMPLE=open("25.sample").readlines()

class Point:
    def __init__(self, line):
        self.x, self.y, self.z, self.w = map(int, line.strip().split(","))

    def constellation_with(self, o):
        return abs(self.x - o.x) + abs(self.y - o.y) + abs(self.z - o.z) + abs(self.w - o.w) <= 3

def parse_lines(lines):
    return list(map(lambda l: Point(l), lines))


def group_points(points):
    def can_join_constellations(a, b):
        if not a or not b:
            return False
        for sa in a:
            for sb in b:
                if sa.constellation_with(sb):
                    return True
        return False
    
    groups = []
    for p in points:
        joined = False
        for g in groups:
            if can_join_constellations([p], g):
                joined = True
                g.append(p)
        if not joined:
            groups.append([p])
            
    
    while True:
        for i in range(len(groups) - 1):
            ig = groups[i]
            for j in range(i + 1, len(groups)):
                jg = groups[j]
                if can_join_constellations(ig, jg):
                    ig += jg
                    jg.clear()
        if not [] in groups:
            break
        groups = [g for g in groups if g]
        print(len(groups))
    
    return groups






def solve(lines):
    parsed = parse_lines(lines)

    return len(group_points(parsed))

sample = solve(SAMPLE)
assert sample == 2
print("*** SAMPLE PASSED ***")

print(solve(REAL))
