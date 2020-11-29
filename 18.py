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

        if instruction in ["set", "add", "mul", "mod"]:
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

def part2(commands):
    p0 = Program(0, commands)
    p1 = Program(1, commands)
    deadlocked = 0
    while True:
        p0_msg = p0.step_program()
        if p0_msg != None:
            p1.send_message(p0_msg)
        p1_msg = p1.step_program()
        if p1_msg != None:
            p0.send_message(p1_msg)
        if deadlocked > 10:
            break
        if p0.finished and p1.finished:
            break
        if p0.deadlocked() and p1.deadlocked():
            break
        
    print(p1.values_sent)

part2(REAL) # 7493 - insanely slow if I allowed it to print out each step.
