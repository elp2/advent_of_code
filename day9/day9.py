import sys
sys.path.append('..')

from intcode.intcode import IntCodeComputer

def part1():
    memory = list(map(lambda m: int(m), open('input').readline().split(',')))
    ic = IntCodeComputer(memory, [1])
    ic.run_until_halt()
    print(ic.outputs)

# part1()

def part2():
    memory = list(map(lambda m: int(m), open('input').readline().split(',')))
    ic = IntCodeComputer(memory, [2])
    ic.debugging = False
    ic.run_until_halt()
    print(ic.outputs)

part2()