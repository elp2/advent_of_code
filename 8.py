from collections import defaultdict

class Computer:
    def __init__(self):
        def retzero(): return 0
        self.registers = defaultdict(retzero)


    def condition_true(self, look_reg, condition, value):
        look_value = self.registers[look_reg]
        if condition == "==":
            return look_value == value
        elif condition == ">=":
            return look_value >= value
        elif condition == ">":
            return look_value > value
        elif condition == "<":
            return look_value < value
        elif condition == "<=":
            return look_value <= value
        elif condition == "!=":
            return look_value != value
        assert False


    def execute(self, ins):
        action_reg, action, amount, _, look_reg, condition, value = ins.split(" ")
        amount = int(amount)
        value = int(value)
        if not self.condition_true(look_reg, condition, value):
            return
        
        delta = 0
        if action == "inc":
            delta = amount
        elif action == "dec":
            delta = -1 * amount
        else:
            assert False
        
        self.registers[action_reg] += delta

    def max_register(self):
        return max(self.registers.values())


def run_program(name):
    program = open(name).readlines()
    computer = Computer()
    for line in program:
        computer.execute(line)
    return computer.max_register()

assert 1 == run_program("8.sample")
print(run_program("8.txt")) # 5102
