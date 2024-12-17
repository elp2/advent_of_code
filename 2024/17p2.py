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

BEST_OUT=0
def simulate(a, b, c, program):
    origa = a
    global BEST_OUT
    ret = 0

    pc = 0
    out = []
    outidx = 0

    done = False

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

        # print("@", pc, "R:", a, b, c, "op", opcode, "l/c", literal, combo)

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
            if done:
                return False # should not be outputting
            toout = combo % 8
            if program[outidx] == toout:
                outidx += 1
                if outidx >= len(program):
                    done = True
                out.append(toout)
                pass
            else:
                break
                return False
            
        elif opcode == 6:
            b = a // pow(2, combo)
        elif opcode == 7:
            c = a // pow(2, combo)

        pc = jmp

    if len(out) > BEST_OUT:
        print(origa, bin(origa), a, out)
        BEST_OUT=len(out)
    return done == True

def find_mina(program, expmax=None):
    
    a = 0
    base = "11101100011011111110111001110000011000000010"
    while True:
        abin = bin(a)[2:] + base

        if a % 10000000 == 0:
            print(a)
        a += 1

        asint = int(abin, 2)
        if simulate(asint, 0, 0, program):
            return asint
        if expmax is not None:
            assert a < expmax

# 0,1
# A = A / 2
# 5,4
# Out(A % 8)
# 3,0
# Jump 0




if __name__ == "__main__":
    # sample = find_mina([0,3,5,4,3,0], 117440)
    # assert sample == 117440
    # print(sample)

    real = find_mina([2,4,1,4,7,5,4,1,1,4,5,5,0,3,3,0])
    print("Found: ", real)

