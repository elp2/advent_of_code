import sys
sys.path.append('..')

from intcode.intcode import IntCodeComputer

from itertools import product
from tractor_beam import TractorBeam
from math import sqrt

def part1():
#    ic.debugging = True

    area = []
    for y in range(0, 50):
        area.append(['?'] * 50)
    
    num_affected = 0
    for coord in product(range(0, 50), repeat=2):
        print(coord)
        # Intcode halts after each one. Advancing past halt results in 0 opcode.
        # Assuming this is due to drones having their own computers.
        memory = list(map(lambda m: int(m), open('input').readline().split(',')))
        ic = IntCodeComputer(memory, [])

        assert len(ic.inputs) == 0
        ic.inputs = list(coord)
        while len(ic.outputs) == 0:
            ic.step()
        [res] = ic.outputs
        [x, y] = coord
        area[y][x] = '*' if res == 1 else '.'
        if res == 1:
            num_affected += 1

        ic.outputs = []
    
    for y in range(0, len(area)):
        print(''.join(area[y]))

# part1() # 129, map.txt

def in_beam(beam, x, y):
    [start, end] = beam[y]
    return x >= start and x <= end

def box_fits(tb, beam, origin, bottom_right):
    [ox, oy] = origin
    [bx, by] = bottom_right

    print(origin, bottom_right)
    assert bx - ox == 99 and by - oy == 99
    if not tb.beam_affects(ox, oy):
        return False
    if not tb.beam_affects(ox, by):
        return False
    if not tb.beam_affects(bx, oy):
        return False
    if not tb.beam_affects(bx, by):
        return False
    return True

def test_upper(tb, beam, y):
    """Returns origin or None if it doesn't fit."""
    [start, end] = beam[y]
    end_x = end - 1
    assert tb.beam_affects(end_x, y)
    assert not tb.beam_affects(end_x + 1, y)
    origin_x = end_x - 99
    bottom_y = y + 99

    origin = [origin_x, y]
    bottom_right = [end_x, bottom_y]
    if box_fits(tb, beam, origin, bottom_right):
        return origin
    else:
        return False

def test_bottom(tb, beam, y):
    """Returns origin or None if it doesn't fit."""
    [start, end] = beam[y]
    origin_x = start
    assert tb.beam_affects(origin_x, y)
    assert not tb.beam_affects(origin_x - 1, y)
    origin = [origin_x, y - 99]
    bottom_right = [origin_x + 99, y]
    if box_fits(tb, beam, origin, bottom_right):
        return origin
    else:
        return False

def score(origin):
    [x, y] = origin
    distance = sqrt(x * x + y * y)
    answer = 10000 * x + y
    print('%.2f: %d' % (distance, answer))

def part2():
    tb = TractorBeam()
    beam_lines = open('beam.txt').readlines()
    beam = {}
    for line in beam_lines:
        [y, start, width] = line.strip().split(' ')
        beam[int(y)] = [int(start), int(start) + int(width)]
    best_upper_right = None
    best_bottom_left = None
    for y in range(600, 1000):
        if y not in beam:
            day = tb.dimensions_at(y)
            beam[y] = [day[0], day[1] + day[0]]
        if not best_upper_right:
            best_upper_right = test_upper(tb, beam, y)
            if best_upper_right:
                score(best_upper_right) # [1418, 706] [1518, 806]
        if not best_bottom_left:
            best_bottom_left = test_bottom(tb, beam, y)
            if best_bottom_left:
                score(best_bottom_left)
                break
        if best_bottom_left and best_upper_right:
            score(best_bottom_left)
            score(best_upper_right)
            break

# part2() # 14040699