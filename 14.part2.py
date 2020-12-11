from collections import defaultdict

def return_default():
    return 0

REAL=704321

def parse_lines(lines):
    return list(map(int, lines))


def solve(target):
    tarr = list(map(int, str(target)))
    tlen = len(tarr)
    arr = [None] * (200 * 704321 + 20)
    arr[0] = 3
    arr[1] = 7
    arrlen = 2
    i1 = 0
    i2 = 1

    partial = []
    while True:
        here1 = arr[i1]
        here2 = arr[i2]
        summed = here1 + here2
        if summed >= 10:
            arr[arrlen] = 1
            arrlen += 1
            summed -= 10
        arr[arrlen] = summed
        arrlen += 1
        i1 = (i1 + here1 + 1) % arrlen
        i2 = (i2 + here2 + 1) % arrlen
        if arr[arrlen - tlen:arrlen] == tarr:
            return arrlen - tlen

    return ret

for si in range(3):
    expected = [9, 18, 2018][si]
    sample = [51589, 92510, 59414][si]
    actual = solve(sample)
    assert actual == expected

REAL=704321
print("SOLVED: ", solve(REAL)) 
# 126228040 too high 200 * 700k items
