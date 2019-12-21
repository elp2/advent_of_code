def wire_positions(path_line):
    positions = {}
    pos = [0,0]
    signal_length = 0
    for move in path_line.split(','):
        if move[0] == 'U':
            delta = [0, 1]
        elif move[0] == 'D':
            delta = [0, -1]
        elif move[0] == 'L':
            delta = [-1, 0]
        elif move[0] == 'R':
            delta = [1, 0]
        else:
            print("unknown move: ", move[0])
        distance = int(move[1:])

        while distance > 0:
            signal_length += 1
            pos[0] += delta[0]
            pos[1] += delta[1]
            strpos = str(pos)
            if not strpos in positions:
                positions[strpos] = signal_length
            distance -= 1
    return positions

lines = open('input').readlines()
w1 = wire_positions(lines[0])
w2 = wire_positions(lines[1])


min_distance = 1000000000
for pos in w1.keys():
    if not pos in w2:
        continue
    distance = w1[pos] + w2[pos]
    if min_distance > distance:
        min_distance = distance

print(min_distance) # 3454
