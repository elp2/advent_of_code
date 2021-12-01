from amplifiers import Amplifiers

def part1():
    program = open('input').readline()
    a = Amplifiers(program)
    print('Part1 %s' % (a.find_highest_signal()))

part1() # 206580

def part2():
    program = open('input').readline()
    a = Amplifiers(program)
    print('Part2 %s' % (a.find_highest_feedback()))

part2() # [2299406, (6, 5, 9, 7, 8)]