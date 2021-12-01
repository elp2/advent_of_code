from collections import defaultdict

def return_default():
    return 0

REAL=open("2.txt").readlines()
SAMPLE=open("2.sample").readlines()

def parse_lines(lines):
    def parse_line(line):
        split = line.split(" ")
        times = split[0]
        tmin, tmax = times.split("-")
        tmin = int(tmin)
        tmax = int(tmax)
        letter = split[1].replace(":", "")
        password = split[2]
        return ((tmin, tmax), letter, password)
    return list(map(parse_line, lines))


def solve(lines):
    parsed = parse_lines(lines)
    ret = 0
    for p in parsed:
        (tmin, tmax), letter, password = p
        la = password[tmin - 1] == letter
        lb = password[tmax - 1] == letter
        if (la and not lb) or (lb and not la):
            ret += 1

    return ret

sample = solve(SAMPLE)
assert sample == 1
print("*** SAMPLE PASSED ***")

print(solve(REAL))
