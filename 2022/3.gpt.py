from collections import Counter

# The sum of the priorities
sum_of_priorities = 0

# Read the rucksacks from standard input
rucksacks = []
while True:
    try:
        line = input()
    except EOFError:
        # Stop reading when we reach the end of the input
        break
    rucksacks.append(line)

# Loop over the rucksacks
for rucksack in rucksacks:
    # Get the length of the rucksack
    n = len(rucksack)

    # Split the rucksack into two compartments
    compartment1 = rucksack[:n//2]
    compartment2 = rucksack[n//2:]

    # Count the items in each compartment
    compartment1_counts = Counter(compartment1)
    compartment2_counts = Counter(compartment2)

    # Find the items that appear in both compartments
    common_items = compartment1_counts & compartment2_counts

    # Loop over the common items
    for item, count in common_items.items():
        # Get the priority of the item
        if item.islower():
            priority = ord(item) - ord('a') + 1
        else:
            priority = ord(item) - ord('A') + 27

        # Add the priority to the sum
        sum_of_priorities += priority

# Print the sum of the priorities
print(sum_of_priorities)