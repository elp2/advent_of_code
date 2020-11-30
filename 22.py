from collections import defaultdict

def read_board(lines):
    def return_empty():
        return "."
    board = defaultdict(return_empty)
    zero_x = int(len(lines[0].strip()) / 2)
    zero_y = int(len(lines) / 2)

    for y in range(len(lines)):
        for x in range(len(lines[0].strip())):
            board[(x - zero_x, y - zero_y)] = lines[y][x]
    
    return board
  

INFECTED="#"
CLEAN="."
def part1(lines):
    caused_infection = 0
    board = read_board(lines)
    pos = (0, 0)
    dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    dir = 0 # right +, left -
    for burst in range(10_000):
        # Turn if infected
        here = board[pos]
        if here == INFECTED:
            dir = (dir + 1) % len(dirs)
        else:
            dir = (dir - 1 + len(dirs)) % len(dirs)
        # Swap Clean / infected
        if board[pos] == CLEAN:
            caused_infection += 1
            board[pos] = INFECTED
        else:
            board[pos] = CLEAN
        # Move forward.
        dx, dy = dirs[dir]
        pos = (pos[0] + dx, pos[1] + dy)
    print(caused_infection)

REAL=open("22.txt").readlines()
SAMPLE=open("22.sample").readlines()

part1(REAL)
