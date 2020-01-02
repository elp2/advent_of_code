FLOOR = '.'

def read_portal(lines, x, y):
    """x,y is a potential portal spot."""
    for (a,b) in [[(-2, 0), (-1, 0)], [(1,0), (2,0)], [(0, -2), (0, -1)], [(0, 1), (0, 2)]]:
        try:
            if lines[y][x] != '.':
                return False
            ac = lines[y + a[1]][x + a[0]]
            bc = lines[y + b[1]][x + b[0]]

            name = (ac + bc).strip()
            if len(name) != 2:
                continue
            if '.' in name or '#' in name:
                continue
            return name
        except:
            continue
    return False

def find_portals(lines):
    portal_to_pos = {}
    pos_to_portal = {}

    for y in range(len(lines)):
        for x in range(len(lines[y])):
            portal = read_portal(lines, x, y)
            if not portal:
                continue
            if portal in portal_to_pos:
                portal = portal.lower()
            portal_to_pos[portal] = (x, y)
            pos_to_portal[(x, y)] = portal

    return [portal_to_pos, pos_to_portal]

def paired_portal(portal, portal_to_pos):
    if othercase(portal) in portal_to_pos:
        return portal_to_pos[othercase(portal)]
    return False

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
    lines = split_lines(lines)
    [portal_to_pos, pos_to_portal] = find_portals(lines)
    print(portal_to_pos)
    print(portal_to_pos['AA'], '->', portal_to_pos['ZZ'])
    print(othercase('AA'), othercase('aa'))
    visited = [[0] * len(lines[0]) for y in range(len(lines))]

    search = [(portal_to_pos['AA'], 0)]
    while search:
        [pos, steps] = search[0]
        search = search[1:]

        if visited[pos[1]][pos[0]]:
            continue
        visited[pos[1]][pos[0]] = steps + 1

        if pos in pos_to_portal:
            portal = pos_to_portal[pos]
            if portal == 'ZZ':
                print('Found: ', steps)
                # return
            pair = paired_portal(portal, portal_to_pos)
            if pair:
                print('Pair: %s -> %s' % (portal, pair))
                search.append((pair, steps + 1))
            else:
                print('NO PAIR FOR %s' % (portal))
        around = get_around(pos, lines)
        for a in around:
            search.append((a, steps + 1))

    for y in range(len(lines)):
        for x in range(len(lines[y])):
            if visited[y][x]:
                lines[y][x] = str(visited[y][x] % 10)
    for y in range(len(lines)):
        print(''.join(lines[y]).rstrip())

def split_lines(lines):
    board = []
    for y in range(len(lines)):
        line = []
        for x in range(len(lines[y])):
            line.append(lines[y][x])
        board.append(line)
    return board

def part1():
    lines = open('input').readlines()
    bfs_lines(lines)

part1()