from collections import defaultdict

def return_default():
    return 0

CHALLENGE_DAY = "3"
REAL = open(CHALLENGE_DAY + ".txt").readlines()
SAMPLE = open(CHALLENGE_DAY + ".sample").readlines()


def parse_lines(lines):
    return list(map(lambda x: list(x.strip()), lines))


def solve(lines, dx, dy):
    parsed = parse_lines(lines)
    ret = 0
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

rets = []
for (dx, dy) in [(1, 1), (3, 1), (5, 1), (7,1), (1, 2)]:
    rets.append(solve(REAL, dx, dy))

print(rets)

a = rets[0]
for m in rets[1:]:
    a *= m
print(a)