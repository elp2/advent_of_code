# part2

total_fuel = 0
for line in open('input').readlines():
    mass = int(line.strip())
    fuel = mass / 3 - 2
    while(fuel > 0):
        total_fuel += fuel
        fuel = fuel / 3 - 2

print(total_fuel) # 4736213