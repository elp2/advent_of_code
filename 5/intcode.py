class IntCodeComputer:
    def __init__(self, memory):
        self.pc = 0
        self.memory = memory
        self.halted = False
        self.debugging = True

    def decode_opcode(self, packed_opcode):
        """Returns [opcode, immediate1, 2, 3]."""
        opcode = packed_opcode % 100
        packed_opcode -= opcode
        packed_opcode /= 100
        decoded = [opcode]
        decoded.append(packed_opcode % 10 == 1)
        packed_opcode /= 10        
        decoded.append(packed_opcode % 10 == 1)
        packed_opcode /= 10        
        decoded.append(packed_opcode % 10 == 1)
        return decoded

    def advance_pc(self):
        self.pc += 1

    def read_pc(self, immediate):
        at_pc = self.memory[self.pc]
        if immediate:
            return at_pc
        else:
            return self.memory[at_pc]

    def eat_pc(self, immediate):
        here = self.read_pc(immediate)
        self.advance_pc()
        return here
    
    def set_memory(self, address, value):
        if self.debugging:
            print('Setting memory at %d to %d' % (address, value))
        self.memory[address] = value

    def step(self):
        """Steps the machine 1 instruction, returning True if halted."""
        decoded_opcode = self.decode_opcode(self.eat_pc(True))
        opcode = decoded_opcode[0]
        if 1 == opcode or 2 == opcode:
            self.add_multiply_instruction(decoded_opcode)
        elif 99 == opcode:
            self.halt(decoded_opcode)
        else:
            print('Unknown opcode: ', opcode)
            raise AssertionError('!')
        
    def add_multiply_instruction(self, decoded_opcode):
        input1 = self.eat_pc(decoded_opcode[1])
        input2 = self.eat_pc(decoded_opcode[2])
        destination = self.eat_pc(decoded_opcode[3])
        if 1 == decoded_opcode[0]:
            result = input1 + input2
        else:
            result = input1 * input2
        self.set_memory(destination, result)

    def halt(self, decoded_opcode):
        self.halted = True

    def print_memory(self):
        print(self.memory)

def test_day2():
    day2_memory = list(map(lambda m: int(m), open('5/day2').readline().split(',')))
    day2_memory[1] = 12
    day2_memory[2] = 2
    ic = IntCodeComputer(day2_memory)
    while not ic.halted:
        ic.step()
    ic.print_memory()

