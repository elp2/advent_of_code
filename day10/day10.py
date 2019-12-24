from math import atan2
def asteroid_locations(filename):
    asteroids = []
    lines = open(filename).readlines()
    for y in range(0, len(lines)):
        for x in range(0, len(lines[0].strip())):
            if lines[y][x] == '#':
                asteroids.append((x, y))
    return asteroids

asteroids = asteroid_locations('input')


def part1():
    asteroid_visible_angles = {}
    for asteroid in asteroids:
        visible = set()
        for other in asteroids:
            if asteroid == other:
                continue
            xdiff = asteroid[0] - other[0]
            ydiff = asteroid[1] - other[1]
            visible.add(atan2(ydiff, xdiff))
        asteroid_visible_angles[asteroid] = len(visible)
        if len(visible) == 286:
            print(asteroid, '!')

    print(max(asteroid_visible_angles.values())) # 286

# 22, 25

def angle_between(asteroid, other):
    xdiff = other[0] - asteroid[0]
    ydiff =  asteroid[1] - other[1]
    # Rotate by 90 degrees (should be y,x) so sorting is easier.
    angle = atan2(xdiff, ydiff)
    print(other, xdiff, ydiff, angle)
    return [angle, ydiff * ydiff + xdiff + xdiff]

def part2():
    by_angle = {}
    for asteroid in asteroids:
        if (22,25) != asteroid:
            continue
        for other in asteroids:
            if asteroid == other:
                continue
            [angle, distance] = angle_between(asteroid, other)
            if angle not in by_angle:
                by_angle[angle] = []
            by_angle[angle].append([other, distance])

    # sort order:
    # 0-pi
    # -pi -> 0

    keys = by_angle.keys()
    tan_sorted = sorted(keys, key=lambda val: val if val >= 0 else 8 + val)
    # print(tan_sorted)
    num_removed = 0
    # print(tan_sorted)
    while True:
        for angle in tan_sorted:
            if len(by_angle[angle]):
                closest_first = sorted(by_angle[angle], key=lambda d: d[1])
                if len(closest_first) > 1:
                    print(closest_first)
                removed = closest_first[0][0]
                num_removed += 1
                print("Removing #%d: %s (%.3f)" % (num_removed, removed, angle))
                by_angle[angle] = closest_first[1:]
                if num_removed == 200:
                    print('Answer is: %d' % (removed[0] * 100 + removed[1])) # 504
                    return

part2()
