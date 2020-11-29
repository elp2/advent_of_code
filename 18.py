# snd X plays a sound with a frequency equal to the value of X.
# set X Y sets register X to the value of Y.
# add X Y increases register X by the value of Y.
# mul X Y sets register X to the result of multiplying the value contained in register X by the value of Y.
# mod X Y sets register X to the remainder of dividing the value contained in register X by the value of Y (that is, it sets X to the result of X modulo Y).
# rcv X recovers the frequency of the last sound played, but only when the value of X is not zero. (If it is zero, the command does nothing.)


def num_or_reg_value(num, regs):
    try:
        return int(num)
    except ValueError:
        return regs[num]


def set_regs(command, regs):
    split = command.strip().split(" ")
    instruction = split[0]
    a = split[1]
    b = split[2]
    if instruction == "set":
        regs[a] = num_or_reg_value(b, regs)
    elif instruction == "add":
        regs[a] += num_or_reg_value(b, regs)
    elif instruction == "mul":
        regs[a] *= num_or_reg_value(b, regs)
    elif instruction == "mod":
        regs[a] = regs[a] % num_or_reg_value(b, regs)


REAL = open("18.txt").readlines()
SAMPLE = open("18.sample").readlines()
from collections import defaultdict


def run_program(commands):
    def return_zero():
        return 0
    regs = defaultdict(return_zero)
    pc = 0
    last_sound = None
    rcv_sound = None
    while pc >= 0 and pc < len(commands):
        print(pc, regs)
        command = commands[pc]
        split = command.strip().split(" ")
        instruction = split[0]


        # jgz X Y jumps with an offset of the value of Y, but only if the value of X is greater than zero.
        # (An offset of 2 skips the next instruction, an offset of -1 jumps to the previous instruction, and so on.)
        if instruction == "jgz":
            x = split[1]
            y = split[2]
            do_jump = num_or_reg_value(x, regs) > 0
            if do_jump:
                pc = pc + num_or_reg_value(y, regs)
            else:
                pc += 1
            continue

        if instruction in ["set", "add", "mul", "mod"]:
            set_regs(command, regs)
        elif instruction == "snd":
            snd = num_or_reg_value(split[1], regs)
            assert snd != 0 # not sure if necessary?
            last_sound = snd
            print("Sound: ", snd)
        elif instruction == "rcv":
            rcv = num_or_reg_value(split[1], regs)
            if 0 != rcv:
                rcv_sound = last_sound
                assert None != rcv_sound
                print("rcv: ", rcv_sound)
                return
        else:
            assert False

        pc += 1

# run_program(REAL) # 3423
