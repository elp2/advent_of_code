
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
    portals = {}

    for y in range(len(lines)):
        for x in range(len(lines[y])):
            for dir in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                portal = read_portal(lines, x, y, dir[0], dir[1])
                if not portal:
                    continue
                if portal in portals:
                    portal = portal.lower()
                portals[portal] = (x, y)
    return portals

print(find_portals(open('input').readlines()))
