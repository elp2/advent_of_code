import sys
sys.path.append('..')

from intcode.intcode import IntCodeComputer

from itertools import product

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