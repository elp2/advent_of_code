from collections import defaultdict

def return_default():
    return 0

CHALLENGE_DAY = "6"
REAL = open(CHALLENGE_DAY + ".txt").read().split("\n\n")
SAMPLE = open(CHALLENGE_DAY + ".sample").read().split("\n\n")


def parse_lines(lines):
    return list(map(lambda l:l.split("\n"), lines))


def solve(lines):
    parsed = parse_lines(lines)
    ret = 0
    for group in parsed:
        ans = defaultdict(return_default)
        for line in group:
            for c in line.strip():
                ans[c] += 1

        all = list(filter(lambda a: a == len(group), list(ans.values())))
        print(all, ans, len(ans.keys()))
        ret += len(all)
    return ret

sample = solve(SAMPLE)
assert sample == 6
print("*** SAMPLE PASSED ***")

solved = solve(REAL)
print("SOLUTION: ", solved)
# assert solved
