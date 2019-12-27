import sys
sys.path.append('..')

from intcode.intcode import IntCodeComputer

from itertools import product

def part1():
    memory = list(map(lambda m: int(m), open('input').readline().split(',')))
    ic = IntCodeComputer(memory, [])

    area = []
    for y in range(0, 50):
        area.append(['?'] * 50)
    
    num_affected = 0
    for coord in product(range(0, 50), repeat=2):
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

part1()