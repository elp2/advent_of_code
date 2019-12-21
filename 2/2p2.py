program = open('input').readline()
#program = '2,4,4,5,99,0'
starting_memory = list(map(lambda ram: int(ram), program.split(',')))
pc = 0


noun = 0
verb = 0

while noun < 100:
    pc = 0
    memory = starting_memory[:]
    memory[1] = noun
    memory[2] = verb
    while True:
        opcode = memory[pc]
        if 99 == opcode:
            #print('HALTING!!!', memory[0])
            if memory[0] == 19690720:
                print("SOULUTION!!!", noun, verb)
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
            # print(opcode, '[', destination, ']', input1, input2, result)
            pc += 4
        else:
            print('Unknown opcode', opcode, ' at ', pc)
            break
    #print(noun, verb, memory[0])
    #print(memory)
    if verb == 99:
        verb = 0
        noun += 1
        #print('new noun', noun)
    else:
        # print(verb)
        verb += 1


# 2003