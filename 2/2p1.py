program = open('input').readline()
#program = '2,4,4,5,99,0'
memory = map(lambda ram: int(ram), program.split(','))
pc = 0
memory[1] = 12
memory[2] = 2

print(memory)

while True:
    opcode = memory[pc]
    if 99 == opcode:
        print('HALTING!!!')
        break

    if 1 == opcode or 2 == opcode:
        input1 = memory[memory[pc+1]]
        input2 = memory[memory[pc+2]]
        destination = memory[pc+3]
        if 1 == opcode:
            result = input1 + input2
        else:
            result = input1 * input2
        memory[destination] = result
        print(opcode, '[', destination, ']', input1, input2, result)
        pc += 4
    else:
        print('Unknown opcode', opcode, ' at ', pc)
        break


print(memory) # 12490719