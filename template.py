from collections import defaultdict

def return_default():
    return 0

REAL=open("1.txt").readlines()
SAMPLE=open("1.sample").readlines()

def parse_lines(lines):
    return list(map(int, lines))


def solve(lines):
    parsed = parse_lines(lines)
    ret = 0

    return ret

sample = solve(SAMPLE)
assert sample == 1
print("*** SAMPLE PASSED ***")

print(solve(REAL))
