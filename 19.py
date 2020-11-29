def part1(board):
    y = 0
    x = list(board[0]).index("|")
    dx = 0
    dy = 1

    def square(x, y):
        if y < 0 or y >= len(board):
            return None
        row = board[y]
        if x < 0 or x >= len(row):
            return None
        return row[x]

    seen = ""
    distance = -1
    px, py = None, None
    while True:
        here = square(x, y)
        if here is None or here == " ":
            break
        distance += 1

        if here in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            seen += here
        
        if here == "+":
            deltas = [(-1, 0), (1, 0), (0, 1), (0, -1)]

            ndx, ndy = None, None
            for d in deltas:
                edx, edy = d
                ex = x + edx
                ey = y + edy
                if (ex, ey) == (px, py):
                    # Loop back, skip.
                    continue
                sq = square(ex, ey)
                print(sq)
                if None == sq:
                    continue
                if sq in ('-ABCDEFGHIJKLMNOPQRSTUVWXYZ|'):
                    ndx, ndy = edx, edy
            assert ndx is not None
            dx = ndx
            dy = ndy
        px, py = x, y
        x += dx
        y += dy
        print(x, y, here, seen, distance)
    print(seen, distance)

        
SAMPLE = open("19.sample").readlines()
REAL = open("19.txt").readlines()
part1(REAL) # 16334 too high, 16333 too high, 16331 low, 16332 juuust right. Bedtime.
