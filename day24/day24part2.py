from copy import deepcopy

BUG = '#'
EMPTY = '.'
LOWER_LEVEL = '?'

def parse_board(lines):
    board = []
    for line in lines:
        row = []
        for char in line.strip():
            row.append(char)
        board.append(row)
    board[2][2] = LOWER_LEVEL
    return board

def empty_board():
    board = []
    for y in range(0, 5):
        board.append([EMPTY] * 5)
    board[2][2] = LOWER_LEVEL
    return board

def print_levels(levels, depth):
    return
    for b in levels:
        print('Depth %d:' % (depth))
        depth += 1
        for y in range(0, 5):
            print(''.join(b[y]))

def adjacent_lower_level(fromx, fromy):
    if fromx == 2:
        y = 0 if fromy == 1 else 4
        return list(map(lambda x: [x, y, -1], range(0, 5)))
    elif fromy == 2:
        x = 0 if fromx == 1 else 4
        return list(map(lambda y: [x, y, -1], range(0, 5)))
    assert False

def adjacent_map():
    ret = []
    for y in range(0, 5):
        ret.append([])
        for x in range(0, 5):
            adj = []
            for dir in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx = x + dir[0]
                ny = y + dir[1]
                if nx == 2 and ny == 2:
                    adj += adjacent_lower_level(x, y)
                elif nx >= 0 and nx < 5 and ny >= 0 and ny < 5:
                    adj.append([nx, ny, 0])
                elif nx >=5:
                    adj.append([3, 2, 1])
                elif nx < 0:
                    adj.append([1, 2, 1])
                elif ny >= 5:
                    adj.append([2, 3, 1])
                elif ny < 0:
                    adj.append([2, 1, 1])
            ret[-1].append(adj)
    return ret

ADJACENT_MAP = adjacent_map()

for arow in ADJACENT_MAP:
    for aa in arow:
        print(aa)
    
    print('')

def bugs_around(x, y, z, levels):
    around = 0
    for (ax, ay, az_delta) in ADJACENT_MAP[y][x]:
        if levels[az_delta + z][ay][ax] == BUG:
            around += 1
    return around

def evolve(levels):
    new = deepcopy(levels)
    assert bugs_on_board(levels[0]) == 0
    assert bugs_on_board(levels[-1]) == 0
    # Top and bottom-most levels are kept empty so we don't have to worry about z boundary checking.
    for z in range(1, len(levels) - 1):
        for y in range(0, 5):
            for x in range(0, 5):
                current = levels[z][y][x]
                if current == LOWER_LEVEL:
                    continue
                around = bugs_around(x, y, z, levels)

                if current == BUG:
                    new[z][y][x] = BUG if around == 1 else EMPTY
                elif current == EMPTY:
                    new[z][y][x] = BUG if (around == 1 or around == 2) else EMPTY
                else:
                    assert False

    return new

def bugs_on_board(board):
    bugs = 0
    for y in range(0, len(board)):
        for square in board[y]:
            if square == BUG:
                bugs += 1
    return bugs

def part2(board, max_minutes):
    levels = [empty_board(), empty_board(), board, empty_board(), empty_board()]
    depth_0 = -2
    print_levels(levels, depth_0)

    num_minutes = 0
    while num_minutes < max_minutes:
        print(num_minutes)
        levels = evolve(levels)
        # Maintain an empty set of boards, which we use to avoid boundary misses.
        if bugs_on_board(levels[1]) != 0:
            levels = [empty_board()] + levels
            depth_0 -= 1
        if bugs_on_board(levels[-2]) != 0:
            levels += [empty_board()]
        num_minutes += 1
        print('\n')
        print_levels(levels, depth_0)
    print()

    bugs = 0
    for l in levels:
        bugs += bugs_on_board(l)
    print('ANSWER after %d minutes: %d bugs' % (num_minutes, bugs))

part2(parse_board(open('input').readlines()), 200) # 1983
# part2(parse_board(['....#', '#..#.', '#.?##', '..#..', '#....']), 10)
