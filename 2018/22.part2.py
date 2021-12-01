from collections import defaultdict

def return_default():
    return 0


import sys
print(sys.getrecursionlimit())
sys.setrecursionlimit(2000)


def geologic_index(gis, x, y, depth):
    key = (x, y)
    if key in gis:
        return gis[key]
    val = erosion_level(gis, x - 1, y, depth) * erosion_level(gis, x, y - 1, depth)
    gis[key] = val
    # print("Set: ", key, " = ", val)
    return val


def erosion_level(gis, x, y, depth):
    key = ("e", x, y)
    if key in gis:
        return gis[key]
    level = (geologic_index(gis, x, y, depth) + depth) % 20183
    gis[key] = level
    return level % 3



def default_gis(tx, ty):
    gis = {}
    gis[(0, 0)] = 0
    for x in range(tx + 1 + TARGET_DELTA):
        gis[(x, 0)] = x * 16807
    for y in range(ty + 1 + TARGET_DELTA):
        gis[(0, y)] = y * 48271
    gis[(tx, ty)] = 0
    return gis


GEAR = 0
TORCH = 1
NEITHER = 2
REQUIRED = [[GEAR, TORCH], [GEAR, NEITHER], [TORCH, NEITHER]]

TARGET_DELTA = 200

def traverse(x, y, holding, minutes, fastest, els, target):
    key = (x, y, holding)
    if key in fastest and fastest[key] <= minutes:
        return
    fastest[key] = minutes
    
    allowed_gear = REQUIRED[els[(x, y)]]

    moves = []
    for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
        nx = x + dx
        ny = y + dy
        if 0 <= ny <= target[1] + TARGET_DELTA:
            if 0 <= nx <= target[0] + TARGET_DELTA:
                el = els[(nx, ny)]
                for gear in REQUIRED[el]:
                    move_time = 1
                    if gear in allowed_gear:
                        if gear != holding:
                            move_time = 8
                        traverse(nx, ny, gear, minutes + move_time, fastest, els, target)


from collections import deque
def iterative_traverse(fastest, start_holding, els, target):
    q = deque()
    q.append((0, 0, 0, start_holding))
    while q:
        if len(fastest) % 1000 == 0:
            print(len(fastest), len(q))
        t, x, y, holding = q.popleft()

        key = (x, y, holding)
        if key in fastest and fastest[key] <= t:
            continue
        fastest[key] = t
        
        allowed_gear = REQUIRED[els[(x, y)]]
        for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            nx = x + dx
            ny = y + dy
            if 0 <= ny <= target[1] + TARGET_DELTA:
                if 0 <= nx <= target[0] + TARGET_DELTA:
                    el = els[(nx, ny)]
                    for gear in REQUIRED[el]:
                        move_time = 1
                        if gear in allowed_gear:
                            if gear != holding:
                                move_time = 8
                            q.append((t + move_time, nx, ny, gear))


def solve(depth, tx, ty):
    ret = 0

    els = {}
    gis = default_gis(tx, ty)
    for y in range(ty + 1 + TARGET_DELTA):
        for x in range(tx + 1 + TARGET_DELTA):
            el = erosion_level(gis, x, y, depth)
            els[(x, y)] = el
    assert els[(tx, ty)] == 0

    fastest = {}
    iterative_traverse(fastest, TORCH, els, (tx, ty))
    # traverse(0, 0, TORCH, 0, fastest, els, (tx, ty))

    mins = []
    print("DONE!")
    for item in [GEAR, TORCH]:
        key = (tx, ty, item)
        fto = fastest[key]
        if item != TORCH:
            fto += 7
        mins.append(fto)
    print(mins)
    return min(mins)

# sample = solve(510, 10, 10)
# assert sample == 45
# print("*** SAMPLE PASSED ***")


print(solve(8103, 9, 758)) # 1045, 1030 too high