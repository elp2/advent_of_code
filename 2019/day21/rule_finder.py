from itertools import product
from collections import defaultdict

def key(arr):
    return ''.join(map(lambda x: '#' if x else '.', arr))

JUMP = 4
VISION = 9

BASE_HULL = [True] * 5
endings = list(product([True, False], repeat = 5))

death = defaultdict(lambda: 0)
life = defaultdict(lambda: 0)

def survivable_jump(hull, x):
    """Returns whether you can get through the hull."""
    pos = x
    while pos != len(hull):
        if hull[pos] == False:
            return False

        if pos + JUMP < len(hull) and hull[pos + JUMP] == True and survivable_jump(hull, pos + JUMP):
            return True

        pos += 1
    return True

for end in endings:
    end = list(end)
    if end == [False, False, False, False, False]:
        # Would be unjumpable, assume these don't exist in the data.
        continue
    for end2 in endings:
        end2 = list(end2)
        if end2 == [False, False, False, False, False]:
            # Would be unjumpable, assume these don't exist in the data.
            continue

        hull = BASE_HULL + end + end2
        for x in range(0, 6):
            if hull[x] == False:
                # Couldn't jump from a empty spot
                continue
            vision = key(hull[x + 1:x + 1 + VISION])
            if survivable_jump(hull, x):
                life[vision] += 1
            else:
                death[vision] += 1

for key in life.keys():
    if key not in death:
        print('TOTALLY SAFE!: ', key)
print(life)

# Only SAFE key is #...., everything else is inherently unsafe.
# Need to send test springdroids to determine the particular set.
# AND 6 * 2 poss
# NOT 6 * 2 poss
# OR 6 * 2 poss            
