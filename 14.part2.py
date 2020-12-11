from collections import defaultdict

def return_default():
    return 0

REAL=704321

def parse_lines(lines):
    return list(map(int, lines))


def solve(target):
    tarr = list(map(int, str(target)))
    arr = [3, 7]
    i1 = 0
    i2 = 1

    while True:
        if len(arr) % 100000 == 0:
            print(len(arr))
        here1 = arr[i1]
        here2 = arr[i2]
        summed = here1 + here2
        if summed >= 10:
            arr.append(1)
            if arr[-len(tarr):] == tarr:
                return len(arr) - len(tarr)
            summed -= 10
        arr.append(summed)
        i1 = (i1 + here1 + 1) % len(arr)
        i2 = (i2 + here2 + 1) % len(arr)
        if arr[-len(tarr):] == tarr:
            return len(arr) - len(tarr)


for si in range(3):
    expected = [9, 18, 2018][si]
    sample = [51589, 92510, 59414][si]
    actual = solve(sample)
    assert actual == expected
print("Solving")
REAL=704321
print("SOLVED: ", solve(REAL)) 
# 126228040 too high 200 * 700k items
