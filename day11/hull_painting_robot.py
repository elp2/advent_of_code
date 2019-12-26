import sys
sys.path.append('..')
from intcode.intcode import IntCodeComputer


GRID_RADIUS = 100

BLACK = 0
WHITE = 1

LEFT = 0
RIGHT = 1

# Left moves left through array and vice versa.
AROUND = [(0, -1), (1, 0), (0, 1), (-1, 0)]

class HullPaintingRobot:
    def __init__(self):
        self.ic = IntCodeComputer(list(map(lambda m: int(m), open('input').readline().split(','))))
        self.ic.debugging = False
        self.painted = []
        self.grid = []
        for y in range(0, 2 * GRID_RADIUS):
            self.grid.append([BLACK] * (GRID_RADIUS * 2))
            self.painted.append([False] * (GRID_RADIUS * 2))
        self.pos = (GRID_RADIUS, GRID_RADIUS)
        self.direction_index = 0

    def print_grid(self):
        for y in range(0, len(self.grid)):
            print(''.join(self.grid[y]))
    
    def paint_until_halt(self):
        while self.ic.halted == False:
            (x, y) = self.pos
            [to_paint, turn_direction] = self.step(self.grid[y][x])
            self.grid[y][x] = to_paint
            self.painted[y][x] = True
            self.direction_index += -1 if LEFT == turn_direction else 1
            self.direction_index += 4
            self.direction_index = self.direction_index % 4
            self.pos = [self.pos[0] + AROUND[self.direction_index][0], self.pos[1] + AROUND[self.direction_index][1]]

        num_painted = 0
        for y in range(0, len(self.painted)):
            for x in range(0, len(self.painted[y])):
                if self.painted[y][x]:
                    num_painted += 1
        print('Painted at least once: %d' % (num_painted))

    def step(self, over_color):
        assert(len(self.ic.inputs)) == 0
        self.ic.inputs = [over_color]
        while len(self.ic.outputs) != 2:
            self.ic.step()
        ret = self.ic.outputs
        self.ic.outputs = []
        return ret
