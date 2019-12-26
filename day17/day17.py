from ascii_computer import AsciiComputer

SCAFFOLDING = '#'

def part1():
    ac = AsciiComputer()

    total = 0
    lines = ac.run().split('\n')
    for y in range(1, len(lines) - 3):
        for x in range(1, len(lines[0].strip()) - 1):

            if lines[y][x] == SCAFFOLDING:
                if lines[y-1][x] == SCAFFOLDING and lines[y+1][x] == SCAFFOLDING and lines[y][x+1] == SCAFFOLDING and lines[y][x-1] == SCAFFOLDING:
                    alignment_parameter = x * y
                    print('Intersection at %d, %d, AP = %d' % (x, y, alignment_parameter))
                    total += alignment_parameter

    print('Alignment Parameter: %d' % (total))

part1() # 4688