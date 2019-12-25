import unittest

from amplifiers import Amplifiers

class TestAdapters(unittest.TestCase):
    def disabled_test_highest_one(self):
        program = '3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0'
        a = Amplifiers(program)
        [max_output, max_powers] = a.find_highest_signal()
        self.assertEqual(max_output, 43210)
        self.assertEqual(max_powers, (4,3,2,1,0))

    def test_highest_feedback_one(self):
        program = '3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5'
        a = Amplifiers(program)
        [max_output, max_powers] = a.find_highest_feedback()
        self.assertEqual(max_powers, (9,8,7,6,5))
        self.assertEqual(max_output, 139629729)

    def disabled_test_highest_feedback_two(self):
        program = '3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10'
        a = Amplifiers(program)
        [max_output, max_powers] = a.find_highest_feedback()
        self.assertEqual(max_powers, (9,7,8,5,6))
        self.assertEqual(max_output, 18216)


if __name__ == '__main__':
    unittest.main()
