FLOOR = '.'

def read_portal(lines, x, y, xdiff, ydiff):
    """x,y is a potential portal spot."""
    try:
        if lines[y + ydiff][x + xdiff] == ' ':
            return False
        a = lines[y + ydiff][x + xdiff]
        b = lines[y + 2 * ydiff][x + 2 * xdiff]
        name = (a + b).strip()
        if len(name) != 2:
            return False
        if '.' in name:
            return False
        return name
    except:
        return False

def find_portals(lines):
    portal_to_pos = {}
    pos_to_portal = {}

    for y in range(len(lines)):
        for x in range(len(lines[y])):
            for dir in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                portal = read_portal(lines, x, y, dir[0], dir[1])
                if not portal:
                    continue
                if portal in portals:
                    portal = portal.lower()
                portal_to_pos[portal] = (x, y)
                pos_to_portal[(x, y)] = portal

    return [portal_to_pos, pos_to_portal]

def get_around(pos, lines):
    around = []
    for dir in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
        try:
            x = pos[0] + dir[0]
            y = pos[1] + dir[1]
            if lines[y][x] == FLOOR:
                around.append((x, y))
        except:
            continue
    return around

def othercase(string):
    if string.upper() == string:
        return string.lower()
    else:
        return string.upper()

def bfs_lines(lines):
    [portal_to_pos, pos_to_portal] = find_portals(lines)
    visited = [[False] * len(lines[0]) for y in range(len(lines))]

    search = [(portal_to_pos['AA'], 0)]
    while search:
        [pos, steps] = search[0]
        search = search[1:]

        if visited[pos[1]][pos[0]]:
            continue
        visited[pos[1]][pos[0]] = True
        if pos in pos_to_portal:
            portal = pos_to_portal[pos]
            if portal == 'ZZ':
                print('Found: ', steps)
                return
            paired_portal = othercase(portal)
            search.append((portal_to_pos[paired_portal], steps + 1)
        else:
            around = get_around(pos, lines)
            for a in around:
                search.append((a, steps+1))

def part1():
    lines = open('input').readlines()
    bfs_lines(lines)
