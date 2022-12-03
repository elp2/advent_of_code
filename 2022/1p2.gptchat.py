# Read the input lines
lines = []
while True:
  try:
    line = input()
  except EOFError:
    break
  lines.append(line)

# Calculate the total Calories for each Elf
group_calories = []
total_calories = 0
for line in lines:
  if line == '':
    # A blank line indicates the end of an Elf's inventory
    group_calories.append(total_calories)
    total_calories = 0
  else:
    # Add the Calories to the current Elf's total
    total_calories += int(line)

# Sum the largest three groups of Calories
group_calories.sort(reverse=True)
result = sum(group_calories[:3])

# Return the result
print(f'The sum of the largest three groups of Calories is {result}.')