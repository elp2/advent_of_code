import sys
sys.path.append('..')
from intcode.intcode import IntCodeComputer

class AsciiComputer:
    def __init__(self):
        self.ic = IntCodeComputer(list(map(lambda m: int(m), open('input').readline().split(','))))
        self.ic.debugging = False
        self.output_string = ''

    def run(self):
        while self.ic.halted == False:
            self.ic.step()

        for char in self.ic.outputs:
            self.output_string += chr(char)

        return self.output_string

if __name__ == "__main__":
    ac = AsciiComputer()
    print(ac.run())