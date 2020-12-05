from collections import defaultdict

def return_default():
    return 0

CHALLENGE_DAY = "5"
REAL = open(CHALLENGE_DAY + ".txt").readlines()
SAMPLE = open(CHALLENGE_DAY + ".sample").readlines()


def parse_lines(lines):
    return list(map(int, lines))


def solve(lines):
    parsed = parse_lines(lines)
    ret = 0

    return ret

sample = solve(SAMPLE)
assert sample == 1
print("*** SAMPLE PASSED ***")

solved = solve(REAL)
print("SOLUTION: ", solved)
# assert solved
