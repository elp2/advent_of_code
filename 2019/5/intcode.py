import unittest

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


def test_day2():
    day2_memory = list(map(lambda m: int(m), open('5/day2').readline().split(',')))
    day2_memory[1] = 12
    day2_memory[2] = 2
    ic = IntCodeComputer(day2_memory)
    while not ic.halted:
        ic.step()
    ic.print_memory()


def part1():
    day2_memory = list(map(lambda m: int(m), open('5/input').readline().split(',')))
    ic = IntCodeComputer(day2_memory)
    while not ic.halted:
        ic.step()
    ic.print_memory()

def run_test_case(program, inputs=[]):
    memory = list(map(lambda m: int(m), program.split(',')))
    ic = IntCodeComputer(memory, inputs)
    while not ic.halted:
        ic.step()
    return ic

class TestIntCode(unittest.TestCase):
    def run_case(self, program, inputs=[]):
        return run_test_case(program, inputs)

    def test_pos_eq_8(self):
        program = '3,9,8,9,10,9,4,9,99,-1,8'
        ic = self.run_case(program, [8])
        self.assertEqual(ic.outputs, [1])
        ic = self.run_case(program, [3])
        self.assertEqual(ic.outputs, [0])
        ic = self.run_case(program, [9])
        self.assertEqual(ic.outputs, [0])

    def test_pos_lt_8(self):
        program = '3,9,7,9,10,9,4,9,99,-1,8'
        ic = self.run_case(program, [7])
        self.assertEqual(ic.outputs, [1])
        ic = self.run_case(program, [3])
        self.assertEqual(ic.outputs, [1])
        ic = self.run_case(program, [9])
        self.assertEqual(ic.outputs, [0])

    def test_imm_eq_8(self):
        program = '3,3,1108,-1,8,3,4,3,99'
        ic = self.run_case(program, [7])
        self.assertEqual(ic.outputs, [0])
        ic = self.run_case(program, [3])
        self.assertEqual(ic.outputs, [0])
        ic = self.run_case(program, [8])
        self.assertEqual(ic.outputs, [1])

    def test_imm_lt_8(self):
        program = '3,3,1107,-1,8,3,4,3,99'
        ic = self.run_case(program, [7])
        self.assertEqual(ic.outputs, [1])
        ic = self.run_case(program, [3])
        self.assertEqual(ic.outputs, [1])
        ic = self.run_case(program, [9])
        self.assertEqual(ic.outputs, [0])

    def test_jump_pos(self):
        program = '3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9'
        ic = self.run_case(program, [7])
        self.assertEqual(ic.outputs, [1])
        ic = self.run_case(program, [3])
        self.assertEqual(ic.outputs, [1])
        ic = self.run_case(program, [0])
        self.assertEqual(ic.outputs, [0])

    def test_jump_imm(self):
        program = '3,3,1105,-1,9,1101,0,0,12,4,12,99,1'
        ic = self.run_case(program, [7])
        self.assertEqual(ic.outputs, [1])
        ic = self.run_case(program, [3])
        self.assertEqual(ic.outputs, [1])
        ic = self.run_case(program, [0])
        self.assertEqual(ic.outputs, [0])

    def test_999(self):
        program = '3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99'
        ic = self.run_case(program, [7])
        self.assertEqual(ic.outputs, [999])
        ic = self.run_case(program, [8])
        self.assertEqual(ic.outputs, [1000])
        ic = self.run_case(program, [1000])
        self.assertEqual(ic.outputs, [1001])

    def test_immediate(self):
        program = '1002,4,3,4,33'
        ic = self.run_case(program, [])
        self.assertEqual(ic.memory[4], 99)

def part2():
    memory = list(map(lambda m: int(m), open('5/input').readline().split(',')))
    ic = IntCodeComputer(memory, [5])
    while not ic.halted:
        ic.step()
    ic.print_memory()

part2() # 11981754

# if __name__ == '__main__':
#     unittest.main()
