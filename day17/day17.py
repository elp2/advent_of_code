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
    print('\n'.join(lines))

#part1() # 4688

# x,y steps.
DIRECTIONS = [[0, 1], [1, 0], [0, -1], [-1, 0]]

TURN_LEFT = -10
TURN_RIGHT = -20

ORIGIN_Y = 26
ORIGIN_X = 20


class ScaffoldMap:
    def __init__(self):
        self.lines = open('map.txt').readlines()
        assert self.lines[ORIGIN_Y][ORIGIN_X] == SCAFFOLDING # Hard coded this to a scaffold to avoid special casing.

        # Index into DIRECTIONS. Turning left moves index -1, right +1.
        self.direction = 0 
        self.solutions = []
        self.find_intersections()

    def find_intersections(self):
        lines = self.lines
        self.intersections = []
        for y in range(0, len(lines)):
            for x in range(0, len(lines[y].strip())):
                up = y > 0 and lines[y-1][x] == SCAFFOLDING
                down = y < len(lines) - 1 and lines[y+1][x] == SCAFFOLDING
                left = x > 0 and lines[y][x-1] == SCAFFOLDING
                right = x < len(lines[y]) - 1 and lines[y][x+1] == SCAFFOLDING
                redirection = (up or down) and (left or right)
                dead_end = [up, down, left, right].count(True) == 1
                if redirection or dead_end:
                    self.intersections.append((x, y))


scaffold_map = ScaffoldMap()
