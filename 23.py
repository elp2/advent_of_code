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
    elif instruction == "sub":
        regs[a] -= num_or_reg_value(b, regs)
    elif instruction == "mul":
        regs[a] *= num_or_reg_value(b, regs)
    elif instruction == "mod":
        regs[a] = regs[a] % num_or_reg_value(b, regs)


REAL = open("18.txt").readlines()
SAMPLE2 = open("18.sample2").readlines()
from collections import defaultdict


class Program:
    def __init__(self, p, commands):
        def return_zero():
            return 0
        self.regs = defaultdict(return_zero)
        self.regs["p"] = p
        self.pc = 0
        self.finished = False
        self.queue = []
        self.commands = commands
        self.waiting_for_value = False
        self.values_sent = 0
        self.muls = 0


    def step_program(self):
        if self.pc < 0 or self.pc >= len(self.commands):
            self.finished = True
            return None

        # print(self.pc, self.regs, self.queue)
        command = self.commands[self.pc]
        split = command.strip().split(" ")
        instruction = split[0]

        # jgz X Y jumps with an offset of the value of Y, but only if the value of X is greater than zero.
        # (An offset of 2 skips the next instruction, an offset of -1 jumps to the previous instruction, and so on.)
        if instruction == "jgz":
            x = split[1]
            y = split[2]
            do_jump = num_or_reg_value(x, self.regs) > 0
            if do_jump:
                self.pc = self.pc + num_or_reg_value(y, self.regs)
            else:
                self.pc += 1
            if self.pc < 0 or self.pc >= len(self.commands):
                self.finished = True
            return None
        if instruction == "jnz":
            x = split[1]
            y = split[2]
            do_jump = num_or_reg_value(x, self.regs) != 0
            if do_jump:
                self.pc = self.pc + num_or_reg_value(y, self.regs)
            else:
                self.pc += 1
            if self.pc < 0 or self.pc >= len(self.commands):
                self.finished = True
            return None

        if instruction == "mul":
            self.muls += 1
            # mul X Y sets register X to the result of multiplying the value contained in register X by the value of Y.
            # mul X Y sets register X to the result of multiplying the value contained in register X by the value of Y.
        if instruction in ["set", "add", "mul", "mod", "sub"]:
            set_regs(command, self.regs)
            self.pc += 1
            return None
        elif instruction == "snd":
            snd = num_or_reg_value(split[1], self.regs)
            self.pc += 1
            self.values_sent += 1
            
            return snd
        elif instruction == "rcv":
            if 0 == len(self.queue):
                self.waiting_for_value = True
                # Do not advance PC since we want to try rcv again.
                return None
            self.waiting_for_value = False 
            received = self.queue[0]
            self.regs[split[1]] = received
            self.queue = self.queue[1:]
            self.pc += 1
            return None
        assert False

    def deadlocked(self):
        return self.waiting_for_value and len(self.queue) == 0
    
    def send_message(self, message):
        self.queue.append(message)

def part1(commands):
    p0 = Program(0, commands)
    while True:
        p0_msg = p0.step_program()
        if p0.finished:
            break
        if p0.deadlocked():
            break
        
    print(p0.muls)

# part2(REAL) # 7493 - insanely slow if I allowed it to print out each step.

REAL = open("23.txt").readlines()
part1(REAL)
