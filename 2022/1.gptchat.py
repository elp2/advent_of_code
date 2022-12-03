# Read the input lines
lines = []
while True:
  try:
    line = input()
  except EOFError:
    break
  lines.append(line)

# Calculate the total Calories for each Elf
total_calories = 0
max_calories = 0
for line in lines:
  if line == '':
    # A blank line indicates the end of an Elf's inventory
    max_calories = max(max_calories, total_calories)
    total_calories = 0
  else:
    # Add the Calories to the current Elf's total
    total_calories += int(line)

# Return the maximum total Calories
print(f'The maximum total Calories is {max_calories}.')