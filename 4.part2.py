from collections import defaultdict

def return_default():
    return 0

CHALLENGE_DAY = "4"
REAL = open(CHALLENGE_DAY + ".txt").read()
SAMPLE = open(CHALLENGE_DAY + ".sample2").read()


def parse_lines(lines):
    ports = []
    lines = lines.split("\n\n")
    for line in lines:
        line = line.replace("\n", " ")
        line = line.strip()
        port = {}
        fields = line.split(" ")
        for f in fields:
            k, v = f.split(":")
            port[k] = v
        ports.append(port)
    return ports


def valid_port(port):
    try:
        if not (1920 <= int(port["byr"]) <= 2002):
            return False
        if not (2010 <= int(port["iyr"]) <= 2020):
            return False
        if not (2020 <= int(port["eyr"]) <= 2030):
            return False

        hgt = port["hgt"]
        unit = hgt[-2:]
        num = int(hgt[0:-2])
        if unit == "in":
            if not (59 <= num <= 76):
                return False
        elif unit == "cm":
            if not (150 <= num <= 193):
                return False
        else:
            return False
        hcl = port["hcl"]
        if "#" != hcl[0]:
            return False
        if len(hcl) != 7:
            return False
        for c in hcl[1:]:
            if c not in "0123456789abcdef":
                return False
        if port["ecl"] not in "amb blu brn gry grn hzl oth".split(" "):
            return False
        if len(port["pid"]) != 9:
            return False
    except KeyError:
        return False
    return True


def solve(lines):
    parsed = parse_lines(lines)
    ret = 0
    fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]
    for port in parsed:
        seen = []
        for f in fields:
            if f in port:
                seen.append(f)
        if valid_port(port):
            ret += 1
        else:
            print("Rejected:", port)

    return ret

sample = solve(SAMPLE)
assert 4 == sample
print("*** SAMPLE PASSED ***")

print(solve(REAL))
assert 179 == solve(REAL)
