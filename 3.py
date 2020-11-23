CACHE = {}
def bottom_right_index(x):
    if x in CACHE:
        return CACHE[x]
    if x <= 0:
        return 1
    diameter = 2 * x + 1
    return diameter * 2 + (diameter - 2) * 2 + bottom_right_index(x - 1)

for br in [0,1,2]:
    print(bottom_right_index(br))

print('-----')

def manhattan_distance_for(num):
    br = 1
    while True:
        if bottom_right_index(br) >= num:
            break
        else:
            br += 1
    here = bottom_right_index(br)
    x = br
    y = -br

    corners = [(-br, -br), (-br, br), (br, br), (br, -br)]
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    
    while True:
        if here == num:
            print(x, y)
            return abs(x) + abs(y)
        if (x, y) == corners[0]:
            print("c ", x, y)
            corners = corners[1:]
            dirs = dirs[1:]
        dx, dy = dirs[0]
        x += dx
        y += dy
        here -= 1




    assert(False)

# assert 3 == manhattan_distance_for(12)
# assert 2 == manhattan_distance_for(23)

# print(manhattan_distance_for(265149)) # 438

SPIRAL = {}

def spiral_larger(num):
    def sum_around(x, y):
        around = 0
        for dx in range(-1, 2, 1):
            for dy in range(-1, 2, 1):
                key = (x + dx, y + dy)
                if key in SPIRAL:
                    around += SPIRAL[key]
        return around
    
    def fill(x, y):
        here = sum_around(x, y)
        print(x, y, here)
        SPIRAL[(x, y)] = here
        return here
    
    SPIRAL[(0, 0)] = 1
    dim = 1
    x, y = (1, 0)
    while True:
        corners = [(dim, dim), (-dim, dim), (-dim, -dim), (dim, -dim)]
        dirs = [(0, 1), (-1, 0), (0, -1), (1, 0)]

        while True:
          if (x, y) in corners:
              corners = corners[1:]
              dirs = dirs[1:]

          here = fill(x, y)
          if here > num:
              print("HERE > NUM!", here)
              return 0
          if len(corners) == 0:
              dim += 1
              x += 1
              break
          else:
              dx, dy = dirs[0]
              x += dx
              y += dy

spiral_larger(265149) # 266330
