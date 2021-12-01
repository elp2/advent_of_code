from collections import defaultdict

def return_default():
    return 0

REAL=704321

def parse_lines(lines):
    return list(map(int, lines))


def solve(target):
    arr = [None] * (704321 + 20)
    arr[0] = 3
    arr[1] = 7
    arrlen = 2
    i1 = 0
    i2 = 1
    while arrlen < target + 10:
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

    ret = "".join(map(str, arr[target:target + 10]))        

    return ret

for si in range(4):
    sample = [9, 5, 18, 2018][si]
    expected = ["5158916779", "0124515891", "9251071085", "5941429882"][si]
    actual = solve(sample)
    assert actual == expected

REAL=704321
print(solve(REAL))
