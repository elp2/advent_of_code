class IntCodeComputer:
    def __init__(self, memory):
        self.pc = 0
        self.memory = memory
        self.halted = False
        self.debugging = True
        print('Memory: len=%d' % (len(self.memory)))

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

    def step(self):
        """Steps the machine 1 instruction, returning True if halted."""
        print('Step from PC=%d' % (self.pc))
        decoded_opcode = self.decode_opcode(self.eat_pc(True))
        opcode = decoded_opcode[0]
        if 1 == opcode or 2 == opcode:
            self.add_multiply_instruction(decoded_opcode)
        elif 3 == opcode:
            self.input_instruction(decoded_opcode)
        elif 4 == opcode:
            self.output_instruction(decoded_opcode)
        elif 99 == opcode:
            self.halt(decoded_opcode)
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
        address = self.eat_pc(True)
        self.set_memory(address, result)

    def input_instruction(self, decoded_opcode):
        address = self.eat_pc(True)
        while True:
            try:
                val = int(input('Enter value: '))
                break
            except ValueError:
                print('Enter integer value.')
        self.set_memory(address, val)

    def output_instruction(self, decoded_opcode):
        address = self.eat_pc(True)
        print('Output: %d' % (self.memory[address]))

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


def part1():
    day2_memory = list(map(lambda m: int(m), open('5/input').readline().split(',')))
    ic = IntCodeComputer(day2_memory)
    while not ic.halted:
        ic.step()
    ic.print_memory()

def test(program):
    print('Testing: %s' % (program))
    memory = list(map(lambda m: int(m), program.split(',')))
    ic = IntCodeComputer(memory)
    while not ic.halted:
        ic.step()
    ic.print_memory()

test('1002,4,3,4,33')
test('1101,100,-1,4,0')

# part1() # 9025675