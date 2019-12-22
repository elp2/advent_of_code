class IntCodeComputer:
    def __init__(self, memory, inputs=[]):
        self.pc = 0
        self.memory = memory
        self.halted = False
        self.debugging = True
        print('Memory: len=%d' % (len(self.memory)))
        self.inputs = inputs
        self.inputs.reverse()
        self.outputs = []

    def decode_opcode(self, packed_opcode):
        """Returns [opcode, immediate1, 2, 3]."""
        packed_opcode = str(packed_opcode)
        while(len(packed_opcode) != 5):
            packed_opcode = '0' + packed_opcode

        return [int(packed_opcode[3:]), packed_opcode[2] == '1', packed_opcode[1] == '1', packed_opcode[0] == '1']

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

    def set_pc(self, new_pc):
        if self.debugging:
            print('Jumping from %d to %d' % (self.pc, new_pc))
        self.pc = new_pc

    def set_memory_pc_address(self, value):
        self.set_memory(self.eat_pc(True), value)

    def step(self):
        """Steps the machine 1 instruction, returning True if halted."""
        start_pc = self.pc
        decoded_opcode = self.decode_opcode(self.eat_pc(True))
        print('Step from PC=%d (%s)' % (start_pc, decoded_opcode))
        opcode = decoded_opcode[0]
        if 1 == opcode or 2 == opcode:
            self.add_multiply_instruction(decoded_opcode)
        elif 3 == opcode:
            self.input_instruction(decoded_opcode)
        elif 4 == opcode:
            self.output_instruction(decoded_opcode)
        elif 5 == opcode or 6 == opcode:
            self.jump_instruction(decoded_opcode)
        elif 7 == opcode or 8 == opcode:
            self.compare_instruction(decoded_opcode)
        elif 99 == opcode:
            self.halt_instruction(decoded_opcode)
        else:
            print('Unknown opcode: ', opcode)
            raise AssertionError('!')
        
    def add_multiply_instruction(self, decoded_opcode):
        # print('Starting add at %d' % (self.pc))
        input1 = self.eat_pc(decoded_opcode[1])
        input2 = self.eat_pc(decoded_opcode[2])
        if 1 == decoded_opcode[0]:
            result = input1 + input2
        else:
            result = input1 * input2
        if decoded_opcode[3] == True:
            raise AssertionError('Unexpected non positional store location.')
        self.set_memory_pc_address(result)

    def input_instruction(self, decoded_opcode):
        while True:
            if len(self.inputs):
                val = self.inputs.pop()
                break
            try:
                val = int(input('Enter value: '))
                break
            except ValueError:
                print('Enter integer value.')
        self.set_memory_pc_address(val)

    def output_instruction(self, decoded_opcode):
        out = self.eat_pc(True) if decoded_opcode[1] else self.memory[self.eat_pc(True)]
        print('*** Output: %d' % (out))
        self.outputs.append(out)

    def halt_instruction(self, decoded_opcode):
        self.halted = True

    def jump_instruction(self, decoded_opcode):
        condition = self.eat_pc(decoded_opcode[1])
        address = self.eat_pc(decoded_opcode[2])
        if (decoded_opcode[0] == 5 and condition != 0) or (decoded_opcode[0] == 6 and condition == 0):
            self.set_pc(address)

    def compare_instruction(self, decoded_opcode):
        a = self.eat_pc(decoded_opcode[1])
        b = self.eat_pc(decoded_opcode[2])
        opcode = decoded_opcode[0]
        if opcode == 7:
            condition = a < b
        elif opcode == 8:
            condition = a == b
        else:
            raise AssertionError('Unknown opcode')
        
        if decoded_opcode[3] == True:
            raise AssertionError('Unexpected non positional store location.')
        self.set_memory_pc_address(1 if condition else 0)

    def print_memory(self):
        print(self.memory)

    def run_until_halt(self):
        while not self.halted:
            self.step()
