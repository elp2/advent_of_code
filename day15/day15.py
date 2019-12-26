import sys
sys.path.append('..')
from intcode.intcode import IntCodeComputer

NORTH = 1
SOUTH = 2
WEST = 3
EAST = 4
AROUND = [(0, -1), (1, 0), (0, 1), (-1, 0)]

MAP_CENTER = 50

class Searcher:
    def __init__(self):
        self.fastest_path = {(0,0): 0}
        self.queue = list(map(lambda x: [x], AROUND))
        self.memory = list(map(lambda m: int(m), open('input').readline().split(',')))
        self.text_map = []
        for y in range(0, MAP_CENTER * 2):
            self.text_map.append(['.'] * (MAP_CENTER * 2))

    def search(self):
        while len(self.queue):
            path = self.queue[0]
            self.queue = self.queue[1:]
            result = self.try_path(path)
            destination = path[-1]
            self.fastest_path[destination] = len(path)
            if len(self.fastest_path) % 50 == 0:
                self.print_text_map()
            # print('%s %s -> %d' % (path, destination, result))
            if result == 2:
                print('Found oxygen at %s len=%d' % (path, len(path)))
                self.add_to_map('O', destination)
                return True
            elif result == 1:
                self.add_to_map(' ', destination)
                self.continue_path(path)
            elif result == 0:
                self.add_to_map('*', destination)
                # Nothing to do since this is a wall.
                continue
            else:
                assert False, 'Unexpected search result %d' % (result)

        self.print_text_map()
        assert False, 'Finished without Oxygen!'
    
    def add_to_map(self, char, pos):
        self.text_map[pos[1]+MAP_CENTER][pos[0]+MAP_CENTER] = char

    def print_text_map(self):
        for line in self.text_map:
            print(''.join(line))

    def continue_path(self, path):
        pos = path[-1]
        for delta in AROUND:
            x = pos[0] + delta[0]
            y = pos[1] + delta[1]
            new_pos = (x,y)
            if new_pos in self.fastest_path:
                continue
            pos_path = path[:]
            pos_path.append(new_pos)
            self.queue.append(pos_path)
    
    def direction_between(self, prev, next):
        dir = (next[0] - prev[0], next[1] - prev[1])
        if dir == (0, -1):
            return NORTH
        elif dir == (0, 1):
            return SOUTH
        elif dir == (1, 0):
            return EAST
        elif dir == (-1, 0):
            return WEST
        else:
            AssertionError('Unknown dir: %s' % (dir))

    def try_path(self, path):
        """Returns the result of executing this path."""
        prev = (0, 0)
        dirs = []
        for i in range(0, len(path)):
            point = path[i]
            dirs.append(self.direction_between(prev, point))
            prev = point
        ic = IntCodeComputer(self.memory[:], dirs)
        ic.debugging = False
        while len(ic.outputs) != len(path):
            ic.step()
            assert ic.halted == False
        assert len(ic.inputs) == 0
        return ic.outputs[-1]
    

def part1():
    searcher = Searcher()
    searcher.search()

# part1() # 226
