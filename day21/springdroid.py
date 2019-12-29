import sys
sys.path.append('..')
from intcode.intcode import IntCodeComputer

class SpringDroid:
    def __init__(self):
        self.ic = IntCodeComputer(list(map(lambda m: int(m), open('input').readline().split(','))))
    
    def execute(self, springscript):
        """Returns the amount of damage detected, or None if it fell in a hole."""
        self.ic.inputs = list(map(lambda x: ord(x), springscript))

        while not self.ic.halted:
            if self.ic.next_opcode() == 3 and len(self.ic.inputs) == 0:
                break
            self.ic.step()
        
        out = ''
        score = None
        for char in self.ic.outputs:
            if char >= 0 and char < 255:
                out += chr(char)
            else:
                assert score == None
                score = char
        print(out)
        if score:
            print('SCORE: %d' % (score))
        return False

# .
# ...
# .##.

def part1():
    sd = SpringDroid()
    sd.execute('NOT C J\nAND D J\nNOT A T\nOR T J\nWALK\n')
    # 19350938

def part2():
    sd = SpringDroid()
    sd.execute('NOT C J\nAND D J\nNOT A T\nOR T J\nRUN\n')


if __name__ == "__main__":
    part2()