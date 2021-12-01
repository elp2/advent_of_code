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
            return score
        return False

#     If one of the first three is empty, and we can jump to the 4th, do it.
BASE = """NOT A J
    NOT B T
    OR T J
    NOT C T
    OR T J
    AND D J
    """

def part1():
    sd = SpringDroid()
    assert sd.execute(BASE + 'WALK\n') == 19350938
    # 19350938

def part2():
    sd = SpringDroid()

    # .ABCDEFGHI
    #      ABCDEFGHI
    # We need to find a path from A->D->H (maybe I?).
    # A->D->
    #       (Jump) H, walk to I or jump past.
    #      -> E -Jump-> I
    #           -> F -jump> pos after I
    # D and ((E AND (F OR I)) OR H)


    script = BASE + """NOT F T
    NOT T T
    """ # T = F
    script += """OR I T
    """ #T = F OR I
    script += """AND E T
    """ # T = (F OR I) AND E
    script += """OR H T
    """ # T = H OR ((F OR I) AND E)
    script += """AND T J
    """ # Jump if we have a path AND above.


    script += 'RUN\n'
    assert sd.execute(script) == 1142986901


if __name__ == "__main__":
    part1()
    part2()