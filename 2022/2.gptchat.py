# Import the sys module
import sys

# Initialize the score
score = 0

# Define the rules of the game
# HEAVILY UPDATED.
rules = {
    'A': {'X': 3 + 1, 'Y': 6 + 2, 'Z': 0 + 3},
    'B': {'X': 0 + 1, 'Y': 3 + 2, 'Z': 6 + 3},
    'C': {'X': 6 + 1, 'Y': 0 + 2, 'Z': 3 + 3},
}

# Open the strategy guide file
with open(sys.argv[1], 'r') as f:
    # Read the strategy guide from the file
    strategy_guide = f.read()

# Parse the strategy guide and calculate the score
for line in strategy_guide.split('\n'):
    if not line:
        continue

    # Get the opponent's choice and your response
    opponent, response = line.split()

    # Look up the outcome and update
    score  += rules[opponent][response]


print(score)