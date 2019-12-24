def pattern_for(i, num):
    pattern = [0] * i
    j = 1 # Skip zeroes, use special case above.
    sequence = [0, 1, 0, -1]
    while len(pattern) < len(num):
        pattern += [sequence[j]] * (i + 1)
        j += 1
        j = j % 4
    return pattern

def part1():
    num = open('input').readline().strip()

    for round in range(0, 100):
        new_num = ''
        for i in range(0, len(num)):
            pattern = pattern_for(i, num)
            new_digit = 0
            for j in range(0, len(num)):
                new_digit += int(num[j]) * pattern[j]
            new_digit = abs(new_digit)
            new_digit = new_digit % 10
            new_num += str(new_digit)
        num = new_num

    print(num)

# part1() # 9074471474

