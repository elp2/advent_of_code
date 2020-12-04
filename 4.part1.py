from collections import defaultdict

def return_default():
    return 0

CHALLENGE_DAY = "4"
REAL = open(CHALLENGE_DAY + ".txt").readlines()
SAMPLE = open(CHALLENGE_DAY + ".sample").readlines()


def parse_lines(lines):
    ports = []
    port = {}
    for line in lines:
        if len(line.strip()) == 0:
            ports.append(port)
            port = {}
        else:
            line = line.strip()
            fields = line.split(" ")
            for f in fields:
                k, v = f.split(":")
                port[k] = v
    if len(port):
          ports.append(port)
    return ports

def solve(lines):
    parsed = parse_lines(lines)
    ret = 0
    fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]
    for port in parsed:
        seen = []
        for f in fields:
            if f in port:
                seen.append(f)
        valid = False
        if len(seen) == 8:
            valid = True
        if len(seen) == 7 and "cid" not in seen:
            valid = True
        if valid:
            ret += 1

    return ret

sample = solve(SAMPLE)
assert sample == 2
print("*** SAMPLE PASSED ***")

print(solve(REAL))
