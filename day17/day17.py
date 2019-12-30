from ascii_computer import AsciiComputer
import sys
sys.path.append('..')
from intcode.intcode import IntCodeComputer

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

# part1() # 4688

# x,y steps.
DIRECTIONS = [(0, -1), (1, 0), (0, 1), (-1, 0)]

TURN_LEFT = -10
TURN_RIGHT = -20

ORIGIN_Y = 26
ORIGIN_X = 20

MAX_PATH_LENGTH=42

class Part2:
    def __init__(self):
        self.lines = open('map.txt').readlines()
        self.scaffold_size = 0
        for y in range(len(self.lines)):
            for x in range(len(self.lines[y])):
                if self.at((x, y))== '^':
                    self.start_pos = (x, y)
                elif self.at((x, y)) == '#':
                    self.scaffold_size += 1

    def at(self, pos):
        (x, y) = pos
        try:
            return self.lines[y][x]
        except IndexError:
            return ''

    def path_from(self, path, pos, dir_idx):
        assert self.at(pos) == SCAFFOLDING or self.at(pos) == '^'
        print('PF', pos, dir_idx)
        def extend_path(dir_idx, pos):
            length = 0
            dir_idx = dir_idx % 4
            while True:
                next = (pos[0] + DIRECTIONS[dir_idx][0], pos[1] + DIRECTIONS[dir_idx][1])
                if self.at(next) == SCAFFOLDING:
                    length += 1
                    pos = next
                else:
                    return length
        def advance(pos, dir, length):
            return (pos[0] + length * dir[0], pos[1] + length * dir[1])

        left_path = extend_path(dir_idx - 1, pos)
        right_path = extend_path(dir_idx + 1, pos)
        if left_path == right_path and left_path == 0:
            return path
        elif left_path > 0 and right_path > 0:
            assert False # shouldn't happen.
        elif left_path > 0:
            dir_idx = (dir_idx - 1 ) % 4
            new_path = path[:]
            new_path = new_path + ['L' + str(left_path)]
            return self.path_from(new_path, advance(pos, DIRECTIONS[dir_idx], left_path), dir_idx)
        elif right_path > 0:
            dir_idx = (dir_idx + 1 ) % 4
            new_path = path[:]
            new_path = new_path + ['R' + str(right_path)]
            return self.path_from(new_path, advance(pos, DIRECTIONS[dir_idx], right_path), dir_idx)
        else:
            assert False

    def calculate_path(self):
        return self.path_from([], self.start_pos, 0)
    
    def path_patterns(self, path):
        MAX_PATTERN_LEN = 10
        patterns = []
        for i in range(len(path)):
            here = []
            for j in range(1, MAX_PATTERN_LEN):
                if i + j > len(path):
                    continue
                here.append(path[i:i + j])
            patterns.append(here)
        return patterns

    def spanning_patterns(self, patterns):
        def recurse_patterns(idx, used, pattern_path):
            #print('RP: ', idx, used, pattern_path)
            if idx > len(patterns):
                return False
            if idx == len(patterns) and len(used) < 4:
                print('SPaNNED: ', pattern_path)
                return (used, pattern_path)
            if len(used) > 3:
                return False
            for p in patterns[idx]:
                new_used = used[:]
                if p not in new_used:
                    new_used.append(p)
                new_pattern_path = pattern_path[:]
                new_pattern_path.append(p)
                recursed = recurse_patterns(idx + len(p), new_used, new_pattern_path)
                if recursed:
                    return recursed
            return False
        return recurse_patterns(0, [], [])

    def generate_input(self, spanned):
        (used, pattern_path) = spanned
        main = []
        for pattern in pattern_path:
            used_idx = used.index(pattern)
            assert used_idx != -1
            letter = chr(ord('A') + used_idx)
            main.append(letter)
        ret = ','.join(main) + '\n'
        for u in used:
            here = []
            for up in u:
                dir = up[0]
                dist = up[1:]
                here += [dir, dist]
            ret += ','.join(here) + '\n'

        return ret

def part2():
    p2 = Part2()
    path = p2.calculate_path()
    print(path)
    patterns = p2.path_patterns(path)
    for p in patterns:
        print(p)
    spanned = p2.spanning_patterns(patterns)
    print(spanned)

    inp = p2.generate_input(spanned)
    print(inp)

    memory = list(map(lambda m: int(m), open('input').readline().split(',')))
    assert memory[0] == 1
    memory[0] = 2
    ic = IntCodeComputer(memory, list(map(lambda x: ord(x), inp)))
    while ic.halted == False:
        ic.step()
    print(ic.outputs)


part2() # 714866
