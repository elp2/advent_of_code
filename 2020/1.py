REAL=open("1.txt").readlines()
SAMPLE=open("1.sample").readlines()

def parse_lines(lines):
    return list(map(int, lines))

def part1(lines):
    parsed = parse_lines(lines)
    for i in range(len(parsed) - 2):
        for j in range(i + 1, len(parsed) - 1):
            a = parsed[i]
            b = parsed[j]

            if a + b == 2020:
                print(a, b)
                return a * b
    return ret

assert part1(SAMPLE) == 514579
print(part1(REAL))

def part2(lines):
    parsed = parse_lines(lines)
    for i in range(len(parsed) - 2):
        for j in range(i + 1, len(parsed) - 1):
            for k in range(j + 1, len(parsed)):
                a = parsed[i]
                b = parsed[j]
                c = parsed[k]

                if a + b + c == 2020:
                    print(a, b, c)
                    return a * b * c
    return ret

assert part2(SAMPLE) == 241861950
print(part2(REAL)) # 236430480
