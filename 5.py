def execute(input):
    instructions = list(map(int, input))
    pc = 0
    steps = 0
    while pc >= 0 and pc < len(instructions):
        steps += 1
        jump = instructions[pc]
        instructions[pc] += 1
        pc += jump
    return steps

# assert 5 == execute("""0
# 3
# 0
# 1
# -3""".split("\n"))

# print(execute(open("5.txt").readlines())) # 364539

