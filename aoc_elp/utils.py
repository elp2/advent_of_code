from functools import cmp_to_key
import os

##### Parse Hints #####
# Simple parse - parse as all one type
# split = list(map(int, line.split(" "))) # All Ints

# Using Parse Library
# split = parse("{:d} {:s}", line) # Simple - unnamed
# split = parse("{name:s} {height:d}", line) # Parse with field names
# assert split # Make sure line was parsed

# Sorts with cmp. cmp < 0 for a < b, == 0 for a==b, > 0 for a > b.
def elpsort(array, cmp):
    return sorted(array, key=cmp_to_key(cmp))

ON_CHAR = '\u2588' # █
OFF_CHAR = '\u2592' # ▒

LEFT = (-1, 0)
UP = (0, -1)
RIGHT = (1, 0)
DOWN = (0, 1)
CHAR_TO_DS = {"^": UP, ">": RIGHT, "<": LEFT, "v": DOWN}
DS = [LEFT, UP, RIGHT, DOWN] # +IDX = TURN RIGHT
def TURN_RIGHT90(dir):
    return DS[(DS.index(dir) + 1) % 4]
def TURN_LEFT90(dir):
    return DS[(DS.index(dir) + 3) % 4]

UPLEFT = (-1, -1)
UPRIGHT = (1, -1)
DOWNRIGHT = (1, 1)
DOWNLEFT = (-1, 1)
DS8 = [LEFT, UPLEFT, UP, UPRIGHT, RIGHT, DOWNRIGHT, DOWN, DOWNLEFT] # +IDX = TURN RIGHT
def TURN_RIGHT45(dir):
    return DS8[(DS8.index(dir) + 1) % 4]
def TURN_LEFT45(dir):
    return DS8[(DS8.index(dir) + 7) % 4]

def arounds(x, y, diagonals):
    ret = []
    for dx, dy in DS8 if diagonals else DS:
        ret.append((x + dx, y + dy))
    return ret

def get_raw_inputs(argv):
    def get_challenge_day():
        return argv[0].split("/")[-1].replace("p2.py", "").replace(".py", "")
    def get_aoc_dir():
        return os.path.dirname(argv[0])
    
    print("Day: ", get_challenge_day())
    try:
        sample_file = os.path.join(get_aoc_dir(), get_challenge_day() + ".s.txt")
        SAMPLE = open(sample_file).read()
    except:
        assert None, "Missing Sample File: %s" % (sample_file)

    try:
        solutions_file = os.path.join(get_aoc_dir(), get_challenge_day() + ".txt")
        REAL = open(solutions_file).read()
    except:
        assert None, "Missing Solutions File: %s" % (solutions_file)

    return SAMPLE, REAL