def sum_doubles():
    numbers = open('1.txt').readline()
    numbers = numbers + numbers[0]
    total = 0
    for i in range(len(numbers) - 1):
        a = int(numbers[i])
        b = int(numbers[i+1])
        if a == b:
            total += a
    return total

# print(sum_doubles()) # 1341

def sum_halfway(numbers):
    total = 0
    delta = int(len(numbers) / 2)
    for i in range(len(numbers) - 1):
        bi = (i + delta) % len(numbers)
        a = int(numbers[i])
        b = int(numbers[bi])
        if a == b:
            total += a
    return total

print(sum_halfway(open('1.txt').readline())) # 1348
# print(sum_halfway("12131415"))
