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
WEAKENED="W"
FLAGGED="F"
def part1(lines):
    caused_infection = 0
    board = read_board(lines)
    pos = (0, 0)
    dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    dir = 0 # right +, left -
    for burst in range(10_000_000):
        # Turn if infected
        here = board[pos]
        if here == INFECTED:
            dir = (dir + 1) % len(dirs)
        # elif here == WEAKENED:
        #     # nop
        elif here == CLEAN:
            dir = (dir - 1 + len(dirs)) % len(dirs)
        elif here == FLAGGED:
            dir = (dir - 2 + len(dirs)) % len(dirs)
        else:
            assert here == WEAKENED         
        # Swap Clean / infected
        if board[pos] == WEAKENED:
            caused_infection += 1
            board[pos] = INFECTED
        elif board[pos] == CLEAN:
            board[pos] = WEAKENED
        elif board[pos] == INFECTED:
            board[pos] = FLAGGED
        elif board[pos] == FLAGGED:
            board[pos] = CLEAN
        else:
            assert False
        # Move forward.
        dx, dy = dirs[dir]
        pos = (pos[0] + dx, pos[1] + dy)
    print(caused_infection)

REAL=open("22.txt").readlines()
SAMPLE=open("22.sample").readlines()

# part1(SAMPLE) # 2511944
part1(REAL) # 2511776