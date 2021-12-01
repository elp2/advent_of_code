from collections import defaultdict

def return_default():
    return 0

CHALLENGE_DAY = "3"
REAL = open(CHALLENGE_DAY + ".txt").readlines()
SAMPLE = open(CHALLENGE_DAY + ".sample").readlines()


def parse_lines(lines):
    return list(map(lambda x: list(x.strip()), lines))


def solve(lines):
    parsed = parse_lines(lines)
    ret = 0
    dx = 3
    dy = 1
    y = 0
    x = 0
    TREE = "#"
    trees = 0
    while y < len(parsed):
        x = x % len(parsed[y])
        here = parsed[y][x]
        if here == TREE:
            trees += 1
        x += dx
        y += dy


    return trees
sample = solve(SAMPLE)
assert sample == 7
print("*** SAMPLE PASSED ***")

print(solve(REAL))
