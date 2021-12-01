from collections import defaultdict

def return_default():
    return 0

REAL=open("20.txt").readlines()
SAMPLE=open("20.sample").readlines()

def parse_lines(lines):
    return lines[0].strip()


def move(c, fastest, pos, depth):
    x, y = pos
    if c == "N":
        pos = (x, y+1)
    elif c == "S":
        pos = (x, y-1)
    elif c == "E":
        pos = (x+1, y)
    elif c == "W":
        pos = (x - 1, y)
    else:
        assert False
    if pos in fastest:
        comp = fastest[pos]
        if depth < comp:
            fastest[pos] = depth
    else:
        fastest[pos] = depth
    return pos

def solve(lines):
    parsed = parse_lines(lines)

    fastest = {}
    pos = (0, 0)
    depth = 0
    stack = []
    fastest[pos] = depth
    for c in parsed:
        if c in "NSEW":
            depth += 1
            pos = move(c, fastest, pos, depth)
        elif c == "(":
            stack.append((pos, depth))
        elif c == "|":
            pos, depth = stack[-1]
        elif c == ")":
            stack.pop()
    return max(fastest.values())

sample = solve(SAMPLE)
assert sample == 31
print("*** SAMPLE PASSED ***")

print(solve(REAL))
