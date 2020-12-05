from collections import defaultdict

def return_default():
    return 0

CHALLENGE_DAY = "5"
REAL = open(CHALLENGE_DAY + ".txt").readlines()
SAMPLE = open(CHALLENGE_DAY + ".sample").readlines()


def parse_lines(lines):
    return lines


def seat_id(p):
    p = p.strip()
    start = 0
    end = 128
    for fb in p[0:7]:
        ran = (end - start) / 2
        if "F" == fb:
            end -= ran
        else:
            start += ran
        # print(start, end, ran)
    assert end - start == 1
    row = int(start)
    start = 0
    end = 8
    for lr in p[7:]:
        ran = int(end - start) / 2
        if "L" == lr:
            end -= ran
        else:
            start += ran
        # print(start, end, ran)
    assert start == end - 1
    col = int(start)
    return row * 8 + col

def solve(lines):
    parsed = parse_lines(lines)
    ids = {}
    for l in parsed:
        ids[seat_id(l)] = True

    s = sorted(ids.keys())
    for i in range(2, len(s) - 1):
        if s[i-1] + 1 != s[i]:
            return (i, s[i], s[i-1])
    print(s)

print(solve(REAL))
