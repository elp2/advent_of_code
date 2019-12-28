BUG = '#'
EMPTY = '.'

def parse_board():
    board = []
    for line in open('input').readlines():
        for char in line.strip():
            board.append(char)
    return board

def print_board(board):
    for y in range(0, 5):
        print(''.join(board[y * 5:y * 5 + 5]))        

def board_at(board, x, y):
    idx = x + 5 * y
    if x < 0 or x > 4 or y < 0 or y > 4:
        return None
    return board[idx]

def evolve(board):
    new = board[:]
    for y in range(0, 5):
        for x in range(0, 5):
            bugs_around = 0
            if board_at(board, x + 1, y) == BUG:
                bugs_around += 1
            if board_at(board, x - 1, y) == BUG:
                bugs_around += 1
            if board_at(board, x, y + 1) == BUG:
                bugs_around += 1
            if board_at(board, x, y - 1) == BUG:
                bugs_around += 1

            here = board_at(board, x, y)
            if here == BUG:
                new[y * 5 + x] = BUG if bugs_around == 1 else EMPTY
            else:
                new[y * 5 + x] = BUG if (bugs_around == 1 or bugs_around == 2) else EMPTY
            print('%d, %d [%d] (%s -> %s)' % (x, y, bugs_around, board_at(board, x,y), board_at(new, x, y)))
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
part1()