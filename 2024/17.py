from collections import defaultdict, deque, Counter
from itertools import combinations, combinations_with_replacement, permutations, product
from functools import reduce, cmp_to_key
from operator import add, mul, itemgetter, attrgetter
import os
from parse import parse
import sys
from re import findall

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, root_dir)
from aoc_elp import *

######################
SAMPLE_EXPECTED = "4,6,3,5,6,3,5,2,1,0"
######################
assert SAMPLE_EXPECTED != None, "Must enter sample value"

def parse_group(group):
    lines = group.split("\n")
    ret = []
    for y, line in enumerate(lines):
        line = line.strip()
        assert len(line) != 0

        split = line.split(" ")

        for x, xc in enumerate(split):
            pass

        assert len(split) != 0
        ret.append(split)

    return ret


def parse_lines(raw):
    registers, program = raw.split("\n\n")
    registers = registers.split("\n")
    [a] = map(int, findall("\d+", registers[0]))
    [b] = map(int, findall("\d+", registers[1]))
    [c] = map(int, findall("\d+", registers[2]))

    program = program.replace("Program: ", "")
    program = list(map(int, program.split(",")))

    return a, b, c, program


def solve(raw):
    a, b, c, program = parse_lines(raw)
    return simulate(a, b, c, program)

def simulate(a, b, c, program):
    ret = 0

    pc = 0
    out = []

    while pc < len(program):
        # input("input: ")
        opcode, literal = program[pc: pc + 2]

        combo = literal
        if literal == 4:
            combo = a
        elif literal == 5:
            combo = b
        elif literal == 6:
            combo = c
        # assert literal != 7 # for part 1 :( ?

        print("@", pc, "R:", a, b, c, "op", opcode, "l/c", literal, combo)


        jmp = pc + 2
        if opcode == 0:
            a = a // pow(2, combo)
        elif opcode == 1:
            b = b ^ literal
        elif opcode == 2:
            b = combo % 8
        elif opcode == 3:
            if a == 0:
                pass
            else:
                jmp = literal
            # The jnz instruction (opcode 3) does nothing if the A register is 0. 
            # However, if the A register is not zero, it jumps by setting the instruction pointer to the value of its 
            # literal operand; if this instruction jumps, the instruction pointer is not increased by 2 after this
            # instruction.
        elif opcode == 4:
            b = b ^ c
        elif opcode == 5:
            out.append(str(combo % 8))
            print("Out: ", out[-1])
        elif opcode == 6:
            b = a // pow(2, combo)
        elif opcode == 7:
            c = a // pow(2, combo)

        pc = jmp


    return ",".join(out), a, b, c

if __name__ == "__main__":
    SAMPLE, REAL = get_raw_inputs(sys.argv)

    ttf, a, _, _ = simulate(2024, 0, 0, [0,1,5,4,3,0])
    assert ttf == "4,2,5,6,7,7,7,7,3,1,0"
    assert a == 0


    zeroonetwo, _, _, _ = simulate(10, 0, 0, [5,0,5,1,5,4])
    assert zeroonetwo == "0,1,2"

    print("!")

    sample = solve(SAMPLE)
    assert sample[0] == SAMPLE_EXPECTED, "Sample Result %s != %s expected" % (sample, SAMPLE_EXPECTED)
    print("\n*** SAMPLE PASSED ***\n")

    solved = solve(REAL)
    print("SOLUTION: ", solved)
