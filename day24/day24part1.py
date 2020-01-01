BUG = '#'
EMPTY = '.'
LOWER_LEVEL = '?'

def parse_board():
    board = []
    for line in open('input').readlines():
        for char in line.strip():
            board.append(char)
    board[2*5 + 2] = LOWER_LEVEL
    return board

def print_board(board):
    for y in range(0, 5):
        print(''.join(board[y * 5:y * 5 + 5]))        

def board_at(board, x, y):
    idx = x + 5 * y
    if x < 0 or x > 4 or y < 0 or y > 4:
        return None
    return board[idx]

def bugs_around(x, y, z, levels):
    around = 0

def evolve(levels):
    new = levels[:]
    for z in range(0, len(levels)):
        for y in range(0, 5):
            for x in range(0, 5):
                current = levels[z][y][x]
                if current == LOWER_LEVEL:
                    continue
                around = bugs_around(x, y, z, levels)

                if current == BUG:
                    levels[z][y

    return new

def part1():
    board = parse_board()
    seen_boards = {}
    num_minutes = 0
    while True:
        # print_board(board)
        # print('------------------------------------------------')

        board_str = ('').join(board)
        if board_str in seen_boards:
            print(board)
            biodiversity = 0
            power = 1
            for i in range(0, 25):
                if board[i] == BUG:
                    biodiversity += power
                power *= 2
            print('Biodiversity: %d @ %d' % (biodiversity, num_minutes))
            break
        seen_boards[board_str] = True
        board = evolve(board)
        num_minutes += 1
        if num_minutes % 100 == 0:
            print(num_minutes)

# 16778801 too low
# 14545834 too low - fix empty bug
# 20751345 is juuust right! Fix overlapping into next row bug.
# part1()