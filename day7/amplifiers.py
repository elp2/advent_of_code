import itertools

import sys
sys.path.append('..')
from intcode.intcode import IntCodeComputer

class Amplifiers:
    def __init__(self, program):
        self.memory = list(map(lambda m: int(m), program.split(',')))

    def find_highest_signal(self):
        power_combos = list(itertools.permutations([0, 1, 2, 3, 4], 5))
        print('Working on %d combos.' % (len(power_combos)))
        max_output = 0
        max_powers = []
        for powers in power_combos:
            amp_input = 0
            print(powers)
            for i in range(0, 5):
                ic = IntCodeComputer(self.memory[:], [powers[i], amp_input])
                ic.debugging = False
                ic.run_until_halt()
                [amp_input] = ic.outputs
            if amp_input > max_output:
                max_output = amp_input
                max_powers = powers
        print('MAX OUTPUT: %d' % (max_output))
        return [max_output, max_powers]

    def find_highest_feedback(self):
        power_combos = list(itertools.permutations([5, 6, 7, 8, 9], 5))
        print('Working on %d combos.' % (len(power_combos)))
        max_output = 0
        max_powers = []
        for powers in power_combos:
            amp_input = 0
            ics = []
            for i in range(0, 5):
                ic = IntCodeComputer(self.memory[:], [powers[i]])
                ics.append(ic)
            while ics[4].halted == False:
                for i in range(0, 5):
                    ic = ics[i]
                    if ic.halted:
                        continue
                    ic.inputs.append(amp_input)
                    while True:
                        if ic.halted:
                            break
                        if len(ic.outputs):
                            [amp_input] = ic.outputs
                            ic.outputs = []
                            assert 0 == len(ic.inputs) # All inputs should be consumed.
                            break
                        ic.step()
                
                if i == 4 and amp_input > max_output:
                    max_output = amp_input
                    max_powers = powers
                
        print('MAX FEEDBACK OUTPUT: %d' % (max_output))
        return [max_output, max_powers]


a = Amplifiers(open('input').readline())
a.find_highest_signal()