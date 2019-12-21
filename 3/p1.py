def wire_positions(path_line):
    positions = set()
    pos = [0,0]
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
            pos[0] += delta[0]
            pos[1] += delta[1]
            positions.add(str(pos))
            distance -= 1
    return positions

lines = open('input').readlines()
w1 = wire_positions(lines[0])
w2 = wire_positions(lines[1])

intersections = w1.intersection(w2)
print(intersections)

min_manhattan = 1000000000
for inter in intersections:
    i = eval(inter)
    manhattan_distance = abs(i[0]) + abs(i[1])
    if manhattan_distance < min_manhattan:
        min_manhattan = manhattan_distance

print(min_manhattan) # 217
