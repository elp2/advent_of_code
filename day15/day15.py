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


    def search(self, stop_at_oxygen=True):
        while len(self.queue):
            path = self.queue[0]
            self.queue = self.queue[1:]
            result = self.try_path(path)
            destination = path[-1]
            self.fastest_path[destination] = len(path)
            if len(self.fastest_path) % 200 == 0:
                self.print_text_map()
            # print('%s %s -> %d' % (path, destination, result))
            if result == 2:
                print('Found oxygen at %s len=%d' % (path, len(path)))
                self.add_to_map('O', destination)
                if stop_at_oxygen:
                    return True
                else:
                    self.continue_path(path)
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
        if stop_at_oxygen:
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

def get_full_map():
    searcher = Searcher()
    searcher.search(stop_at_oxygen=False)

# part1() # 226

# get_full_map()

def part2():
    oxygen_map = []
    for line in open('map.txt').readlines():
        split_line = []
        for char in line.strip():
            split_line.append(char)
        oxygen_map.append(split_line)
    empties = 0
    time = 0
    next_round = []
    for y in range(0, len(oxygen_map)):
        for x in range(0, len(oxygen_map[y])):
            if ' ' == oxygen_map[y][x]:
                empties += 1
            elif 'O' == oxygen_map[y][x]:
                next_round = [(x,y)] # Start out with these.
                oxygen_map[y][x] = ' ' # We are simulating the 0 minute

    assert [(38, 40)] == next_round

    while empties > 0:
        discovered = []
        for pos in next_round:
            [x, y] = pos
            assert oxygen_map[y][x] == ' '
            oxygen_map[y][x] = 'O'
            empties -= 1

            for delta in AROUND:
                x = pos[0] + delta[0]
                y = pos[1] + delta[1]
                new_pos = (x,y)
                if oxygen_map[new_pos[1]][new_pos[0]] != ' ' or new_pos in discovered or new_pos in next_round:
                    continue
                discovered.append(new_pos)
        time += 1
        if time % 20 == 0:
            for y in range(0, len(oxygen_map)):
                for x in range(0, len(oxygen_map[y])):
                    print(''.join(oxygen_map[y]))
        next_round = discovered
    print('Done at %d' % (time))

part2() # 342.