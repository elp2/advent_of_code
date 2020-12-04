from collections import defaultdict

def return_default():
    return 0

CHALLENGE_DAY = "4"
REAL = open(CHALLENGE_DAY + ".txt").readlines()
SAMPLE = open(CHALLENGE_DAY + ".sample2").readlines()


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

def valid_port(port):
    try:
        byr = int(port["byr"])
        if byr < 1920 or byr > 2002:
            return False
        iyr = int(port["iyr"])
        if iyr < 2010 or iyr >2020:
            return False
        eyr = int(port["eyr"])
        if eyr < 2020 or eyr > 2030:
            return False
        hgt = port["hgt"]
        unit = hgt[-2:]
        num = int(hgt[0:-2])
        if unit == "in":
            if num < 59 or num > 76:
                return False
        elif unit == "cm":
            if num < 150 or num > 193:
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
        # if len(seen) != 8:
        #     continue
        # if len(seen) == 7 and "cid" in seen:
        #     continue
        if valid_port(port):
            ret += 1
        else:
            print("Rejected:", port)

    return ret

sample = solve(SAMPLE)
assert 4 == sample
print("*** SAMPLE PASSED ***")

print(solve(REAL))
