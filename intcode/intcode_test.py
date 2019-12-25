import unittest

from intcode import IntCodeComputer

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

    def test_output_copy(self):
        program = '109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99'
        ic = self.run_case(program, [])
        self.assertEqual(ic.outputs, list(map(lambda ins: int(ins), program.split(','))))

    def test_outputs_16_digit_number(self):
        program = '1102,34915192,34915192,7,4,7,99,0'
        ic = self.run_case(program, [])
        self.assertEqual(ic.outputs, [1219070632396864])

    def test_outputs_large_number(self):
        program = '104,1125899906842624,99'
        ic = self.run_case(program, [])
        self.assertEqual(ic.outputs, [1125899906842624])

    def test_203(self):
        program = '109,7,203,0,204,0,99,123'
        ic = self.run_case(program, [29])
        self.assertEqual(ic.outputs, [29])
        self.assertEqual(ic.memory[7], 29)

if __name__ == '__main__':
    unittest.main()