POSITION_MODE = '0'
IMMEDIATE_MODE = '1'
RELATIVE_MODE = '2'

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
        self.relative_base = 0

    def decode_opcode(self, packed_opcode):
        """Returns [opcode, immediate1, 2, 3]."""
        packed_opcode = str(packed_opcode)
        while(len(packed_opcode) != 5):
            packed_opcode = '0' + packed_opcode

        return [int(packed_opcode[3:]), packed_opcode[2], packed_opcode[1], packed_opcode[0]]

    def advance_pc(self):
        self.pc += 1

    def read_pc(self, param_mode):
        at_pc = self.get_memory(self.pc)
        if param_mode == POSITION_MODE:
            return self.get_memory(at_pc)
        if param_mode == IMMEDIATE_MODE:
            return at_pc
        elif param_mode == RELATIVE_MODE:
            return self.get_memory_relative(at_pc)
        else:
            assert False, ('Unknown param mode: ' % (param_mode))

    def eat_pc_value(self):
        pc_value = self.memory[self.pc]
        self.advance_pc()
        return pc_value

    def eat_pc(self, param_mode):
        here = self.read_pc(param_mode)
        self.advance_pc()
        return here
    
    def set_memory(self, address, value):
        self.extend_memory_to_address(address)
        if self.debugging:
            print('Setting memory at %d to %d' % (address, value))
        self.memory[address] = value

    def get_memory(self, address):
        assert address >= 0, 'Negative memory address.'
        self.extend_memory_to_address(address)
        return self.memory[address]

    def get_memory_relative(self, relative):
        return self.get_memory(relative + self.relative_base)

    def extend_memory_to_address(self, address):
        past_end = address - len(self.memory) + 1
        if (past_end > 0):
            empty_memory = [0] * past_end
            self.memory += empty_memory
            print('Extended memory by %d', len(empty_memory))

    def set_pc(self, new_pc):
        if self.debugging:
            print('Jumping from %d to %d' % (self.pc, new_pc))
        self.pc = new_pc

    def set_memory_pc_address(self, value, mode):
        assert mode != IMMEDIATE_MODE, 'Can''t set IMMEDIATE'
        pc_value = self.eat_pc_value()
        address = pc_value
        if RELATIVE_MODE == mode:
            address += self.relative_base
        self.set_memory(address, value)

    def step(self):
        """Steps the machine 1 instruction, returning True if halted."""
        start_pc = self.pc
        decoded_opcode = self.decode_opcode(self.eat_pc_value())
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
        elif 9 == opcode:
            self.adjust_relative_base_instruction(decoded_opcode)
        elif 99 == opcode:
            self.halt_instruction(decoded_opcode)
        else:
            raise AssertionError('Unknown opcode: %s', decoded_opcode)
        
    def add_multiply_instruction(self, decoded_opcode):
        # print('Starting add at %d' % (self.pc))
        input1 = self.eat_pc(decoded_opcode[1])
        input2 = self.eat_pc(decoded_opcode[2])
        if 1 == decoded_opcode[0]:
            result = input1 + input2
        else:
            result = input1 * input2

        self.set_memory_pc_address(result, decoded_opcode[3])

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
        self.set_memory_pc_address(val, decoded_opcode[1])

    def output_instruction(self, decoded_opcode):
        param_mode = decoded_opcode[1]
        pc_contents = self.eat_pc_value()
        if param_mode == POSITION_MODE:
            out = self.get_memory(pc_contents)
        elif param_mode == IMMEDIATE_MODE:
            out = pc_contents
        elif param_mode == RELATIVE_MODE:
            out = self.get_memory_relative(pc_contents)
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
        
        self.set_memory_pc_address(1 if condition else 0, decoded_opcode[3])

    def adjust_relative_base_instruction(self, decoded_opcode):
        delta = self.eat_pc(decoded_opcode[1])
        self.relative_base += delta

    def print_memory(self):
        print(self.memory)

    def run_until_halt(self):
        while not self.halted:
            self.step()
