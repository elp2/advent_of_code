from collections import deque
import copy

CHALLENGE_DAY = "20"
REAL = open(CHALLENGE_DAY + ".txt").read()
SAMPLE = open(CHALLENGE_DAY + ".sample.txt").read()

def edge_right(grid):
    ret = []
    for y in range(len(grid)):
        ret.append(grid[y][-1])
    return "".join(ret)

def edge_left(grid):
    ret = []
    for y in range(len(grid)):
        ret.append(grid[y][0])
    return "".join(ret)

def edge_top(grid):
    return "".join(grid[0])

def edge_bottom(grid):
    return "".join(grid[-1])

EDGE_FNS = [ edge_bottom, edge_left, edge_right, edge_top ]

def flip_x(grid):
    return list(map(lambda r: r[::-1], grid))

print(flip_x([[1,2], [3, 4]]))

def flip_y(grid):
    ret = copy.deepcopy(grid)
    ret.reverse()
    return ret

print(flip_y([[1,2], [3, 4]]))
print(flip_y(flip_x([[1,2], [3, 4]])))

def rotate_right(grid):
    ret = []
    for x in range(len(grid[0])):
        row = []
        for y in range(len(grid) - 1, -1, -1):
            row.append(grid[y][x])
        ret.append(row)
    return ret

def grid_possibilities(grid):
    poss = []

    grid = copy.deepcopy(grid)

    for i in range(4):
        rotated = rotate_right(grid)
        poss.append(copy.deepcopy(grid))
        poss.append(flip_x(grid))
        poss.append(flip_y(grid))
        poss.append(flip_x(flip_y(grid)))

        grid = rotated
    return poss

class Tile:
    def __init__(self, txt):
        txt = txt.strip()
        lines = txt.split("\n")
        self.id = int(lines[0].split(" ")[1].replace(":", ""))
        self.image = list(map(list, lines[1:]))

        self.edges = set([edge_fn(self.image) for edge_fn in EDGE_FNS])
        self.reversed_edges = set([edge_fn(self.image)[::-1] for edge_fn in EDGE_FNS])
        self.adjacents = []
        self.pos = None # set to (x, y) when this is placed in grid
    
    def removed_edges(self):
        ret = []
        for row in self.image[1:-1]:
            ret.append(row[1:-1])
        return ret

def parse_lines(raw):
    # Groups.
    raw_tiles = raw.split("\n\n")

    tiles = [Tile(rt) for rt in raw_tiles]
    return dict([[t.id, t] for t in tiles])

def find_adjacents(tiles):
    for tnum, tile in tiles.items():
        for onum, otile in tiles.items():
            if onum == tnum:
                continue
            if tile.edges & otile.edges or tile.reversed_edges & otile.edges:
                tile.adjacents.append(onum)

def position_tiles(tiles):
    grid = {}
    q = deque()

    grid[(0, 0)] = tiles[list(tiles.keys())[0]]
    q.append((0, 0))

    while q:
        pos = q.popleft()
        tile = grid[pos]
        print("Considering ", tile.id, " at ", pos)
        tile.pos = pos
        x, y = pos
        for adj_num in tile.adjacents:
            adj = tiles[adj_num]
            if adj in grid.values():
                continue
            potentials = [
                [(x, y - 1), edge_top(tile.image), edge_bottom],
                [(x + 1, y), edge_right(tile.image), edge_left],
                [(x, y + 1), edge_bottom(tile.image), edge_top],
                [(x - 1, y), edge_left(tile.image), edge_right],
            ]

            for ppos, match_edge, match_fn in potentials:
                if ppos in grid:
                    continue
                for adj_poss in grid_possibilities(adj.image):
                    if match_fn(adj_poss) == match_edge:
                        adj.image = adj_poss
                        grid[ppos] = adj
                        q.append(ppos)
                        break

    assert len(grid) == len(tiles)
    return grid

def gridify(positioned):
    xes = []
    yes = []
    for x, y in positioned.keys():
        xes.append(x)
        yes.append(y)
    
    grid = []
    for y in range(min(yes), max(yes) + 1):
        row = []
        for x in range(min(xes), max(xes) + 1):
            if (x, y) in positioned:
                row.append(positioned[(x, y)])
            else:
                row.append("????")
        grid.append(row)
    return grid

def print_grid(grid, separator=" "):
    for r in grid:
        print(separator.join(map(lambda t: str(t.id) if type(t) == Tile else t, r)))

def part1(raw):
    tiles = parse_lines(raw)
    find_adjacents(tiles)
    positioned = position_tiles(tiles)
    grid = gridify(positioned)
    print_grid(grid)

    h = len(grid)
    w = len(grid[0])
    return grid[0][0].id * grid[w-1][0].id * grid[0][h - 1].id * grid[w - 1][h - 1].id


p1s = part1(SAMPLE)
assert p1s == 20899048083289

p1 = part1(REAL)
assert p1 == 7492183537913


def stitch_grid(grid):
    stitched = []
    for grid_row in grid:
        removed_edges = list(map(lambda t: t.removed_edges(), grid_row))
        for y in range(len(removed_edges[0])):
            srow = []
            for re in removed_edges:
                srow += re[y]
            stitched.append(srow)
    return stitched


MONSTER_STRING="""                  # 
#    ##    ##    ###
 #  #  #  #  #  #   """
MONSTER = list(map(list, MONSTER_STRING.split("\n")))

def mark_monsters(img):
    def monster_positions(monster, dx, dy):
        pos = []
        for y, row in enumerate(monster):
            for x, c in enumerate(row):
                if c == "#":
                    pos.append((x + dx, y + dy))
        
        return pos

    for _, monster in enumerate(grid_possibilities(MONSTER)):
        for y in range(0, len(img)):
            for x in range(0, len(img[y])):
                body_parts = 0
                mps = monster_positions(monster, x, y)
                for (mx, my) in mps:
                    if 0 <= my < len(img) and 0 <= mx < len(img[y]) and img[my][mx] == "#":
                        body_parts += 1
                if body_parts == MONSTER_STRING.count("#"):
                    print("FOUND MONSTER!", x, y)
                    for (mx, my) in mps:
                        img[my][mx] = "O"
    
    return img


def part2(raw):
    tiles = parse_lines(raw)
    find_adjacents(tiles)
    positioned = position_tiles(tiles)
    grid = gridify(positioned)
    print_grid(grid)

    stitched = stitch_grid(grid)
    stitched = flip_y(stitched) # so sample looks the same.
    print_grid(stitched, "")

    marked = mark_monsters(stitched)
    print_grid(marked, "")

    ret = 0
    for r in marked:
        ret += r.count("#")
    return ret

assert part2(SAMPLE) == 273

print("PART2: ", part2(REAL))
