def execute(jump_strings):
    instructions = list(map(int, jump_strings))
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

def execute2(jump_strings):
    instructions = list(map(int, jump_strings))
    pc = 0
    steps = 0
    while pc >= 0 and pc < len(instructions):
        steps += 1
        jump = instructions[pc]
        if jump >= 3:
            instructions[pc] -= 1
        else:
            instructions[pc] += 1
        pc += jump
    return steps


assert 10 == execute2("""0
3
0
1
-3""".split("\n"))

print(execute2(open("5.txt").readlines())) # 27477714
