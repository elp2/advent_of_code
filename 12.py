from collections import defaultdict, deque
import re

CHALLENGE_DAY = "12"
REAL = open(CHALLENGE_DAY + ".txt").read()

def parse_lines(raw):
  return raw

def solve(raw):
    nums = list(map(lambda x: int(x), re.findall(r'(-?[0-9]+)', raw)))
    return sum(nums)


def dictify(line):
    assert line[0] == "{"
    depth = 1
    endi = 1
    while True:
        if line[endi] == "{":
            depth += 1
        elif line[endi] == "}":
            depth -= 1
            assert depth >= 0
            if depth == 0:
                return line[1:endi], endi
        endi += 1


def solve2(raw):
    if type(raw) == type('red'):
        return 0
    elif type(raw) == type(1):
        return raw
    elif type(raw) == type(dict()):
        if 'red' in raw.values():
            return 0
        else:
            return solve2(list(raw.values()))
    elif type(raw) == type([]):
        ret = 0
        for a in raw:
            ret += solve2(a)
        return ret
    else:
        assert False


solved = solve(REAL)
print("SOLUTION1: ", solved)

solved = solve2(eval(REAL))
print("SOLUTION2: ", solved)
