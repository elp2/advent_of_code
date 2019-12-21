# Fuel required to launch a given module is based on its mass. 
# #Specifically, to find the fuel required for a module, take its mass, 
# # divide by three, round down, and subtract 2.

total_fuel = 0
for line in open('input').readlines():
    mass = int(line.strip())
    fuel = mass / 3 -2
    total_fuel += fuel

print(total_fuel)