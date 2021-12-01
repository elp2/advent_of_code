import sys
sys.path.append('..')

from intcode.intcode import IntCodeComputer

class TractorBeam:
    def __init__(self):
        self.memory = list(map(lambda m: int(m), open('input').readline().split(',')))

    def beam_affects(self, x, y):
        """Returns True if the beam affects (x, y)."""
        # print(x, y)
        ic = IntCodeComputer(self.memory[:], [x, y])
        while len(ic.outputs) == 0:
            ic.step()
        [res] = ic.outputs
        return 1 == res

    def dimensions_at(self, y, step = 10):
        x = 0
        while not self.beam_affects(x, y):
            x += step
        start = x - step
        while not self.beam_affects(start, y):
            start += 1
        
        x = start
        while self.beam_affects(x, y):
            x += step
        end = x - step
        while self.beam_affects(end, y):
            end += 1

        return [start, end - start]

    def print_y(self, y):
        line = ''
        x = 0
        while not self.beam_affects(x, y):
            line += '.'
            x += 1
        line += '*'
        while self.beam_affects(x, y):
            line += '*'
            x += 1
        print(line)

def write_beam():
    tb = TractorBeam()
    f = open('beam.txt', 'w')
    for y in range(252, 600, 1):
        day = tb.dimensions_at(y)
        line = '%d %d %d' % (y, day[0], day[1])
        f.write(line + '\n')
        print(line)
    f.close()